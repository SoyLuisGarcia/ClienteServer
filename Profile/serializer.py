from rest_framework import routers, serializers, viewsets

from rest_framework import routers, serializers, viewsets

#---------------- AGREGANDO MODELOS ---------------------
from Profile.models import Example3
from Profile.models import ModelsEstadoCivil
from Profile.models import ModelsCiudad
from Profile.models import ModelsOcupacion
from Profile.models import ModelsEstado
from Profile.models import ModelsGenero


class Example3Serializers(serializers.ModelSerializer):
    class Meta: 
        model = Example3
        fields = ('__all__')

class EstadoCivilSerializers(serializers.ModelSerializer):
    class Meta: 
        model = ModelsEstadoCivil
        fields = ('__all__')

class CiudadSerializers(serializers.ModelSerializer):
    class Meta: 
        model = ModelsCiudad
        fields = ('__all__')

class OcupacionSerializers(serializers.ModelSerializer):
    class Meta: 
        model = ModelsOcupacion
        fields = ('__all__')

class EstadoSerializers(serializers.ModelSerializer):
    class Meta: 
        model = ModelsEstado
        fields = ('__all__')

class GeneroSerializers(serializers.ModelSerializer):
    class Meta: 
        model = ModelsGenero
        fields = ('__all__')