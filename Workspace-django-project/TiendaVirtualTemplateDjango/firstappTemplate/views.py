from django.shortcuts import render

def rendertemplate(request):
    return render(request, 'templatefirstapp/template1.html')

def rendertemplatedata(request):
    data = {"nombre": "Tere"}
    return render(request, 'templatefirstapp/template2.html', data)

def infoUsuario(request):
    data = {
        "id": "123",
        "nombre": "Teresa Tapia",
        "email": "teresa.tapia02@hotmail.com"
    }
    return render(request, 'templatefirstapp/userInfoTemplate.html', data)

def infoUsuarioImagen(request):
    data = {
        "id": "123",
        "nombre": "Teresa Tapia",
        "email": "teresa.tapia02@hotmail.com"
    }
    return render(request, 'templatefirstapp/userInfoTemplateImagen.html', data)
