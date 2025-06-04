from .forms import *
from django.shortcuts import render,redirect
from .models import *
import random
import string

def inicio(request):
    return render(request,'inicio.html')


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

def vista_agregar_empleado(request):
	if request.method == 'POST':
		formulario = agregar_empleado_form(request.POST, request.FILES)
		if formulario.is_valid():
			emple = formulario.save(commit = False)
			emple.status = True
			emple.save()
			formulario.save_m2m()
			return redirect ('/inicio/')
	else:
		formulario = agregar_empleado_form()
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
        if form_anexo.is_valid() and form_anexo.cleaned_data['aneUrl']:
            anexo = form_anexo.save(commit=False)
            anexo.aneSolicitud = solicit
            anexo.save()
            return redirect('/inicio/')
    else:
        codigo = generarcodigo_solicitud()
        formulario = agregar_solicitud_form(initial={'solCodigo': codigo})
        form_anexo = agregar_anexoSolicitudes_form()
    return render(request, 'vista_agregar_solicitud.html', {'formulario': formulario, 'form_anexo': form_anexo})

