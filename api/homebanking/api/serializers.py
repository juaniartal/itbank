from rest_framework import serializers
from base.models import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        read_only_fields = ("id")


class ClienteTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente.CustomerType
        fields = '__all__'


class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = '__all__'


class TipoCuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta.AccountType
        fields = '__all__'


class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'


class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class PrestamoTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo.LoanType
        fields = '__all__'


class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = '__all__'


class MarcaTarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta.CardBrand
        fields = '__all__'


class TipoTarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta.CardType
        fields = '__all__'        


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'        

                