from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.forms import CreacionAuto
from home.models import Auto
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicio(request):
    # return HttpResponse('<h1>HOLA</h1>')
    return render(request, 'home/inicio.html')
    # return HttpResponse('<h1 asd="asdasd" asd="asdasd" asd="asdasd"/>')

@login_required
def crear_auto(request):
    
    print('ESTOS SON LOS DATOS DEL GET -->>', request.GET)
    print('ESTOS SON LOS DATOS DEL POST -->>', request.POST)
    
    if request.method == "POST":
        formulario = CreacionAuto(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            auto = Auto(marca=info.get('marca'), modelo=info.get('modelo'), fecha_creacion=info.get('fecha_creacion'))
            auto.save()
            return redirect('listado_de_autos')
    else:
        formulario = CreacionAuto()
    
    return render(request, 'home/crear_auto.html', {'formulario': formulario})

def listado_de_autos(request):
    autos = Auto.objects.all()
    return render(request, 'home/listado_de_autos.html', {'autos': autos})

def detalle_auto(request, auto_en_especifico):
    auto = Auto.objects.get(id=auto_en_especifico)
    return render(request, 'home/detalle_auto.html', {'auto': auto})

class VistaDetalleAuto(DetailView):
    model = Auto
    template_name = "home/detalle_auto.html"

class VistaModificarAuto(LoginRequiredMixin, UpdateView):
    model = Auto
    template_name = "home/modificar_auto.html"
    fields = ["marca", "modelo", "fecha_creacion"]
    success_url = reverse_lazy('listado_de_autos')

class VistaEliminarAuto(LoginRequiredMixin, DeleteView):
    model = Auto
    template_name = "home/eliminar_auto.html"
    success_url = reverse_lazy('listado_de_autos')
