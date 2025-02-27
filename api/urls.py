from django.db import router
from django.urls import path, include
from rest_framework import routers
from api import views


routers = routers.DefaultRouter()
routers.register(r'piezas', views.PiezasViewSet)
routers.register(r'bitacoras', views.BitacorasViewSet)
routers.register(r'empleados', views.EmpleadosViewSet)
routers.register(r'areas_de_trabajo', views.AreasdetrabajoViewSet)
routers.register(r'materiales', views.MaterialesViewSet)
routers.register(r'AtModelos', views.AtModelosViewSet)
routers.register(r'AtPiezas', views.AtPiezasViewSet)

urlpatterns = [
    path('',include(routers.urls))
]