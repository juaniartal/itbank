# no importamos
class Cuenta:
    def __init__(self, **kwargs) -> None:
        self.limite_extraccion_diario = kwargs.get(
            'limite_extraccion_diario', 0)
        self.limite_trasnferencia_recibida = kwargs.get(
            'limite_trasnferencia_recibida', 0)
        self.costo_trasnferencia = kwargs.get('costo_transferencia', 0.05)
        self.total_tarjetas_credito = kwargs.get('total_tarjetas_credito', 0)
        self.total_chequeras = kwargs.get('total chequeras', 0)
        self.saldo_descubierto_disponible = kwargs.get(
            'saldo_descubierto_disponible', 0)
