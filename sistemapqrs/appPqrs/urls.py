from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('agregar_oficina/',views.vista_agregar_oficina, name = 'vista_agregar_oficina'),
    path('agregar_empleado/',views.vista_agregar_empleado, name = 'vista_agregar_empleado'),
    path('agregar_solicitud/',views.vista_agregar_solicitud, name = 'vista_agregar_solicitud'),
    path('agregar_usuario/',views.vista_agregar_usuario, name = 'vista_agregar_usuario'),
    path('login/', views.VistaLogin.as_view(), name='login'),
    path('logout/',views.vista_logout,name="vista_logout"),
    path('panel/', views.panel_empleado, name='panel_empleado'),
    path('panel_administrador/', views.admin, name='panel_administrador'),
    path('responder/<int:solicitud_id>/', views.responder_solicitud, name='responder_solicitud'),
    path('consultarrespuesta/', views.consultar_respuesta, name='consultar_respuesta'),
    
]