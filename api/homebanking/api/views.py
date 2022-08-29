from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView 
from rest_framework import permissions
from rest_framework import status
from base.models import *
from .serializers import *

class Tarjetas(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, cliente_id):
        tarjeta = Tarjeta.objects.filter(customer_id=cliente_id).order_by('id')
        serializer = TarjetaSerializer(tarjeta, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)    

class Clientes(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, cliente_id):
        cliente = Cliente.objects.filter(id=cliente_id)
        serializer = ClienteSerializer(cliente, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)    