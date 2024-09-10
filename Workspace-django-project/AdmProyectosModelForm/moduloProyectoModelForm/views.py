from django.shortcuts import render, redirect
from moduloProyectoModelForm.models import Proyecto
from moduloProyectoModelForm.forms import FormProyecto


# Create your views here.
def index(request):
    return render(request, 'templateModuloProyecto/index.html')

def listadoProyectos(request):
    proyectos = Proyecto.objects.all()
    data = {'proyectos': proyectos}
    return render(request, 'templateModuloProyecto/proyectos.html', data)


def agregarProyecto(request):
    formu = FormProyecto()
    if request.method == 'POST':
        formu = FormProyecto(request.POST)
        if formu.is_valid():
            formu.save()
            return redirect('/proyectos')  # return #index(request)

    data = {'formu': formu, 'titulo': 'AGREGAR PROYECTO'}
    return render(request, 'templateModuloProyecto/agregar.html', data)

def eliminarProyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    proyecto.delete()
    return redirect('/proyectos')

def actualizarProyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    formu = FormProyecto(instance=proyecto)
    if request.method == 'POST':
        formu = FormProyecto(request.POST, instance=proyecto)
        if formu.is_valid():
            formu.save()
            return redirect('/proyectos')

    data = {'formu': formu, 'titulo': 'ACTUALIZAR PROYECTO'}
    return render(request, 'templateModuloProyecto/agregar.html', data)

