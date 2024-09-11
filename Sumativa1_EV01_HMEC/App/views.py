from django.shortcuts import render, redirect
from .models import Vehiculo
from .forms import VehiculoForm

def inicio(request):
    return render(request, 'inicio.html')

def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'listarVehiculo.html', {'vehiculos': vehiculos})

def agregar_vehiculo(request):
    vehiculos = Vehiculo.objects.all()  # Obtener todos los vehículos para mostrarlos en la tabla
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            vehiculo = form.save(commit=False)
            vehiculo.patente = form.cleaned_data['patente']
            vehiculo.save()
            return redirect('agregar_vehiculo')  # Recargar la página después de guardar
    else:
        form = VehiculoForm()
    
    return render(request, 'agregarVehiculo.html', {'form': form, 'vehiculos': vehiculos})


def actualizar_vehiculo(request, id):
    vehiculo = Vehiculo.objects.get(id=id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('listar_vehiculos')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'agregarVehiculo.html', {'form': form})

def eliminar_vehiculo(request, id):
    vehiculo = Vehiculo.objects.get(id=id)
    vehiculo.delete()
    return redirect('listar_vehiculos')
