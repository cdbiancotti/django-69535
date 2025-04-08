from django.urls import path
from home.views import inicio, crear_auto, listado_de_autos

urlpatterns = [
    path('', inicio, name='inicio'),
    path('autos/', listado_de_autos, name='listado_de_autos'),
    path('autos/crear/', crear_auto, name='crear_auto'),
]
