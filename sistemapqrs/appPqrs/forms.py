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

class agregar_solicitud_form(forms.ModelForm):
	solCodigo = forms.CharField(
        required=False,
        label='Código de Solicitud',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
	solForma = forms.ChoiceField(choices=SolForma.choices, required=True, label='Forma de Solicitud')
	solTipo = forms.ChoiceField(choices=solTipo.choices, required=True, label='Tipo de Solicitud')
	solOficina = forms.ModelChoiceField(queryset=Oficina.objects.all(), required=True, label='Oficina')
	solBarrio = forms.CharField(max_length=50, required=False, label='Barrio')
	solNombreCiudadano = forms.CharField(max_length=50, required=False, label='Nombre del Ciudadano')
	solCorreoElectronico = forms.EmailField(max_length=50, required=False, label='Correo Electrónico')
	solDescripcion = forms.CharField(widget=forms.Textarea, required=True, label='Descripción de la Solicitud')
	solFecha=forms.DateField(widget=forms.SelectDateWidget, required=False, label='Fecha de Solicitud')
	solEstado = forms.ChoiceField(choices=solEstado.choices, initial=solEstado.Solicitada, required=True, label='Estado de la Solicitud')
	class Meta:
		model= Solicitud
		fields= '__all__'
