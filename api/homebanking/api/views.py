from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework import status
from base.models import *
from .serializers import *

class ClientesById(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, cliente_id):
        cliente = Cliente.objects.filter(id=cliente_id)
        serializer = ClienteSerializer(cliente, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)    

class CuentasById(APIView):
    def get(self, request, cliente_id):
        cuenta = Cuenta.objects.filter(customer_id=cliente_id).order_by('id')
        serializer = CuentaSerializer(cuenta, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)    

class Prestamos(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request): 
        serializer = PrestamoSerializer(data=request.data, context={'request': request}) 
        if serializer.is_valid(): 
            status = status.HTTP_201_CREATED            
            data = serializer.data
            serializer.save() 
            return Response(data, status=status)             
        else:
            status = status.HTTP_400_BAD_REQUEST
            data = serializer.errors
            return Response(data, status=status) 

class PrestamosById(APIView):   
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated] 

    def get(self, request, cliente_id):
        prestamo = Prestamo.objects.filter(customer_id=cliente_id).order_by('id')
        serializer = PrestamoSerializer(prestamo, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)                    
        
    def delete(self, request, cliente_id): 
        prestamo = Prestamo.objects.filter(customer_id=cliente_id).first() 
        serializer = PrestamoSerializer(prestamo, context={'request': request}) 
        prestamo.delete() 
        return Response(serializer.data, status=status.HTTP_200_OK) 

class PrestamosSucursalById(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]    

    def get(self, request, branch_id):
        prestamos = []
        clientes = Cliente.objects.filter(branch_id = branch_id).order_by('id')
        for cliente in clientes:
            prestamos += Prestamo.objects.filter(customer_id = cliente)
        serializer = PrestamoSerializer(prestamos, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)                    

class DireccionesById(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]   

    def patch(self, request, address_id):
        address = Address.objects.filter(id = address_id).first()
        serializer = DireccionSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

class TarjetasById(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]    

    def get(self, request, cliente_id):
        tarjeta = Tarjeta.objects.filter(customer_id=cliente_id).order_by('id')
        serializer = TarjetaSerializer(tarjeta, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)    

class Sucursales(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]    

    def get(self, request):
        sucursales = Branch.objects.all().order_by('id')
        serializer = SucursalSerializer(sucursales, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)                    
