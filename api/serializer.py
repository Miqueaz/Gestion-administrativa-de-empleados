from dataclasses import field
from rest_framework import serializers
from core.models import (
    AtModelos, AtPiezas, Actividades, Areasdetrabajo, BitAct, BitTarea,
    Bitacoras, Empleados, Errores, Estados, Materiales, Metas,
    ModeloPiezas, Modelos, Piezas, PiezasMaterial, Puestos,
    Soluciones, Tareas
)
from core.views import piezas

class ModelosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelos
        fields = '__all__'
        
class AreasdetrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areasdetrabajo
        fields = '__all__'
        
class AtModelosSerializer(serializers.ModelSerializer):
    modelo = ModelosSerializer()
    area = AreasdetrabajoSerializer()
    class Meta:
        model = AtModelos
        fields = [
            'area',
            'modelo',
            'cantidad',
        ]
        
class AtPiezasSerializer(serializers.ModelSerializer):
    pieza__numero = serializers.IntegerField()
    pieza__nombre = serializers.CharField()
    stock = serializers.IntegerField()
    class Meta:
        model = AtPiezas
        fields = [
            'pieza__numero',
            'pieza__nombre',
            'stock'
        ]
        
class ActividadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividades
        fields = '__all__'



class BitActSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitAct
        fields = '__all__'

class BitTareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitTarea
        fields = '__all__'
        
class BitacorasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bitacoras
        fields = '__all__'
        
class EmpleadosSerializer(serializers.ModelSerializer):
    areatrabajo__numero = serializers.IntegerField()
    areatrabajo__nombre = serializers.CharField()
    empleados = serializers.IntegerField()
    
    class Meta:
        model = Empleados
        fields = ['areatrabajo__numero', 'areatrabajo__nombre', 'empleados']

class ErroresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Errores
        fields = '__all__'

class EstadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estados
        fields = '__all__'

class MaterialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materiales
        fields = '__all__'

class MetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metas
        fields = '__all__'
        
class ModeloPiezasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloPiezas
        field = '__all__'
        


class PiezasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piezas
        fields = '__all__'

class PuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puestos
        fields = '__all__'

class SolucionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soluciones
        fields = '__all__'

class TareasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = '__all__'
        
class PiezasMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiezasMaterial
        fields = '__all__'
        