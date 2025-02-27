from django.urls import path
from . import views
app_name = 'core'


urlpatterns = [

#Administración    
    path('', views.paginaPrincipal.as_view(), name='pagina_principal'),
    path('usuario/', views.user.as_view(), name='user'),
    path('verificar_contrasena/<str:password>/', views.verificar_contrasena, name='verificar_contrasena'),

#Solo para empleado    
    path('empleados/',views.empleados.as_view(), name='empleados'),
    path('registro/', views.registro.as_view(), name='registro'),
    path('detailEmpleado/<int:pk>/', views.DetailEmpleado.as_view(), name='detailEmpleados'),
    path("eliminarEmpleado/<int:pk>/", views.eliminarEmpleados.as_view(), name='deleteEmpleados'),
    path('cantidadEmpleados/<int:pk>/', views.cantidadEmpleados.as_view(), name="cantidadEmpleados"),
    
#Solo para piezas
    path('piezas/', views.piezas.as_view(), name='piezas'),
    path('editarPiezas/<int:pk>/', views.editarPiezas.as_view(), name='editarPiezas'),
    path("eliminarPiezas/<int:pk>/", views.eliminarPiezas.as_view(), name='deletePiezas'),  

#Solo Para Materiales
    path("materiales/", views.materiales.as_view(), name="materiales"),
    path('editarMaterial/<int:pk>/', views.editarMaterial.as_view(), name='editarMaterial'),
    path("eliminarMaterial/<int:pk>/", views.eliminarMaterial.as_view(), name='deleteMaterial'),

#Solo Para Puestos De Trabajo
    path("puestos/", views.puesto.as_view(), name="puestos"),
    path('editarPuesto/<int:pk>/', views.editarPuesto.as_view(), name='editarPuesto'),
    path("eliminarPuesto/<int:pk>/", views.eliminarPuesto.as_view(), name='deletePuesto'),

#Solo Para Areas De Trabajo
    path("areas/", views.areas.as_view(), name="areas"),
    path('editarArea/<int:pk>/', views.editarArea.as_view(), name='editarArea'),
    path("eliminarArea/<int:pk>/", views.eliminarArea.as_view(), name='deleteArea'),
    path("areasTrabajo/", views.areasTrabajo.as_view(), name="areasTrabajo"),
    path("cantidadModelos/<int:pk>/", views.cantidadModelos.as_view(), name="cantidadModelos"),

#Solo Para Modelos
    path("modelos/", views.modelos.as_view(), name="modelos"),
    path('editarModelos/<int:pk>/', views.editarModelos.as_view(), name='editarModelos'),
    path("eliminarModelos/<int:pk>/", views.eliminarModelos.as_view(), name='deleteModelos'),
    path("detailModelos/<int:pk>/", views.detailModelos.as_view(), name="detailModelos"),


#Solo Para Estados
    path("estados/", views.estados.as_view(), name="estados"),
    path('editarEstados/<int:pk>/', views.editarEstados.as_view(), name='editarEstados'),
    path("eliminarEstados/<int:pk>/", views.eliminarEstados.as_view(), name='deleteEstados'),

#Solo Para Tareas
    path("tareas/", views.tareas.as_view(), name="tareas"),
    path('editarTareas/<int:pk>/', views.editarTareas.as_view(), name='editarTareas'),
    path("eliminarTareas/<int:pk>/", views.eliminarTareas.as_view(), name='deleteTareas'),
    path("asignarTareas/", views.asignarTareas.as_view(), name="asignarTareas"),

#Solo Para Actividades
    path("actividades/", views.actividades.as_view(), name="actividades"),
    path('editarActividades/<int:pk>/', views.editarActividades.as_view(), name='editarActividades'),
    path("eliminarActividades/<int:pk>/", views.eliminarActividades.as_view(), name='deleteActividades'),

#Solo Para Errores
    path("errores/", views.errores.as_view(), name="errores"),
    path('editarErrores/<int:pk>/', views.editarErrores.as_view(), name='editarErrores'),
    path("eliminarErrores/<int:pk>/", views.eliminarErrores.as_view(), name='deleteErrores'),

#Solo Para Soluciones
    path("soluciones/", views.soluciones.as_view(), name="soluciones"),
    path('editarSoluciones/<int:pk>/', views.editarSoluciones.as_view(), name='editarSoluciones'),
    path("eliminarSoluciones/<int:pk>/", views.eliminarSoluciones.as_view(), name='deleteSoluciones'),

#Solo Para Metas
    path("metas/", views.metas.as_view(), name="metas"),
    path('editarMetas/<int:pk>/', views.editarMetas.as_view(), name='editarMetas'),
    path("eliminarMetas/<int:pk>/", views.eliminarMetas.as_view(), name='deleteMetas'),

#Solo Bitacoras
    path("bitacoras/", views.bitacoras.as_view(), name="bitacoras"),
    path("bitacoraErrorSolucion/", views.bitacoraErrorSolucion.as_view(), name="bitacoraErrorSolucion"),
    path("bitacoraTareaActividad/", views.bitacoraTareaActividad.as_view(), name="bitacoraTareaActividad"),
    path("detailBitacoras/<int:pk>/", views.detailBitacoras.as_view(), name="detailBitacoras"),
    path("bitacoraTerminada/<int:pk>/", views.bitacoraTerminada.as_view(), name="bitacoraTerminada")


]
