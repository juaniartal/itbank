from datetime import date
from enum import Enum
import uuid
import random


class TipoTarjeta(Enum):
    CREDITO: int = 0
    DEBITO: int = 1
    ...


class EmisorTarjeta(Enum):
    MASTERCARD: int = 0
    VISA: int = 1
    ...


class Tarjeta:
    numero: str
    nombre: str

    tipo: TipoTarjeta

    emisor: EmisorTarjeta

    fecha_emision: str
    fecha_expiracion: str

    cvv: int

    def __init__(
        self,
        nombre: str,
        tipo: TipoTarjeta,
        emisor: EmisorTarjeta,
    ) -> None:
        today = date.today()

        self.numero = uuid.uuid1()
        self.nombre = nombre
        self.tipo = tipo
        self.emisor = emisor
        self.fecha_emision = today
        self.fecha_expiracion = today.replace(year=today.year + 5)
        self.cvv = random.randrange(100, 1000)
