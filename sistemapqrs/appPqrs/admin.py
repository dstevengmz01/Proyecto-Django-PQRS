from django.contrib import admin

from .models import *
admin.site.register(Oficina)
admin.site.register(Empleados)
admin.site.register(Usuario)
admin.site.register(Solicitud)
admin.site.register(AnexoSolicitudes)
admin.site.register(RespuestSolicitud)
