from .forms import *
from django.shortcuts import render,redirect
from .models import *
import random
import string
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .correo import enviar_correo_asincrono 
from django.urls import reverse

User = get_user_model()

def generar_contraseña():
	contrasena = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
	return contrasena

def vista_agregar_usuario(request):
	if request.method == 'POST':
		formulario = Registro_usuario_form(request.POST, request.FILES)
		if formulario.is_valid():
			usuario = formulario.save(commit = False)
			usuario.status = True
			usuario.save()
			formulario.save_m2m()
			return redirect ('/inicio/')
	else:
		formulario = Registro_usuario_form()
	return render(request, 'vista_agregar_usuario.html', locals()) 

@login_required
def inicio(request):
    return render(request,'inicio.html')

@login_required
def vista_agregar_oficina(request):
	if request.method == 'POST':
		formulario = agregar_oficina_form(request.POST, request.FILES)
		if formulario.is_valid():
			ofici = formulario.save(commit = False)
			ofici.status = True
			ofici.save()
			formulario.save_m2m()
			return redirect ('/inicio/')
	else:
		formulario = agregar_oficina_form()
	return render(request, 'vista_agregar_oficina.html', locals()) 

def generarcodigo_solicitudd():
	# codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
	codigo = ''.join(random.choices(string.digits, k=10)) 
	return codigo

@login_required
def vista_agregar_empleado(request):
	if request.method == 'POST':
		formulario = agregar_empleado_form(request.POST, request.FILES)
		if formulario.is_valid():
			emple = formulario.save(commit = False)
			emple.empIdentificacion = generarcodigo_solicitudd()
			emple.status = True
			emple.save()
			formulario.save_m2m()
			contraseña = generar_contraseña()
			nuevo_usuario = User.objects.create_user(
                username=emple.empCorreo,
                email=emple.empCorreo,
                password=contraseña,
                usuEmpleado=emple,
                usoTipo=TipoUsuario.Empleado
            )
			asunto = 'Tu acceso al sistema PQRS'
			mensaje = f"""
            Se ha creado tu cuenta con éxito.<br>
            <b>Usuario:</b> {nuevo_usuario.username}<br>
            <b>Contraseña:</b> {contraseña}<br><br>
             iniciar sesión en <a href="http://127.0.0.1:8000/login/">este enlace</a>.
            """
			enviar_correo_asincrono(emple.empCorreo, asunto, mensaje)
			return redirect ('/inicio/')
	else:
		codigoemple = generarcodigo_solicitudd()
		formulario = agregar_empleado_form(initial={'empIdentificacion': codigoemple})
		# formulario = agregar_empleado_form()
	return render(request, 'vista_agregar_empleado.html', locals()) 

#Generar codigo
def generarcodigo_solicitud():
	codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
	return codigo

# #Agregar Solicitud
# def vista_agregar_solicitud(request):
# 	if request.method == 'POST':
# 		formulario = agregar_solicitud_form(request.POST, request.FILES)
# 		form_anexo  = agregar_anexoSolicitudes_form(request.POST, request.FILES)
# 		if formulario.is_valid():
# 			solicit = formulario.save(commit = False)
# 			solicit.solCodigo = generarcodigo_solicitud()
# 			solicit.solBarrio = request.POST.get('solBarrio', '')
# 			solicit.status = True
# 			solicit.save()
# 			formulario.save_m2m()
# 		if form_anexo.is_valid() and form_anexo.cleaned_data['aneUrl']:
# 			anexo = form_anexo.save(commit=False)
# 			anexo.aneSolicitud = Solicitud 
# 			anexo.save.save_m2m()
# 			return redirect ('/inicio/')
# 	else:
# 		codigo = generarcodigo_solicitud()
# 		formulario = agregar_solicitud_form(initial={'solCodigo': codigo})
# 	return render(request, 'vista_agregar_solicitud.html', locals()) 


# Vista para agregar una solicitud y su anexo


def vista_agregar_solicitud(request):
    if request.method == 'POST':
        formulario = agregar_solicitud_form(request.POST, request.FILES)
        form_anexo = agregar_anexoSolicitudes_form(request.POST, request.FILES)
        if formulario.is_valid():
            solicit = formulario.save(commit=False)
            solicit.solCodigo = generarcodigo_solicitud()
            solicit.solBarrio = request.POST.get('solBarrio', '')
            solicit.status = True
            solicit.save()
            formulario.save_m2m()
            if form_anexo.is_valid():
                archivo = form_anexo.cleaned_data.get('aneUrl')
                if archivo:
                    anexo = form_anexo.save(commit=False)
                    anexo.aneSolicitud = solicit
                    anexo.save()
            return redirect('/inicio/')
        else:
            print("Errores en el formulario de solicitud:", formulario.errors)
    else:
        codigo = generarcodigo_solicitud()
        formulario = agregar_solicitud_form(initial={'solCodigo': codigo})
        form_anexo = agregar_anexoSolicitudes_form()
    return render(request, 'vista_agregar_solicitud.html', {'formulario': formulario,'form_anexo': form_anexo})


class VistaLogin(LoginView):
    template_name = 'login.html'
    authentication_form = Login_form
    def get_success_url(self):
        usuario = self.request.user
        if usuario.usoTipo == TipoUsuario.Empleado:
            return reverse('panel_empleado') 
        elif usuario.usoTipo == TipoUsuario.Administrador:
            return reverse('inicio')
        else:
            return reverse('inicio')
		

def vista_logout(request):
	logout(request)
	return redirect('login')


@login_required
def panel_empleado(request):
    usuario = request.user
    if usuario.usuEmpleado:
        empleado = usuario.usuEmpleado
        solicitudes = Solicitud.objects.filter(solOficina=empleado.empOficina)
    else:
        empleado = None
        solicitudes = []
    return render(request, 'panel_empleado.html', {'empleado': empleado,'solicitudes': solicitudes})