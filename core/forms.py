from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models


#--------------------------------------------------------------------------
#--EMPLEADOS--

class CreateEmpleadoNombre(forms.ModelForm):
        
    class Meta:
        model = models.Empleados
        fields = [
            'nombrepila',
            'primerapellido',
            'segundoapellido',
            'dircalle',
            'dirnumero',
            'dircolonia',
            'numtel',
            'horario',
            'areatrabajo',
            'puesto',
        ]

        widgets = {
            'nombrepila': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'primerapellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer Apellido'}),
            'segundoapellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Opcional: Segundo Apellido'}),
            'dircalle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Calle:'}),
            'dirnumero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de Calle'}),
            'dircolonia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Colonia'}),
            'numtel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numero de telefono'}),
            'horario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion de Horario'}),
            'areatrabajo': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecciona área de trabajo'}),
            'puesto': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecciona puesto'}),
        }
        
        labels = {
            'nombrepila': 'Nombre',
            'primerapellido': 'Primer Apellido',
            'segundoapellido': 'Segundo Apellido',
            'dircalle': 'Calle',
            'dirnumero': 'Número',
            'dircolonia': 'Colonia',
            'numtel': 'Número De Télefono',
            'horario': 'Horario',
            'areadetrabajo': 'Área De Trabajo',
            'puesto': 'Puesto',
            
        }
  
class CreateUser(UserCreationForm):
    username = forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe tu Username"}))
    password1 = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={"type":"password", "class":"form-control", "placeholder":"Escribe tu Password"}))
    password2 = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={"type":"password", "class":"form-control", "placeholder":"Confirma tu Password"}))
    email = forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe tu Email"}))
    
    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "email"
        ]

        widgets = {
             "username": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe tu Username"}),
             "password": forms.PasswordInput(attrs={"type":"password", "class":"form-control", "placeholder":"Escribe tu Password"}),
             "email": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe tu Email"}),
         }
        

class UpdateEmpleados(forms.ModelForm):        
    class Meta:
        model = models.Empleados
        fields = [
            'numero',
            'nombrepila',
            'primerapellido',
            'segundoapellido',
            'dircalle',
            'dirnumero',
            'dircolonia',
            'numtel',
            'horario',
            'areatrabajo',
            'puesto',
            'jefearea',
            
        ]
        

        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}) ,
            'nombrepila': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'primerapellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer Apellido'}),
            'segundoapellido': forms.TextInput(attrs={'class': 'form-control'}),
            'dircalle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Calle:'}),
            'dirnumero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de Calle'}),
            'dircolonia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Colonia'}),
            'numtel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numero de telefono'}),
            'horario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion de Horario'}),
            'areatrabajo': forms.Select(attrs={'class': 'form-control','placeholder': 'Selecciona área de trabajo'}),
            'puesto': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecciona puesto'}),
            'jefearea': forms.TextInput(attrs={'class': 'form-control', 'disabled': '', 'placeholder': 'Jefe'}),
        }

#--------------------------------------------------------------------------
#--PIEZAS--

class CreatePieza(forms.ModelForm):
    class Meta:
        model = models.Piezas
        fields = [
            'nombre',
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),            
            
        }
        
class UpdatePieza(forms.ModelForm):
    class Meta:
        model = models.Piezas
        fields =[
            'nombre',
        ]
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
#---------------------------------------------------------------------------

#--MATERIALES--

class CreateMaterial(forms.ModelForm):
    class Meta:
        model = models.Materiales
        fields = [
            'nombre',
            'stock'
            
        ]

        widgets = {
           'nombre': forms.TextInput(attrs={'class': 'form-control'}),
           'stock': forms.TextInput(attrs={'class':'form-control'})
            
        }

class UpdateMaterial(forms.ModelForm):
    class Meta:
        model = models.Materiales
        fields =[
            'nombre',
            'stock'
        ]
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'stock' : forms.TextInput(attrs={'class': 'form-control'}),
        }
#---------------------------------------------------------------------------
#--PUESTO DE TRABAJO--

