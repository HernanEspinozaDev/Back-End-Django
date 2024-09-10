from django.contrib import admin
from .models import Proyecto

# Register your models here.
class ProyectoAdmin(admin.ModelAdmin):
    list_display = [
        'fechaInicio',
        'fechaTermino',
        'nombre',
        'responsable',
        'prioridad'
    ]

admin.site.register(Proyecto, ProyectoAdmin)
