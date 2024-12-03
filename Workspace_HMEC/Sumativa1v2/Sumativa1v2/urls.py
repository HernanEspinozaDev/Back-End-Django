"""
URL configuration for Sumativa1v2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.agregarReserva),
    path('eliminarReserva/<int:id>', views.eliminarReserva),
    path('actualizarReserva/<int:id>', views.actualizarReserva),
    path('pdf/<int:id>/', views.generar_pdf, name='generar_pdf'),
    path('qr_pdf/<int:id>/', views.generar_qr_pdf, name='generar_qr_pdf'),  # Nueva ruta
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
