from django.urls import path
from home.views import inicio, crear_auto, listado_de_autos, detalle_auto, VistaDetalleAuto, VistaModificarAuto, VistaEliminarAuto

urlpatterns = [
    path('', inicio, name='inicio'),
    path('autos/', listado_de_autos, name='listado_de_autos'),
    path('autos/crear/', crear_auto, name='crear_auto'),
    # path('autos/<int:auto_en_especifico>/', detalle_auto, name='detalle_auto'),
    path('autos/<int:pk>/', VistaDetalleAuto.as_view(), name='detalle_auto'),
    path('autos/<int:pk>/modificar/', VistaModificarAuto.as_view(), name='modificar_auto'),
    path('autos/<int:pk>/eliminar/', VistaEliminarAuto.as_view(), name='eliminar_auto'),
]
