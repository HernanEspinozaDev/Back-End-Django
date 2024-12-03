from django.contrib import admin
from .models import Reserva, EstadReserva, TipoReserva

@admin.register(EstadReserva)
class EstadReservaAdmin(admin.ModelAdmin):
    list_display = ('estadoReservaId', 'estadoReservaNombre')

@admin.register(TipoReserva)
class TipoReservaAdmin(admin.ModelAdmin):
    list_display = ('tipoSolicitudId', 'tipoSolicitud')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('idSolicitud', 'nombre', 'telefono', 'fechareserva', 'horareserva', 'fecha_nacimiento', 'cantidad_hermanos', 'email', 'fecha_creacion', 'fecha_modificacion')
    readonly_fields = ('fecha_creacion', 'fecha_modificacion', 'qr_code')
