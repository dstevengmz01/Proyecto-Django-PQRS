from django.db import models
from django.contrib.auth.models import AbstractUser

#1###
class Oficina(models.Model):
    ofiNombre=models.CharField(max_length=50)
    def __str__ (self):
            return self.ofiNombre
#2###
class Empleados(models.Model):
    empIdentificacion=models.CharField(max_length=10,unique=True)
    empNombres=models.CharField(max_length=50)
    empApellidos=models.CharField(max_length=50)
    empCorreo=models.CharField(max_length=50)
    empOficina = models.ForeignKey(Oficina, on_delete=models.PROTECT)
    def __str__(self):
            return f"{self.empNombres} {self.empApellidos}" 

#Choise 
class TipoUsuario(models.TextChoices):
    Administrador = 'Administrador', 'Administrador'
    Empleado = 'Empleado', 'Empleado'

#3
class Usuario(AbstractUser):
    # usuEmpleado = models.ForeignKey(Empleados, on_delete=models.PROTECT)
    useFoto=models.ImageField(upload_to='fotosusuario',null=True,blank=True)
    usuEmpleado = models.ForeignKey(Empleados, on_delete=models.PROTECT, null=True, blank=True)  
    usoTipo=models.CharField(max_length=20,choices=TipoUsuario,null=True)
    def __str__ (self):
            return self.username


#Choise 
class SolForma(models.TextChoices):
    Anonimo = 'Anonimo', 'Anonimo'
    Correo_Electronico = 'Correo Electronico', 'Correo Electronico'


#Choise     
class solTipo(models.TextChoices):
    Peticion = 'Peticion', 'Peticion'
    Queja = 'Queja', 'Queja'
    Reclamo ='Reclamo','Reclamo'
    
#Choise
class solEstado(models.TextChoices):
    Solicitada= 'Solicitada','Solicitada'
    Atendida  = 'Atendidad','Atendida'
    
#4
class Solicitud(models.Model):
    solCodigo=models.CharField(max_length=20,unique=True)
    solForma=models.CharField(max_length=20,choices=SolForma,default=SolForma.Correo_Electronico)
    solTipo=models.CharField(max_length=10,choices=solTipo,default=solTipo.Peticion)
    solOficina=models.ForeignKey(Oficina,on_delete=models.PROTECT)
    solBarrio=models.CharField(max_length=50,blank=True)
    solNombreCiudadano=models.CharField(max_length=50,blank=True,null = True)
    solCorreoElectronico=models.CharField(max_length=50,blank=True,null = True)
    solDescripcion=models.TextField()
    solFecha=models.DateField(auto_now_add=True)
    solEstado=models.CharField(max_length=20,choices=solEstado,default=solEstado.Solicitada)
    def __str__ (self):
            return self.solCodigo

#5
class AnexoSolicitudes(models.Model):
    aneSolicitud=models.ForeignKey(Solicitud, on_delete=models.PROTECT)
    aneUrl=models.FileField(upload_to='anexos/',null = True, blank = True)
    def __str__ (self):
            return self.aneUrl

#6
class RespuestSolicitud(models.Model):
    resSolicitud=models.ForeignKey(Solicitud, on_delete=models.PROTECT)
    resDescripcion=models.TextField()
    resUrlAnexo=models.FileField(upload_to='Anexossolicitudes/')
    resFecha=models.DateField(auto_now_add=True)
    resEmpleado=models.ForeignKey(Empleados, on_delete=models.PROTECT)
    def __str__ (self):
            return self.resUrlAnexo