import qrcode
from io import BytesIO
from django.core.files import File
from django.db import models, connection
from datetime import date

class EstadReserva(models.Model):
    estadoReservaId = models.CharField(primary_key=True, max_length=3)
    estadoReservaNombre = models.CharField(max_length=20)

    def __str__(self):
        return "{}".format(self.estadoReservaNombre)

class TipoReserva(models.Model):
    tipoSolicitudId = models.CharField(primary_key=True, max_length=3)
    tipoSolicitud = models.CharField(max_length=20)

    def __str__(self):
        return "{}".format(self.tipoSolicitud)

class Reserva(models.Model):
    idSolicitud = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    fecha_nacimiento = models.DateField()  # Nuevo campo
    fechareserva = models.DateField()
    horareserva = models.TimeField()
    cantidad_hermanos = models.IntegerField()
    foto_carnet = models.ImageField(upload_to='fotos/')
    fecha_creacion = models.DateTimeField()
    fecha_modificacion = models.DateTimeField()
    observaciones = models.CharField(max_length=5000)
    website = models.URLField()
    email = models.EmailField()
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True, null=True)
    estadoReservaId = models.ForeignKey(
        'EstadReserva', null=True, blank=False, on_delete=models.RESTRICT)
    tipoSolicitudId = models.ForeignKey(
        'TipoReserva', null=True, blank=False, on_delete=models.RESTRICT)

    @property
    def edad(self):
        today = date.today()
        return today.year - self.fecha_nacimiento.year - (
            (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )

    def save(self, *args, **kwargs):
        # Obtener la fecha y hora actual desde la base de datos
        if not self.idSolicitud:
            with connection.cursor() as cursor:
                cursor.execute("SELECT CURRENT_TIMESTAMP")
                row = cursor.fetchone()
                self.fecha_creacion = row[0]
        with connection.cursor() as cursor:
            cursor.execute("SELECT CURRENT_TIMESTAMP")
            row = cursor.fetchone()
            self.fecha_modificacion = row[0]

        # Generar datos del QR
        qr_data = f'Reserva: {self.nombre}, Fecha: {self.fechareserva}, Hora: {self.horareserva}'
        qr_image = qrcode.make(qr_data)

        # Guardar la imagen en un buffer
        qr_buffer = BytesIO()
        qr_image.save(qr_buffer, format='PNG')
        qr_buffer.seek(0)

        # Asignar la imagen generada al campo qr_code
        self.qr_code.save(f'{self.nombre}_qr.png', File(qr_buffer), save=False)

        # Llamar al método save del modelo original
        super().save(*args, **kwargs)
