from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.forms import CreacionAuto
from home.models import Auto

def inicio(request):
    # return HttpResponse('<h1>HOLA</h1>')
    return render(request, 'home/inicio.html')
    # return HttpResponse('<h1 asd="asdasd" asd="asdasd" asd="asdasd"/>')

def crear_auto(request):
    
    print('ESTOS SON LOS DATOS DEL GET -->>', request.GET)
    print('ESTOS SON LOS DATOS DEL POST -->>', request.POST)
    
    if request.method == "POST":
        formulario = CreacionAuto(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            auto = Auto(marca=info.get('marca'), modelo=info.get('modelo'))
            auto.save()
            return redirect('listado_de_autos')
    else:
        formulario = CreacionAuto()
    
    return render(request, 'home/crear_auto.html', {'formulario': formulario})

def listado_de_autos(request):
    autos = Auto.objects.all()
    return render(request, 'home/listado_de_autos.html', {'autos': autos})