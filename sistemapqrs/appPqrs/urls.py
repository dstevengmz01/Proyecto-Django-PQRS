from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('agregar_oficina/',views.vista_agregar_oficina, name = 'vista_agregar_oficina'),
    path('agregar_empleado/',views.vista_agregar_empleado, name = 'vista_agregar_empleado'),
    path('agregar_solicitud/',views.vista_agregar_solicitud, name = 'vista_agregar_solicitud'),
]