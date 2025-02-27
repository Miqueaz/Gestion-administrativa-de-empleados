from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.cache import never_cache
from django.contrib import messages

from . import models
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
import requests
from .mixins import StaffRequiredMixin

from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.db.models import F, ExpressionWrapper, fields, CharField, Value, Count, OuterRef, Subquery, Sum




class paginaPrincipal(LoginRequiredMixin,generic.TemplateView):
    template_name = 'core/paginaPrincipal.html'
    context = {}
    
    login_url = reverse_lazy('home:LogIn')
    
    
    def get(self, request):
        user = request.user.id
        context = {}
        
        try:
            Empleado = models.Empleados.objects.get(usuario=user)
            User = request.user
        except models.Empleados.DoesNotExist:
            Empleado = None
            User = None
        
        if request.user.is_staff:
            
            Empleados = models.Empleados.objects.all()
            Taeras = models.Tareas.objects.all()
            Areas = models.Areasdetrabajo.objects.all()
            Modelos = models.Modelos.objects.all()
            
            
                          
            consulta2 = models.AtModelos.objects.values(
            'area', 'modelo__numero', 'modelo__nombre', 'modelo__descripcion', 'cantidad'
            )
            
            termino_busqueda = request.GET.get('q', '')

            resultados = models.Empleados.objects.filter(
                Q(numero__icontains=termino_busqueda) |
                Q(nombrepila__icontains=termino_busqueda) |
                Q(primerapellido__icontains=termino_busqueda) |
                Q(segundoapellido__icontains=termino_busqueda) |
                Q(puesto__nombre__icontains=termino_busqueda) |
                Q(areatrabajo__nombre__icontains=termino_busqueda)
            )
            
            context = {
                'Empleados': resultados,
                'termino_busqueda': termino_busqueda,
                'Tareas': Taeras,
                'Empleado': Empleado,
                'user': User,
                'Areasdetrabajo': Areas,
                'Modelos': consulta2
            }
        else:
            
            try:
                Empleado = models.Empleados.objects.get(usuario=user)
                User = request.user
                
                consulta = (
                    models.Tareas.objects.filter(
                        bittarea__bitacora__empleado__numero=Empleado.numero
                    ).values(
                        'numero', 'orden', 'estado__descripcion'
                    )
                )
                
                area = models.Areasdetrabajo.objects.get(nombre=Empleado.areatrabajo)               
                consulta2 = models.AtModelos.objects.filter(
                    area__nombre=Empleado.areatrabajo
                ).values(
                    'modelo__numero', 'modelo__nombre', 'modelo__descripcion', 'cantidad'
                )
                
                context = {
                    
                }
                
            except models.Empleados.DoesNotExist:
                Empleado = None
                User = None
                consulta = None
                area = None
                consulta2 = None
            
            context = {
                'Modelos': consulta2,
                'AreaTrabajo': area,
                'Tareas': consulta,
                'Empleado': Empleado,
                'user': User,
                
            }
        
        return render(request, self.template_name, context)
    

def verificar_contrasena(request, password):
    # Verificar la contraseña
    user = authenticate(request, username=request.user.username, password=password)

    if user is not None:
        # Contraseña correcta
        return JsonResponse({'valida': True})
    else:
        # Contraseña incorrecta
        return JsonResponse({'valida': False}, status=400)


