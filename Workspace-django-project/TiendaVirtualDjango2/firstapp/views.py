from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.
# fisrtsApp --> view.py

def display(request):
    return HttpResponse("<h1> Hola Mundo!</h1>")

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b>Fecha y Hora Actual: </b>" + str(dt)
    return HttpResponse(s)
