# importar cliente dependiendo donde este from cliente import Cliente
# importar algun tipo de evento / razon
class ClienteClassic (Cliente):
    def __init__(self, **kwargs) -> None:
        super(ClienteClassic, self).__init__(**kwargs)

        def get_razon_compra_cuotas_visa(self, evento: Evento):
            return "Este cliente no puede tener tarjetas de credito"
