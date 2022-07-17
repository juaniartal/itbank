
class Evento:
    estado: str
    tipo = str
    cuentaNumero: int
    cupoDiarioRestante: float
    monto: float
    fecha: str
    numero: int
    saldoEnCuenta: float
    totalTarjetasDeCreditoActualmente: int
    totalChequerasActualmente: int

    def __init__(self, estado, tipo, cuentaNumero, cupoDiarioRestante, monto, fecha, numero, saldoEnCuenta, totalTarjetasDeCreditoActualmente, totalChequerasActualmente):
        self.estado = estado
        self.tipo = tipo
        self.cuentaNumero = cuentaNumero
        self.cupoDiarioRestante = cupoDiarioRestante
        self.monto = monto
        self.fecha = fecha
        self.numero = numero
        self.saldoEnCuenta = saldoEnCuenta
        self.totalTarjetasDeCreditoActualmente = totalTarjetasDeCreditoActualmente
        self.totalChequerasActualmente = totalChequerasActualmente
