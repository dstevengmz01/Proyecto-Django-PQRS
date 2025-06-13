from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


# Formulario para agregar una oficina
class agregar_oficina_form(forms.ModelForm):
	class Meta:
		model = Oficina
		fields = '__all__'

# Formulario para agregar un empleado
class agregar_empleado_form(forms.ModelForm):
      empIdentificacion = forms.CharField(
		label='Código de Empleado',
		widget=forms.TextInput(attrs={'readonly': 'readonly'}))
      class Meta:
        model = Empleados
        fields = '__all__'
		
		
# Formulario para agregar una solicitud
class agregar_solicitud_form(forms.ModelForm):
	solCodigo  = forms.CharField(
		label='Código de Solicitud',
		widget=forms.TextInput(attrs={'readonly': 'readonly'}))
	class Meta:
		model = Solicitud
		fields = '__all__'
		widgets = {
			'solNombreCiudadano': forms.TextInput(attrs={'id': 'id_solNombreCiudadano'}),
			'solCorreoElectronico': forms.EmailInput(attrs={'id': 'id_solCorreoElectronico'}),
			'solDescripcion': forms.Textarea(attrs={'id': 'id_solDescripcion'}),
		}

class agregar_anexoSolicitudes_form(forms.ModelForm):
    class Meta:
        model = AnexoSolicitudes
        fields = ['aneUrl']
		
#Usuario Formulario
class Registro_usuario_form(UserCreationForm):
    class Meta:
        model = Usuario
		# fields = '__all__'
        fields = ['username', 'password1', 'password2', 'email', 'useFoto', 'usuEmpleado', 'usoTipo']


# Formulario de autenticación
class Login_form(AuthenticationForm):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
        
class respuesta_Solicitud_form(forms.ModelForm):
    class Meta:
        model = RespuestSolicitud
        fields = ['resDescripcion', 'resUrlAnexo']
        widgets = {
            'resDescripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'resUrlAnexo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }