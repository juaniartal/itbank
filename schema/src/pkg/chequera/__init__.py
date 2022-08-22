class Cheque:
    nombre: str
    monto: str
    ...

class Chequera:
    cheques = list[Cheque]
    ...