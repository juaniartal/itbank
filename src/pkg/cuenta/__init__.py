LIMITE_MAXAXIMO_DE_TRANSFERENCIA = 9999999999

class Cuenta:
    limite_extraccion_diario : float = 0
    limite_trasnferencia_recibida : float  = 0
    monto : float  = 0
    costo_trasnferencia : float = 0
    saldo_descubierto_disponible : float = 0

    def __init__(self, 
    limite_extraccion_diario : float,
    limite_trasnferencia_recibida : float,
    monto : float,
    costo_trasnferencia : float,
    saldo_descubierto_disponible : float,
    ) -> None:
        self.limite_extraccion_diario = limite_extraccion_diario
        self.limite_trasnferencia_recibida = limite_trasnferencia_recibida
        self.monto = monto
        self.costo_trasnferencia = costo_trasnferencia
        self.saldo_descubierto_disponible = saldo_descubierto_disponible