class CreatePuesto(forms.ModelForm):
    class Meta:
        model = models.Puestos
        fields = [
            'nombre',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class UpdatePuesto(forms.ModelForm):
    class Meta:
        model = models.Puestos
        fields =[
            'nombre',
        ]
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
#------------------------------------------------------------------------
#               AREAS DE TRABAJO

class CreateArea(forms.ModelForm):
    class Meta:
        model = models.Areasdetrabajo
        fields = [
            'nombre',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class UpdateArea(forms.ModelForm):
    class Meta:
        model = models.Areasdetrabajo
        fields =[
            'nombre',
        ]
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
#--------------------------------------------------------------------------------
#               MODELOS

class CreateModelos(forms.ModelForm):
    class Meta:
        model = models.Modelos
        fields = [
            'nombre',
            'descripcion'

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),

        }
        
class UpdateModelos(forms.ModelForm):
    class Meta:
        model = models.Modelos
        fields =[
            'nombre',
            'descripcion'
            
        ]
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),

        }
#--------------------------------------------------------------------------------
#               ESTADOS

class CreateEstados(forms.ModelForm):
    class Meta:
        model = models.Estados
        fields = [
            'descripcion'

        ]

        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),

        }
        
class UpdateEstados(forms.ModelForm):
    class Meta:
        model = models.Estados
        fields =[
            'descripcion'
            
        ]
        
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),

        }
#--------------------------------------------------------------------------------
#               TAREAS

class CreateTareas(forms.ModelForm):
    class Meta:
        model = models.Tareas
        fields = [
            'orden'

        ]

        widgets = {
            'orden': forms.TextInput(attrs={'class': 'form-control'}),

        }
        
class UpdateTareas(forms.ModelForm):
    class Meta:
        model = models.Tareas
        fields =[
            'orden'
            
        ]
        
        widgets = {
            'orden': forms.TextInput(attrs={'class': 'form-control'}),

        }
#--------------------------------------------------------------------------------
#               ACTIVIDADES

class CreateActividades(forms.ModelForm):
    class Meta:
        model = models.Actividades
        fields = [
            'descripcion'

        ]

        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),

        }
        
class UpdateActividades(forms.ModelForm):
    class Meta:
        model = models.Actividades
        fields =[
            'descripcion'
            
        ]
        
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),

        }
#--------------------------------------------------------------------------------
#               ERRORES

class CreateErrores(forms.ModelForm):
    class Meta:
        model = models.Errores
        fields = [
            'descripcion'

        ]

        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),

        }
        
class UpdateErrores(forms.ModelForm):
    class Meta:
        model = models.Errores
        fields =[
            'descripcion'
            
        ]
        
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),

        }
#--------------------------------------------------------------------------------
#               SOLUCIONES

class CreateSoluciones(forms.ModelForm):
    class Meta:
        model = models.Actividades
        fields = [
            'descripcion'

        ]

        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),

        }
        
class UpdateSoluciones(forms.ModelForm):
    class Meta:
        model = models.Soluciones
        fields =[
            'descripcion'
            
        ]
        
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),

        }
#--------------------------------------------------------------------------------
#               METAS

class CreateMetas(forms.ModelForm):
    class Meta:
        model = models.Metas
        fields = [
            'meta'

        ]

        widgets = {
            'meta': forms.TextInput(attrs={'class': 'form-control'}),

        }
        
class UpdateMetas(forms.ModelForm):
    class Meta:
        model = models.Soluciones
        fields =[
            'descripcion'
            
        ]
        
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),

        }
    
#--------------------------------------------------------------------------------
#               BITACORA 

class CreateBitacora(forms.ModelForm):
    class Meta:
        model = models.Bitacoras
        fields = [
            'titulo',
            'empleado',
            # 'meta',
            'fecha',
        ]
        
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'empleado': forms.Select(attrs={'class': 'form-control'}),
            # 'meta': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class CreateBitAct(forms.ModelForm):
    class Meta:
        model = models.BitAct
        fields = [
            'bitacora',
            'actividad',
            'tiempo',
        ]
        
        widgets = {
            'bitacora': forms.Select(attrs={'class': 'form-control'}),
            'actividad': forms.TextInput(attrs={'class': 'form-control'}),
            'tiempo': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CreateBitTarea(forms.ModelForm):
    class Meta:
        model = models.BitTarea
        fields = [
            'bitacora',
            'tarea',
            'fechainicio',
            'fechafinal',
            'horainicio',
            'horafinal',
        ]
        
        widgets = {
            'bitacora': forms.Select(attrs={'class': 'form-control'}),
            'tarea': forms.Select(attrs={'class': 'form-control'}),
            'fechainicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'horainicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'fechafinal': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'horafinal': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

class CreateError(forms.ModelForm):
    class Meta:
        model = models.Errores
        fields = [
            'descripcion'
        ]

        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }
class CreateSolucion(forms.ModelForm):
    class Meta:
        model = models.Soluciones
        fields = [
            'descripcion'
        ]

        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }