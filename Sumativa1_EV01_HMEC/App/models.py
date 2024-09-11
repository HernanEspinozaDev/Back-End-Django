from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class TipoVehiculo(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo

class Vehiculo(models.Model):
    patente = models.CharField(max_length=10)
    nro_chasis = models.CharField(max_length=50)
    nro_motor = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()
    tipo_vehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    posee_seguro = models.BooleanField()
    observaciones = models.TextField()

    def __str__(self):
        return self.patente
