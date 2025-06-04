from django import forms
from .models import *

# Formulario para agregar una oficina
class agregar_oficina_form(forms.ModelForm):
	class Meta:
		model = Oficina
		fields = '__all__'

# Formulario para agregar un empleado
class agregar_empleado_form(forms.ModelForm):
	class Meta:
		model = Empleados
		fields = '__all__'
		
# Formulario para agregar una solicitud
class agregar_solicitud_form(forms.ModelForm):
	solCodigo = forms.CharField(
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
		