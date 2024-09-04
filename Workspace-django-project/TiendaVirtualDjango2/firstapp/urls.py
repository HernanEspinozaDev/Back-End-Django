from django.contrib import admin
from django.urls import path

###### forma 1
from firstapp import views as app1

urlpatterns = [
    path('hola/', app1.display),
    path('ahora/', app1.displayDateTime),
]
