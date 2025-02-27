from token import AT
from rest_framework import viewsets
from . import serializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, F, ExpressionWrapper, fields
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from core import models
from rest_framework.response import Response
from django.db.models import Count, Subquery, OuterRef


# Create your views here.

class PiezasViewSet(viewsets.ModelViewSet):
    queryset = models.Piezas.objects.all()
    serializer_class = serializer.PiezasSerializer

class BitacorasViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = models.Bitacoras.objects.all()
    serializer_class = serializer.BitacorasSerializer

class EmpleadosViewSets(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = models.Empleados.objects.all()
    serializer_class = serializer.EmpleadosSerializer

class AreasdetrabajoViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = models.Areasdetrabajo.objects.all()
    serializer_class = serializer.AreasdetrabajoSerializer
    
class MaterialesViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = models.Materiales.objects.all()
    serializer_class = serializer.MaterialesSerializer
    
class AtModelosViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = models.AtModelos.objects.all()
    serializer_class = serializer.AtModelosSerializer

class EmpleadosViewSet(viewsets.ModelViewSet):
    
    queryset = models.Empleados.objects.values(
        'areatrabajo__numero', 'areatrabajo__nombre'
    ).annotate(
        empleados=Count('areatrabajo')
    ).order_by(
        'areatrabajo__numero'
    )
    
    serializer_class = serializer.EmpleadosSerializer 

    
class AtPiezasViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = models.AtPiezas.objects.values(
        'pieza__numero','pieza__nombre', 
    ).annotate(
        stock=Sum('cantidadpieza')
    ).order_by(
        'pieza__nombre'
    )
    
    serializer_class = serializer.AtPiezasSerializer