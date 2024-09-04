from django.contrib import admin
from django.urls import path

###### forma 1
from secondapp import views as app2

urlpatterns = [
    path("saludo/", app2.saludo),
]
