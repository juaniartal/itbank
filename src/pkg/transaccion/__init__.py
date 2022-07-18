from ..cliente import Cliente


class Transaccion:
    estado: str
    tipo: str
    cuentaNumero: int
    cupoDiarioRestante: float
    monto: float
    fecha: str
    numero: int
    saldo_en_cuenta: float
    totalTarjetasDeCreditoActualmente: int
    totalChequerasActualmente: int

    def __init__(self, estado, tipo, cuentaNumero, cupoDiarioRestante, monto, fecha, numero, saldoEnCuenta,
                 totalTarjetasDeCreditoActualmente, totalChequerasActualmente):
        self.estado = estado
        self.tipo = tipo
        self.cuentaNumero = cuentaNumero
        self.cupoDiarioRestante = cupoDiarioRestante
        self.monto = monto
        self.fecha = fecha
        self.numero = numero
        self.saldo_en_cuenta = saldoEnCuenta
        self.totalTarjetasDeCreditoActualmente = totalTarjetasDeCreditoActualmente
        self.totalChequerasActualmente = totalChequerasActualmente

    def justificar(self, cliente: Cliente) -> str:

        if self.estado == "ACEPTADA":
            return "-"

        match self.tipo:
            case "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
                if self.monto > self.saldo_en_cuenta:
                    return "Saldo insuficiente"
                else:
                    return "Cupo diario alcanzado"
            case "ALTA_TARJETA_CREDITO":
                return "Máximo nro de tarjetas de crédito en uso"
            case "ALTA_CHEQUERA":
                return "Máximo nro de chequeras en uso"
            case "COMPRA_DOLAR":
                if cliente.puede_comprar_dolar():
                    return "Saldo insuficiente"
                else:
                    return "No posee cuenta dólares"
            case _:
                return "Saldo insuficiente"
