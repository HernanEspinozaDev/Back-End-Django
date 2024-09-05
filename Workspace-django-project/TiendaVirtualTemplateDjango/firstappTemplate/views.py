from django.shortcuts import render

def rendertemplate(request):
    return render(request, 'templatefirstapp/template1.html')
