Sumativa1v2
Este es un proyecto Django creado por Hernán Espinoza que implementa un sistema de administración de reservas con características avanzadas como:

Subida de imágenes de foto tamaño carnet.
Registro de fecha y hora de creación y modificación directamente desde la base de datos.
Envío de correos electrónicos al usuario al guardar una reserva.
Generación y almacenamiento de códigos QR asociados a las reservas.
Generación de PDFs con los datos de la reserva y el código QR.

Estructura del Proyecto

Sumativa1v2/
├── App
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── templatetags
│   │   ├── __init__.py
│   │   └── custom_tags.py
│   ├── tests.py
│   └── views.py
├── Sumativa1v2
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── media
│   ├── fotos
│   └── qrcodes
├── static
│   ├── css
│   ├── images
│   └── js
└── templates
    └── templatesApp
        └── agregar.html
Requisitos Previos
Python 3.8 o superior
MySQL Server
Entorno virtual (recomendado)
Git (opcional, si clonas desde un repositorio)
Pasos para Configurar y Ejecutar el Proyecto
Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local.

1. Clonar el Repositorio
Clónalo usando:

git clone https://github.com/HernanEspinozaDev/Back-End-Django.git
Si no, descarga el código fuente y descomprímelo en tu máquina.
navega con cd hasta la carpeta Workspace_HMEC y luego a Sumativa1v2

2. Crear y Activar un Entorno Virtual
Es recomendable usar un entorno virtual para aislar las dependencias del proyecto.

En Windows:

python -m venv venv
venv\Scripts\activate

En macOS/Linux:

python3 -m venv venv
source venv/bin/activate

3. Instalar las Dependencias
Asegúrate de estar en el directorio raíz del proyecto (donde está manage.py) y ejecuta:

pip install -r requirements.txt

4. Configurar la Base de Datos
El proyecto utiliza MySQL como base de datos.

Instala MySQL Server si no lo tienes instalado.

Crea una base de datos llamada sumativa1v2 (o el nombre que prefieras).

Puedes hacerlo desde la línea de comandos de MySQL:


CREATE DATABASE sumativa1v2;
Configura las credenciales en Sumativa1v2/settings.py.


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sumativa1v2',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


5. Realizar las Migraciones
Aplica las migraciones para crear las tablas en la base de datos:


python manage.py makemigrations
python manage.py migrate

6. Crear un Superusuario (Opcional)
Si deseas acceder al panel de administración de Django:


python manage.py createsuperuser

Sigue las instrucciones en pantalla para crear el superusuario.

7. Configurar el Envío de Correos Electrónicos

El proyecto envía correos electrónicos al guardar una reserva. Configura el backend de correo en Sumativa1v2/settings.py:


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tu_correo@gmail.com'
EMAIL_HOST_PASSWORD = 'tu_contraseña'
Recomendación de Seguridad:

No incluyas las credenciales directamente en el código.
Utiliza variables de entorno para almacenar EMAIL_HOST_USER y EMAIL_HOST_PASSWORD.
Si usas Gmail, puede que necesites crear una contraseña de aplicación o habilitar el acceso de aplicaciones menos seguras.

8. Configurar Archivos de Medios y Estáticos

En Sumativa1v2/settings.py, asegúrate de tener las siguientes configuraciones:

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

En Sumativa1v2/urls.py, añade las siguientes líneas al final:

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... tus otras rutas ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
9. Ejecutar el Servidor de Desarrollo
Inicia el servidor:

python manage.py runserver
Accede a la aplicación en tu navegador web en http://127.0.0.1:8000/.

Funcionalidades de la Aplicación
Agregar Reserva: Completa el formulario para agregar una nueva reserva. Los campos incluyen nombre, teléfono, fecha de nacimiento, fecha y hora de reserva, cantidad de hermanos, foto carnet, observaciones, sitio web, email, estado y tipo de reserva.

Confirmación y Envío de Correo: Al guardar la reserva, se muestra un mensaje de confirmación y se envía un correo electrónico al usuario.

Generación de Código QR: Se genera y almacena un código QR asociado a la reserva.

Generación de PDFs: Puedes descargar un PDF con los datos de la reserva y otro con el código QR.

Tabla de Reservas: Visualiza todas las reservas con detalles como nombre, teléfono, edad calculada, fecha de solicitud, estado, acciones, etc.

Editar y Eliminar Reservas: Puedes actualizar o eliminar reservas existentes.

Notas Importantes
Configuración de Gmail: Si utilizas Gmail para el envío de correos, puede que necesites configurar una contraseña de aplicación o habilitar el acceso de aplicaciones menos seguras.

Seguridad: Nunca almacenes contraseñas o información sensible en el código fuente. Utiliza variables de entorno o servicios de gestión de secretos.

Dependencias Adicionales: Asegúrate de que las siguientes bibliotecas están instaladas:

qrcode: Para generar códigos QR.
Pillow: Para manejar imágenes.
reportlab: Para generar PDFs.

Estas deberían instalarse al ejecutar pip install -r requirements.txt.

Contacto
Si tienes alguna pregunta o necesitas ayuda adicional, no dudes en ponerte en contacto con el desarrollador del proyecto Hernán Espinoza.

¡Gracias por utilizar este sistema de administración de reservas!