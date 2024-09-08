from django.shortcuts import render
from moduloEmpleados.models import Employee

# Create your views here.
def getListadoEmpleados(request):
    empleados = Employee.objects.all()
    data = {'empleados': empleados}
    return render(request, 'templateModuloEmpleado/listadoEmpleados.html', data)
