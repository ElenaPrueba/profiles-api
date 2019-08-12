from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""

    def get(self, request,format=None):
        """Devuelve una lista de las caracteristicas de APIView"""
        an_apiview = [
                    'Usa los metodos HTTP como una funcion (get, post, put, patch, delete)',
                    'Es parecida a una vista tradicional de Django',
                    'Da más control sobre la lógica de tu aplicacion',
                    'Está mapeada con URLs'
                    ]
        return Response({'mensaje': 'Hola', 'an_apiview':an_apiview})