#---------------Empleados--------------------------------
class registro(StaffRequiredMixin, generic.TemplateView):
    template_name = 'core/Empleados/registro.html'
    model = models.Empleados
    form_class_Empleados = forms.CreateEmpleadoNombre
    form_class_Usuarios = forms.CreateUser
    
    login_url = reverse_lazy('home:LogIn')
    success_url = reverse_lazy('core:empleados')
    
    def get(self, request):
        context = {
            'form_empleado': self.form_class_Empleados,
            'form_usuario': self.form_class_Usuarios
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form_empleado = self.form_class_Empleados(request.POST)
        form_usuario = self.form_class_Usuarios(request.POST)

        if form_empleado.is_valid() and form_usuario.is_valid():
            # Guardar datos de empleado
            empleado = form_empleado.save()

            # Guardar datos de usuario
            usuario = form_usuario.save(commit=False)
            usuario.set_password(form_usuario.cleaned_data['password1'])
            usuario.save()

            # Actualizar el campo 'usuario' en el empleado
            empleado.usuario = usuario
            empleado.save()

            messages.success(request, 'Registro exitoso!')
            return redirect('/OPPENHEIMER/empleados/')

        # Si alguno de los formularios no es válido
        messages.error(request, 'Hubo un error en el registro. Verifica los datos.')

        context = {
            'form_empleado': form_empleado,
            'form_usuario': form_usuario
        }
        return render(request, self.template_name, context)
    
class empleados(StaffRequiredMixin, generic.View):
    template_name = 'core/Empleados/empleados.html'
    model = models.Empleados
    
    login_url = reverse_lazy('home:LogIn')
    
    def get(self, request):
        Empleados = models.Empleados.objects.all()
        # context = {'Empleados': Empleados}
        
        termino_busqueda = request.GET.get('q', '')

        resultados = models.Empleados.objects.filter(
            Q(numero__icontains=termino_busqueda) |
            Q(nombrepila__icontains=termino_busqueda) |
            Q(primerapellido__icontains=termino_busqueda) |
            Q(segundoapellido__icontains=termino_busqueda) |
            Q(puesto__nombre__icontains=termino_busqueda) |
            Q(areatrabajo__nombre__icontains=termino_busqueda)
        )
            
        context = {
            'Empleados': resultados,
            'termino_busqueda': termino_busqueda,
        }
        
        return render(request, self.template_name, context)
    
class DetailEmpleado(StaffRequiredMixin, generic.UpdateView):
    template_name = 'core/Empleados/detailEmpleados.html'
    model = models.Empleados
    form_class = forms.UpdateEmpleados
    success_url = reverse_lazy("core:empleados")
    login_url = reverse_lazy('home:LogIn')
    
    def get_context_data(self, **kwargs):
        empleado = models.Empleados.objects.get(numero = self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['NumEmp'] = empleado.numero
        context['nombrepila'] = empleado.nombrepila
        context['primerapellido'] = empleado.primerapellido
        return context
        
class eliminarEmpleados(StaffRequiredMixin, generic.View):
    template_name = 'core/Empleados/empleados.html'
    model = models.Empleados
    success_url = reverse_lazy("core:Empleados")
    
    def get(self, request, pk):
        material = models.Empleados.objects.get(numero=pk)
        material.delete()
        material = models.Empleados.objects.all()
        messages.success(request, 'Se elimino el empleado')

        return redirect('/OPPENHEIMER/empleados/')

    
#--------------USER----------------------------------
    
class user(LoginRequiredMixin, generic.TemplateView):
    template_name = 'core/Perfil/user.html'
    model = models.Empleados
    context = {}
    
    def get(self, request):
        user = request.user.id
        print(user)
        
        try:
            Empleado = models.Empleados.objects.get(usuario=user)
            User = request.user
        except models.Empleados.DoesNotExist:
            Empleado = None
            User = None
            
        # print(f"Nombre: {Empleado.nombrepila}")
        self.context = {
            'Empleado': Empleado,
            'user': User
        }
        return render(request, self.template_name, self.context)
        

#---------------VIEWS PARA PIEZAS---------------------

    
class piezas(StaffRequiredMixin, generic.CreateView):
    template_name = 'core/Piezas/piezas.html'
    model = models.Piezas
    form_class = forms.CreatePieza
    
    
    success_url = reverse_lazy('core:piezas')
    login_url = reverse_lazy('home:LogIn')
    
    def get(self, request):
        response = requests.get('http://127.0.0.1:8000/api/v1/AtPiezas/')
        print(response.status_code)
        
        consulta = models.AtPiezas.objects.values(
        'pieza__numero','pieza__nombre', 
        ).annotate(
            stock=Sum('cantidadpieza')
        ).order_by(
            'pieza__nombre'
        )
 
        context = {
            'Piezas': consulta,
            'form': self.form_class
        }
        return render(request, self.template_name, context)   
        
class editarPiezas(StaffRequiredMixin, generic.UpdateView):
    
    template_name = 'core/Piezas/editarPiezas.html'
    model = models.Piezas
    form_class = forms.UpdatePieza
    
    
    
    success_url = reverse_lazy("core:piezas")
    login_url = reverse_lazy('home:LogIn')
    
class eliminarPiezas(StaffRequiredMixin, generic.View):
    template_name = 'core/Piezas/piezas.html'
    model = models.Piezas
    success_url = reverse_lazy("core:piezas")
    
    def get(self, request, pk):
        piezas = models.Piezas.objects.get(numero=pk)
        piezas.delete()
        piezas = models.Piezas.objects.all()
        messages.success(request, 'Se elimino la pieza')

        return redirect('/OPPENHEIMER/piezas/')
#------------------------------------------------------------
#              VIEWS PARA MATERIALES

class materiales(StaffRequiredMixin, generic.CreateView):
   template_name = 'core/Materiales/materiales.html'
   model = models.Materiales
   form_class = forms.CreateMaterial
   
   success_url = reverse_lazy('core:materiales')
   login_url = reverse_lazy('home:LogIn')
   
   def get(self, request):
       Materiales = models.Materiales.objects.all()
       context = {
           'Materiales': Materiales,
           'form': self.form_class
       }
       return render(request, self.template_name, context)

class editarMaterial(StaffRequiredMixin,generic.UpdateView):
    
    template_name = 'core/Materiales/editarMaterial.html'
    model = models.Materiales
    form_class = forms.UpdateMaterial
    
    
    success_url = reverse_lazy("core:materiales")
    login_url = reverse_lazy('home:LogIn')
    
class eliminarMaterial(StaffRequiredMixin, generic.DeleteView):
    
    def get(self, request, pk):
        material = models.Materiales.objects.get(numero=pk)
        material.delete()
        material = models.Materiales.objects.all()
        messages.success(request, 'Se elimino El material')


        return redirect('/OPPENHEIMER/materiales/')

#------------------------------------------------------------
#               PUESTO

class puesto(StaffRequiredMixin, generic.CreateView):
   template_name = 'core/PuestoTrabajo/puestos.html'
   model = models.Puestos
   form_class = forms.CreatePuesto
   
   success_url = reverse_lazy('core:puestos')
   login_url = reverse_lazy('home:LogIn')
   
   def get(self, request):
       Puestos = models.Puestos.objects.all()
       context = {
           'Puestos': Puestos,
           'form': self.form_class
       }
       return render(request, self.template_name, context)

class editarPuesto(StaffRequiredMixin,generic.UpdateView):
    
    template_name = 'core/PuestoTrabajo/editarPuestos.html'
    model = models.Puestos
    form_class = forms.UpdatePuesto
    
    
    success_url = reverse_lazy("core:puestos")
    login_url = reverse_lazy('home:LogIn')    

class eliminarPuesto(StaffRequiredMixin, generic.DeleteView):
    
    def get(self, request, pk):
        puesto = models.Puestos.objects.get(numero=pk)
        puesto.delete()
        puesto = models.Puestos.objects.all()
        messages.success(request, 'Se elimino el puesto')


        return redirect('/OPPENHEIMER/puestos/')


#-------------------------------------------------------------
#           ÁREAS DE TRABAJO

class areas(StaffRequiredMixin, generic.CreateView):
   template_name = 'core/AreaTrabajo/areas.html'
   model = models.Areasdetrabajo
   form_class = forms.CreateArea
   
   success_url = reverse_lazy('core:areas')
   login_url = reverse_lazy('home:LogIn')
   
   def get(self, request):
       Areas = models.Areasdetrabajo.objects.all()
       context = {
           'Areasdetrabajo': Areas,
           'form': self.form_class
       }
       return render(request, self.template_name, context)

class editarArea(StaffRequiredMixin,generic.UpdateView):
    
    template_name = 'core/AreaTrabajo/editarArea.html'
    model = models.Areasdetrabajo
    form_class = forms.UpdateArea
    
    
    success_url = reverse_lazy("core:areas")
    login_url = reverse_lazy('home:LogIn')     

class eliminarArea(StaffRequiredMixin, generic.DeleteView):
    
    def get(self, request, pk):
        areas = models.Areasdetrabajo.objects.get(numero=pk)
        areas.delete()
        areas = models.Areasdetrabajo.objects.all()
        messages.success(request, 'Se elimino el Area de Trabajo')


        return redirect('/OPPENHEIMER/areas/')

class areasTrabajo(StaffRequiredMixin, generic.TemplateView):
    template_name = 'core/AreaTrabajo/areasTrabajo.html'
    model = models.Areasdetrabajo
    
    success_url = reverse_lazy('core:areasTrabajo')
    login_url = reverse_lazy('home:LogIn')
   
    def get(self, request):
        consulta1 = models.Empleados.objects.values('areatrabajo__numero', 'areatrabajo__nombre').annotate(empleados=Count('areatrabajo')).order_by('areatrabajo__numero')
        
        consulta2 = models.AtModelos.objects.values(
        'area__numero', 'area__nombre' 
        ).annotate(
            Modelos=Sum('cantidad')
        ).order_by(
            'area__nombre'
        )
        
        context = {
            'AreasEmpleados': consulta1,
            'AreasModelos': consulta2,
        }
        return render(request, self.template_name, context)

class cantidadEmpleados(StaffRequiredMixin, generic.CreateView):
    template_name = 'core/AreaTrabajo/cantidadEmpleados.html'
    model = models.Empleados
    
    login_url = reverse_lazy('home:LogIn')
    success_url = reverse_lazy('core:empleados')
    
    def get(self, request, pk):
        area = models.Areasdetrabajo.objects.get(numero=pk)          
                
        consulta = models.Empleados.objects.filter(
            areatrabajo__numero=pk
        ).values(
            'numero', 'jefearea__nombrepila','jefearea__primerapellido', 'nombrepila','primerapellido', 'puesto__nombre'
        )
        
        context = {
            'Empleados': consulta,
            'AreaTrabajo': area
        }
        return render(request, self.template_name, context)

class cantidadModelos(StaffRequiredMixin, generic.CreateView):
    template_name = 'core/AreaTrabajo/cantidadModelos.html'
    model = models.Modelos
    
    login_url = reverse_lazy('home:LogIn')
    success_url = reverse_lazy('core:modelos')
    
    def get(self, request, pk):
        area = models.Areasdetrabajo.objects.get(numero=pk)               
        consulta = models.AtModelos.objects.filter(
            area__numero=pk
        ).values(
            'modelo__numero', 'modelo__nombre', 'modelo__descripcion', 'cantidad'
        )
        
        context = {
            'Modelos': consulta,
            'AreaTrabajo': area
        }
        return render(request, self.template_name, context)



#-------------------------------------------------------------
#               MODELOS
class modelos(StaffRequiredMixin, generic.CreateView):
   template_name = 'core/Modelos/modelos.html'
   model = models.Modelos
   form_class = forms.CreateModelos
   
   success_url = reverse_lazy('core:modelos')
   login_url = reverse_lazy('home:LogIn')
   
   def get(self, request):
       Modelos = models.Modelos.objects.all()
       context = {
           'Modelos': Modelos,
           'form': self.form_class
       }
       return render(request, self.template_name, context)

class editarModelos(StaffRequiredMixin,generic.UpdateView):
    
    template_name = 'core/Modelos/editarModelos.html'
    model = models.Modelos
    form_class = forms.UpdateModelos
    
    
    success_url = reverse_lazy("core:modelos")
    login_url = reverse_lazy('home:LogIn')     

class eliminarModelos(StaffRequiredMixin, generic.DeleteView):
    
    def get(self, request, pk):
        modelos = models.Modelos.objects.get(numero=pk)
        modelos.delete()
        modelos = models.Modelos.objects.all()
        messages.success(request, 'Se elimino el Modelo')


        return redirect('/OPPENHEIMER/modelos/')
    
class detailModelos(StaffRequiredMixin, generic.TemplateView):
   template_name = 'core/Modelos/detailModelos.html'
   model = models.Modelos
   
   success_url = reverse_lazy('core:modelos')
   login_url = reverse_lazy('home:LogIn')
   
   def get(self, request, pk):
        Modelos = models.Modelos.objects.get(numero=pk)
       
        consulta = models.ModeloPiezas.objects.filter(modelo__numero=1).values(
            'pieza__numero','pieza__nombre', 'totalpiezas'
        )
        
        print('consulta: ', consulta )
       
        context = {
           'Modelo': Modelos,
           'Modelos': consulta
        }
        return render(request, self.template_name, context)

#---------------------------------------------------------------
#           ESTADOS

class estados(StaffRequiredMixin, generic.CreateView):
   template_name = 'core/Estados/estados.html'
   model = models.Estados
   form_class = forms.CreateEstados
   
   success_url = reverse_lazy('core:estados')
   login_url = reverse_lazy('home:LogIn')
   
   def get(self, request):
       Estados = models.Estados.objects.all()
       context = {
           'Estados': Estados,
           'form': self.form_class
       }
       return render(request, self.template_name, context)

class editarEstados(StaffRequiredMixin,generic.UpdateView):
    
    template_name = 'core/Estados/editarEstados.html'
    model = models.Estados
    form_class = forms.UpdateEstados
    
    
    success_url = reverse_lazy("core:estados")
    login_url = reverse_lazy('home:LogIn')
    
class eliminarEstados(StaffRequiredMixin, generic.DeleteView):
    
    def get(self, request, pk):
        modelos = models.Estados.objects.get(numero=pk)
        modelos.delete()
        modelos = models.Estados.objects.all()
        messages.success(request, 'Se elimino el Estado')


        return redirect('/OPPENHEIMER/estados/')
#---------------------------------------------------------------
#           TAREAS

class tareas(StaffRequiredMixin, generic.CreateView):
   template_name = 'core/Tareas/tareas.html'
   model = models.Tareas
   form_class = forms.CreateTareas
   
   success_url = reverse_lazy('core:estados')
   login_url = reverse_lazy('home:LogIn')
   
   def get(self, request):
       Tareas= models.Tareas.objects.all()
       context = {
           'Tareas': Tareas,
           'form': self.form_class
       }
       return render(request, self.template_name, context)

class editarTareas(StaffRequiredMixin,generic.UpdateView):
    
    template_name = 'core/Tareas/editarTareas.html'
    model = models.Tareas
    form_class = forms.UpdateTareas 
    
    success_url = reverse_lazy("core:tareas")
    login_url = reverse_lazy('home:LogIn')
    
class eliminarTareas(StaffRequiredMixin, generic.DeleteView):
    
    def get(self, request, pk):
        tareas = models.Tareas.objects.get(numero=pk)
        tareas.delete()
        tareas = models.Tareas.objects.all()
        messages.success(request, 'Se elimino la Tarea')


        return redirect('/OPPENHEIMER/tareas/')

class asignarTareas(StaffRequiredMixin, generic.CreateView):
   template_name = 'core/Tareas/asignarTareas.html'
   model = models.Tareas
   form_class = forms.CreateTareas
   
   success_url = reverse_lazy('core:tareas')
   login_url = reverse_lazy('home:LogIn')
   
   def get(self, request):
       Tareas= models.Tareas.objects.all()
       context = {
           'Tareas': Tareas,
           'form': self.form_class
       }
       return render(request, self.template_name, context)

#---------------------------------------------------------------
#           ACTIVIDADES

class actividades(StaffRequiredMixin, generic.CreateView):
   template_name = 'core/Actividades/actividades.html'
   model = models.Actividades
   form_class = forms.CreateActividades
   
   success_url = reverse_lazy('core:actividades')
   login_url = reverse_lazy('home:LogIn')
   
   def get(self, request):
       Actividades = models.Actividades.objects.all()
       context = {
           'Actividades': Actividades,
           'form': self.form_class
       }
       return render(request, self.template_name, context)

class editarActividades(StaffRequiredMixin,generic.UpdateView):
    
    template_name = 'core/Actividades/editarActividades.html'
    model = models.Actividades
    form_class = forms.UpdateActividades
    
    
    success_url = reverse_lazy("core:actividades")
    login_url = reverse_lazy('home:LogIn')   

class eliminarActividades(StaffRequiredMixin, generic.DeleteView):
    
    def get(self, request, pk):
        actividades = models.Actividades.objects.get(numero=pk)
        actividades.delete()
        actividades = models.Actividades.objects.all()
        messages.success(request, 'Se elimino la Actividad')


        return redirect('/OPPENHEIMER/actividades/')

#---------------------------------------------------------------
#           ERRORES

class errores(StaffRequiredMixin, generic.CreateView):
   template_name = 'core/Errores/errores.html'
   model = models.Errores
   form_class = forms.CreateErrores
   
   success_url = reverse_lazy('core:errores')
   login_url = reverse_lazy('home:LogIn')
   
   def get(self, request):
       Errores = models.Errores.objects.all()
       context = {
           'Errores': Errores,
           'form': self.form_class
       }
       return render(request, self.template_name, context)

class editarErrores(StaffRequiredMixin,generic.UpdateView):
    
    template_name = 'core/Errores/editarErrores.html'
    model = models.Errores
    form_class = forms.UpdateErrores
    
    
    success_url = reverse_lazy("core:errores")
    login_url = reverse_lazy('home:LogIn')
    
class eliminarErrores(StaffRequiredMixin, generic.DeleteView):
    
    def get(self, request, pk):
        errores = models.Errores.objects.get(numero=pk)
        errores.delete()
        errores = models.Errores.objects.all()
        messages.success(request, 'Se elimino el Error registrado')


        return redirect('/OPPENHEIMER/errores/')
#---------------------------------------------------------------
#           SOLUCIONES

class soluciones(StaffRequiredMixin, generic.CreateView):
   template_name = 'core/Soluciones/soluciones.html'
   model = models.Soluciones
   form_class = forms.CreateSoluciones
   
   success_url = reverse_lazy('core:soluciones')
   login_url = reverse_lazy('home:LogIn')
   
   def get(self, request):
       Soluciones = models.Soluciones.objects.all()
       context = {
           'Soluciones': Soluciones,
           'form': self.form_class
       }
       return render(request, self.template_name, context)

class editarSoluciones(StaffRequiredMixin,generic.UpdateView):
    
    template_name = 'core/Soluciones/editarSoluciones.html'
    model = models.Soluciones
    form_class = forms.UpdateSoluciones
    
    
    success_url = reverse_lazy("core:soluciones")
    login_url = reverse_lazy('home:LogIn')
    
class eliminarSoluciones(LoginRequiredMixin, generic.DeleteView):
    
    def get(self, request, pk):
        soluciones = models.Soluciones.objects.get(numero=pk)
        soluciones.delete()
        soluciones = models.Soluciones.objects.all()
        messages.success(request, 'Se elimino la Solucion registrada')


        return redirect('/OPPENHEIMER/soluciones/')

#---------------------------------------------------------------
#            METAS

class metas(LoginRequiredMixin, generic.CreateView):
   template_name = 'core/Metas/metas.html'
   model = models.Metas
   form_class = forms.CreateMetas
   
   success_url = reverse_lazy('core:metas')
   login_url = reverse_lazy('home:LogIn')
   
   def get(self, request):
       Metas = models.Metas.objects.all()
       context = {
           'Metas': Metas,
           'form': self.form_class
       }
       return render(request, self.template_name, context)

class editarMetas(LoginRequiredMixin,generic.UpdateView):
    
    template_name = 'core/Metas/editarMetas.html'
    model = models.Metas
    form_class = forms.UpdateMetas
    
    
    success_url = reverse_lazy("core:metas")
    login_url = reverse_lazy('home:LogIn')

class eliminarMetas(LoginRequiredMixin, generic.DeleteView):
    
    def get(self, request, pk):
        metas = models.Metas.objects.get(numero=pk)
        metas.delete()
        metas = models.Metas.objects.all()
        messages.success(request, 'Se elimino la Meta')


        return redirect('/OPPENHEIMER/metas/')

#--------------------------------------------------------------
#           BITACORAS

class bitacoras(LoginRequiredMixin, generic.CreateView):
    template_name = 'core/Bitacoras/bitacoraSinIsaac.html'
    model = models.Bitacoras
    form_class_Bitacoras = forms.CreateBitacora
    form_class_BitAct = forms.CreateBitAct
    form_class_BitTareas = forms.CreateBitTarea
    form_class_Error = forms.CreateError
    form_class_Solucion = forms.CreateSolucion
   
    success_url = reverse_lazy('core:bitacoras')
    login_url = reverse_lazy('home:LogIn')
   
    def get(self, request):
        user = request.user.id

        try:
            Empleado = models.Empleados.objects.get(usuario=user)
            User = request.user
        except models.Empleados.DoesNotExist:
            Empleado = None
            User = None
        context = {
           'Empleado': Empleado,
           'form_Bitacoras':self.form_class_Bitacoras,
           'form_BitAct': self.form_class_BitAct,
           'form_BitTareas': self.form_class_BitTareas
           
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form_Bitacoras = self.form_class_Bitacoras(request.POST)
        form_BitAct = self.form_class_BitAct(request.POST)
        form_BitTareas = self.form_class_BitTareas(request.POST)
        form_Error = self.form_class_Error(request.POST)
        form_Solucion = self.form_class_Solucion(request.Post)
        

        if form_Bitacoras.is_valid() and form_BitAct.is_valid() and form_BitTareas.is_valid() and form_Error.is_valid() and form_Solucion.is_valid():
            # Guardar datos de empleado
            Bitacora = form_Bitacoras.save()
            BitAct = form_BitAct.save()
            BitTarea = form_BitTareas.save()
            
            
            BitAct.bitacora = Bitacora
            BitAct.save()
            
            BitTarea.bitacora = Bitacora
            BitTarea.save()
            

            messages.success(request, 'Registro exitoso!')
            return redirect('/OPPENHEIMER/empleados/')

        # Si alguno de los formularios no es válido
        messages.error(request, 'Hubo un error en el registro. Verifica los datos.')

class bitacoraErrorSolucion(LoginRequiredMixin, generic.CreateView):
    template_name = 'core/Bitacoras/bitacoraErrorSolucion.html'
    model = models.Bitacoras
   
    success_url = reverse_lazy('core:bitacoras')
    login_url = reverse_lazy('home:LogIn')
   
    def get(self, request):
        
        consulta = models.Empleados.objects.values(
            'numero',
            'bitacoras__numero',
            'bitacoras__titulo',
            'bitacoras__fecha',
            'bitacoras__metas__meta',
            'bitacoras__metas__fechainicio',
            'bitacoras__metas__fechafinal',
            'bitacoras__errores__numero',  
            'bitacoras__errores__descripcion',  
            'bitacoras__errores__soluciones__numero',  
            'bitacoras__errores__soluciones__descripcion'
        )
        
        context = {
            'BitacorasErroresSoluciones': consulta
        }
        return render(request, self.template_name, context)

class bitacoraTareaActividad(LoginRequiredMixin, generic.CreateView):

    template_name = 'core/Bitacoras/bitacoraTareaActividad.html'
    model = models.Bitacoras
   
    success_url = reverse_lazy('core:bitacoras')
    login_url = reverse_lazy('home:LogIn')
   
    def get(self, request):
        
        consulta = models.Empleados.objects.values(
            'numero',
            'bitacoras__numero',
            'bitacoras__titulo',
            'bitacoras__fecha',
            'bitacoras__metas__meta',
            'bitacoras__metas__fechainicio',
            'bitacoras__metas__fechafinal',
            'bitacoras__bittarea__tarea__numero',
            'bitacoras__bittarea__tarea__orden',
            'bitacoras__bittarea__fechainicio',
            'bitacoras__bittarea__fechafinal',
        )

        context = {
            'BitacorasActividades': consulta
        }
        return render(request, self.template_name, context)

class detailBitacoras(LoginRequiredMixin, generic.CreateView):

    template_name = 'core/Bitacoras/detailBitacoras.html'
    model = models.Bitacoras
   
    success_url = reverse_lazy('core:bitacoras')
    login_url = reverse_lazy('home:LogIn')
   
    def get(self, request, pk):
        
        consulta1 = models.Empleados.objects.filter(numero=pk).values(
            'nombrepila',
            'numero',
            'bitacoras__numero',
            'bitacoras__titulo',
            'bitacoras__fecha',
            'bitacoras__metas__meta',
            'bitacoras__metas__fechainicio',
            'bitacoras__metas__fechafinal',
            'bitacoras__bittarea__tarea__numero',
            'bitacoras__bittarea__tarea__orden',
            'bitacoras__bittarea__fechainicio',
            'bitacoras__bittarea__fechafinal',            
        )

        consulta2 = models.Empleados.objects.filter(numero=pk).values(
            'nombrepila',
            'numero',
            'bitacoras__numero',
            'bitacoras__titulo',
            'bitacoras__fecha',
            'bitacoras__metas__meta',
            'bitacoras__metas__fechainicio',
            'bitacoras__metas__fechafinal',
            'bitacoras__errores__numero',  
            'bitacoras__errores__descripcion',  
            'bitacoras__errores__soluciones__numero',  
            'bitacoras__errores__soluciones__descripcion'
        )
        
        empleado = models.Empleados.objects.get(numero=pk)
        context = {
            'Empleado': empleado,
            'BitacorasActividades': consulta1,
            'BitacorasErroresSoluciones': consulta2
        }
       
        return render(request, self.template_name, context)
    
class bitacoraTerminada(LoginRequiredMixin, generic.View):
    template_name = 'core/Bitacoras/bitacoraTerminada.html'
    model = models.Bitacoras
    success_url = reverse_lazy('core:bitacoras')
    login_url = reverse_lazy('home:LogIn')
   
    def get(self, request, pk):
        model = models.Bitacoras.objects.get(numero=pk)
        user = request.user.id

        consulta1 = models.Empleados.objects.filter(bitacoras__numero = pk ).values(
            'nombrepila',
            'primerapellido',
            'segundoapellido',
            'dircalle',
            'dirnumero',
            'dircolonia',
            'numtel',
            'horario',
            'jefearea__nombrepila',
            'jefearea__primerapellido',
            'areatrabajo__nombre',
            'puesto__nombre',
            
            
            'bitacoras__numero',
            'bitacoras__titulo',
            'bitacoras__fecha',
            'bitacoras__metas__meta',
            'bitacoras__metas__fechainicio',
            'bitacoras__metas__fechafinal',
        )
        
        consulta2 = models.Empleados.objects.filter(bitacoras__numero = pk ).values(                
            'bitacoras__errores__numero',  
            'bitacoras__errores__descripcion',  
            'bitacoras__errores__soluciones__numero',  
            'bitacoras__errores__soluciones__descripcion'
        )
        
        consulta3 = models.Empleados.objects.filter(bitacoras__numero = pk ).values(                
            'bitacoras__bittarea__tarea__numero',
            'bitacoras__bittarea__tarea__orden',
            'bitacoras__bittarea__fechainicio',
            'bitacoras__bittarea__fechafinal',
            
        )
        
        consulta4 = models.Empleados.objects.filter(bitacoras__numero = pk ).values(                
                       
            'bitacoras__bitact__actividad__numero',
            'bitacoras__bitact__actividad__descripcion',
            'bitacoras__bitact__tiempo',
        )
        
            

            
        context = {
            'Bitacoras': consulta1,
            'ErroresSoluciones':consulta2,
            'Tareas': consulta3,
            'Actividades': consulta4
        }
        return render(request, self.template_name, context)
    