

class Cliente(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        read_only_fields = ("customer_id",)


class Cuenta(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cuenta
        fields = '__all__'


class Prestamo(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'


class Tarjeta(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarjeta
        fields = '__all__'


class Direccion(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        read_only_fields = ("address_id",)


class Sucursal(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class ClienteTipo(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class PrestamoTipo(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'


class MarcaTarjeta(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarjeta
        fields = '__all__'


class TipoCuenta(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cuenta
        fields = '__all__'
