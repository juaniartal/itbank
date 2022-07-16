from ..cliente import Cliente
#from ..evento import Evento
import importlib


class BuscadorProblema:
    def __init__(self, cliente: Cliente) -> None:
        self.cliente = Cliente
        self.tipos = {
            "RETIRO_EFECTIVO_CAJERO_AUTOMATICO": {
                "modulo": "razon_retiro_efectivo",
                "clase": "RazonRetiroEfectivo"
            },
            "ALTA_TARJETA_CREDITO": {
                "modulo": "razon_alta_tarjeta_credito",
                "clase": "RazonAltaTarjetaCredito",
            },
            "ALTA_CHEQUERA": {
                "modulo": "razon_alta_chequera",
                "clase": "RazonAltaChequera"
            },
            "COMPRA_DOLAR": {
                "modulo": "razon_compra_dolar",
                "clase": "RazonCompraDolar"
            },
            "TRANSFERENCIA_ENVIADA": {
                "modulo": "razon_transferencia_enviada",
                "clase": "RazonTransferenciaEnviada"
            },
            "TRANSFERENCIA_RECIBIDA": {
                "modulo": "razon_transferencia_recibida",
                "clase": "RazonTransferenciaRecibida"
            }
        }

        """
        def getResultado(self, evento: Evento):
            explicacion = ""
            if evento.estado == Evento.RECHAZADA:
                module = importlib.import_module(
                    "." + self.tipos[evento.tipo]['modulo'], "clases.razon")
                razon = getattr(module, self.tipos[evento.tipo]['clase'])()
                explicacion = razon.resolver(self.cliente, evento)
            return {
                "razon": explicacion,
                "estado": evento.estado,
                "tipo": evento.tipo,
                "saldo": evento.saldoEnCuenta,
                "fecha": evento.fecha,
                "monto": evento.monto
            }
        """