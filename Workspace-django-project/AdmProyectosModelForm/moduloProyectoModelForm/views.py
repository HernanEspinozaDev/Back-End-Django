from django.shortcuts import render, redirect
from moduloProyectoModelForm.models import Proyecto
from moduloProyectoModelForm.forms import FormProyecto


# Create your views here.
def index(request):
    return render(request, 'templateModuloProyecto/index.html')

def listadoProyectos(request):
    return render(request, 'templateModuloProyecto/proyectos.html')

def agregarProyecto(request):
    return render(request, 'templateModuloProyecto'+'\\'+'agregar.html')

def agregarProyecto(request):
    formu = FormProyecto()
    if request.method == 'POST':
        formu = FormProyecto(request.POST)
        if formu.is_valid():
            formu.save()
            return redirect('/proyectos')  # return #index(request)

    data = {'formu': formu, 'titulo': 'AGREGAR PROYECTO'}
    return render(request, 'templateModuloProyecto/agregar.html', data)
