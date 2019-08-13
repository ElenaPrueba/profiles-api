from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers

#Lista de respuestas HTTP
from rest_framework import status


from rest_framework import viewsets


from . import models


# Create your views here.
class HelloApiView(APIView):
    """Test API View"""


    serializers_class = serializers.HelloSerializer

    def get(self, request,format=None):
        """Devuelve una lista de las caracteristicas de APIView"""
        an_apiview = [
                    'Usa los metodos HTTP como una funcion (get, post, put, patch, delete)',
                    'Es parecida a una vista tradicional de Django',
                    'Da más control sobre la lógica de tu aplicacion',
                    'Está mapeada con URLs'
                    ]
        return Response({'mensaje': 'Hola', 'an_apiview':an_apiview})

    def post(self, request):
        """Crea un saludo con nuestro nombre"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles Actualizando un objeto."""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request, solo actualiza los campos proporcionados en la solicitud."""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None): #pk = primary key
        """Borra un objeto."""

        return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class= serializers.HelloSerializer

    def list(self, request):
        """Devuelve un mensaje de hola."""

        a_viewset = [
            'Usa acciones (list, create, retrieve, update, partial_update)',
            'Automaticamente mapea URLS usando Routers',
            'Proporciona mas funcionalidad con menos codigo'
        ]

        return Response({'message': 'Hola!', 'a_viewset': a_viewset})

    def create(self, request):
        """Crea un nuevo mensaje de saludo."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Se encarga de obtener un objeto por su ID."""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Maneja la actualizacion de un objeto."""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Maneja la actualización de parte de un objeto"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """ManejaManejar la eliminación de un objeto la eliminación de un objeto"""

        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Encargado de la creación y la actualización de los perfiles de usuario"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
