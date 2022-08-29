from rest_framework import serializers
from base.models import *


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        read_only_fields = ("id",)


class ClienteTipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente.CustomerType
        fields = '__all__'


class CuentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cuenta
        fields = '__all__'


class TipoCuentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cuenta.AccountType
        fields = '__all__'


class PrestamoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'


class DireccionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class SucursalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class PrestamoTipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prestamo.LoanType
        fields = '__all__'


class TarjetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarjeta
        fields = '__all__'


class MarcaTarjetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarjeta.CardBrand
        fields = '__all__'


class TipoTarjetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarjeta.CardType
        fields = '__all__'        