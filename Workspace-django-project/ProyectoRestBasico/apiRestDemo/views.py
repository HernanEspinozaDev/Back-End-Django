from django.http import JsonResponse
from django.shortcuts import render
from apiRestDemo.models import Employee


# Create your views here.
def employeeview(request):
    emp={
        'id':123,
        'name':'Clark',
        'email':'a@bx.cl',
        'salary': 5000
    }
    return JsonResponse(emp)

def employeeviewBD(request):
    empleados = Employee.objects.all()
    data = {'Employees': list(empleados.values('name', 'salary'))}
    return JsonResponse(data)