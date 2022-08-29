from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView 
from rest_framework import permissions
from rest_framework import status
from base.models import *
from .serializers import *

class Tarjetas(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, idCliente):
        tarjeta = Tarjeta.objects.filter(customer_id=idCliente)
        serializer = TarjetaSerializer(tarjeta, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)    