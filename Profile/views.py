from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework.views import APIView
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.schemas import AutoSchema


import coreapi
from rest_framework.schemas import AutoSchema


from Profile.models import Example3
from Profile.models import ModelsEstadoCivil
from Profile.models import ModelsCiudad
from Profile.models import ModelsOcupacion
from Profile.models import ModelsEstado
from Profile.models import ModelsGenero


from Profile.serializer import Example3Serializers
from Profile.serializer import  EstadoCivilSerializers
from Profile.serializer import CiudadSerializers
from Profile.serializer import OcupacionSerializers
from Profile.serializer import EstadoSerializers
from Profile.serializer import GeneroSerializers
import coreapi
from rest_framework.permissions import IsAuthenticated


class ProfileLisViewSchema(AutoSchema):
    def get_manual_fields(self,path,method):
        extra_fields = []
        if method.lower() in ('post','get'):
            extra_fields = [
                coreapi.Field('nombre')
            ]
        manual_fields =super().get_manual_fields(path,method)
        return manual_fields + extra_fields


class ExampleList3(APIView):
    
    permission_classes =[IsAuthenticated]
    esquema  =  ProfileLisViewSchema ()

    #METODO GET PARA SOLICITAR INFO
    def get (self , request , format = None):
        print("Metodo get filter")
        queryset = Example3.objects.filter(delete = False)
        #many true si se aplica retornos multiples objetos
        serializer = Example3Serializers(queryset, many= True)
        return Response(serializer.data)

    def post (self, request , format = None):
        serializer = Example3Serializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class EstadoCivil(APIView):

    permission_classes =[IsAuthenticated]
    esquema  =  ProfileLisViewSchema ()

    #METODO GET PARA SOLICITAR INFO
    def get (self , request , format = None):
        print("Metodo get filter")
        queryset = Example3.objects.filter(delete = False)
        #many true si se aplica retornos multiples objetos
        serializer = Example3Serializers(queryset, many= True)
        return Response(serializer.data)

    def post (self, request , format = None):
        serializer = Example3Serializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class Ciudad(APIView):

    permission_classes =[IsAuthenticated]
    esquema  =  ProfileLisViewSchema ()

    #METODO GET PARA SOLICITAR INFO
    def get (self , request , format = None):
        print("Metodo get filter")
        queryset = ModelsCiudad.objects.filter(delete = False)
        #many true si se aplica retornos multiples objetos
        serializer = CiudadSerializers(queryset, many= True)
        return Response(serializer.data)

    def post (self, request , format = None):
        serializer = CiudadSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class Ocupacion(APIView):

    permission_classes =[IsAuthenticated]
    esquema  =  ProfileLisViewSchema ()

    #METODO GET PARA SOLICITAR INFO
    def get (self , request , format = None):
        print("Metodo get filter")
        queryset = ModelsOcupacion.objects.filter(delete = False)
        #many true si se aplica retornos multiples objetos
        serializer = OcupacionSerializers(queryset, many= True)
        return Response(serializer.data)

    def post (self, request , format = None):
        serializer = OcupacionSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class Estado(APIView):
    permission_classes =[IsAuthenticated]
    esquema  =  ProfileLisViewSchema ()

    #METODO GET PARA SOLICITAR INFO
    def get (self , request , format = None):
        print("Metodo get filter")
        queryset = ModelsEstado.objects.filter(delete = False)
        #many true si se aplica retornos multiples objetos
        serializer = EstadoSerializers(queryset, many= True)
        return Response(serializer.data)

    def post (self, request , format = None):
        serializer = EstadoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class Genero(APIView):
    permission_classes =[IsAuthenticated]
    esquema  =  ProfileLisViewSchema ()

    #METODO GET PARA SOLICITAR INFO
    def get (self , request , format = None):
        print("Metodo get filter")
        queryset = ModelsGenero.objects.filter(delete = False)
        #many true si se aplica retornos multiples objetos
        serializer = GeneroSerializers(queryset, many= True)
        return Response(serializer.data)

    def post (self, request , format = None):
        serializer = GeneroSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

