from ..cuenta import Cuenta, LIMITE_MAXAXIMO_DE_TRANSFERENCIA
from ..direccion import Direccion
from ..tarjeta import EmisorTarjeta, Tarjeta, TipoTarjeta
from ..chequera import Chequera

CLASSIC = "CLASSIC"
GOLD = "GOLD"
BLACK = "BLACK"


class Cliente:
    cuentas: list[Cuenta]
    
    tarjetas_de_credito_permitidas: int
    tarjetas: list[Tarjeta]

    chequeras_permitidas: int
    chequeras : list[Chequera]

    direccion: Direccion

    nombre: str
    apellido: str
    numero: str
    dni: str

    def __init__(
        self,
        cuentas: list[Cuenta],
        tarjetas_de_credito_permitidas: int,
        chequeras_permitidas: int,
        direccion: Direccion,
        nombre: str,
        apellido: str,
        numero: str,
        dni: str,
    ) -> None:
        self.cuentas = cuentas
        self.tarjetas = []
        self.tarjetas_de_credito_permitidas = tarjetas_de_credito_permitidas
        self.chequeras_permitidas = chequeras_permitidas
        self.chequeras = []        
        self.direccion = direccion
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.dni = dni

    def puede_crear_chequera(self) -> bool:
        return False

    def puede_crear_tarjeta_credito(self) -> bool:
        return False

    def puede_comprar_dolar(self) -> bool:
        return False


class ClienteClassic(Cliente):
    def __init__(
        self,
        direccion: Direccion,
        nombre: str,
        apellido: str,
        numero: str,
        dni: str,
    ) -> None:
        cuentas: list[Cuenta] = []

        caja_de_ahorro_en_pesos: Cuenta = Cuenta(
            limite_extraccion_diario=10000,
            limite_trasnferencia_recibida=150000,
            monto=0,
            costo_trasnferencia=0.01,
            saldo_descubierto_disponible=0,
        )

        cuentas.append(caja_de_ahorro_en_pesos)

        super().__init__(
            cuentas=cuentas,
            tarjetas_de_credito_permitidas=0,
            chequeras_permitidas=0,
            direccion=direccion,
            nombre=nombre,
            apellido=apellido,
            numero=numero,
            dni=dni,
        )

    def puede_crear_chequera(self) -> bool:
        return False

    def puede_crear_tarjeta_credito(self) -> bool:
        return False

    def puede_comprar_dolar(self) -> bool:
        return False


class ClienteGold(Cliente):
    def __init__(
        self,
        direccion: Direccion,
        nombre: str,
        apellido: str,
        numero: str,
        dni: str,
    ) -> None:
        cuentas: list[Cuenta] = []

        cuenta_corriente: Cuenta = Cuenta(
            limite_extraccion_diario=10000,
            limite_trasnferencia_recibida=500000,
            monto=0,
            costo_trasnferencia=0.05,
            saldo_descubierto_disponible=10000,
        )

        caja_de_ahorro_en_dolares: Cuenta = Cuenta(0, 0, 0, 0, 0,)

        cuentas.append(cuenta_corriente)

        cuentas.append(caja_de_ahorro_en_dolares)


        super().__init__(
            cuentas=cuentas,
            tarjetas_de_credito_permitidas=1,
            chequeras_permitidas=1,
            direccion=direccion,
            nombre=nombre,
            apellido=apellido,
            numero=numero,
            dni=dni,
        )

    def puede_crear_chequera(self) -> bool:
        return False

    def puede_crear_tarjeta_credito(self) -> bool:
        return False

    def puede_comprar_dolar(self) -> bool:
        return False


class ClienteBlack(Cliente):
    def __init__(
        self,
        direccion: Direccion,
        nombre: str,
        apellido: str,
        numero: str,
        dni: str,
    ) -> None:
        cuentas: list[Cuenta] = []

        caja_de_ahorro_en_pesos: Cuenta = Cuenta(
            limite_extraccion_diario=100000,
            limite_trasnferencia_recibida=LIMITE_MAXAXIMO_DE_TRANSFERENCIA,
            monto=0,
            costo_trasnferencia=0,
            saldo_descubierto_disponible=10000,
        )

        cuenta_corriente: Cuenta = Cuenta(
            limite_extraccion_diario=100000,
            limite_trasnferencia_recibida=LIMITE_MAXAXIMO_DE_TRANSFERENCIA,
            monto=0,
            costo_trasnferencia=0,
            saldo_descubierto_disponible=10000,
        )

        caja_de_ahorro_en_dolares: Cuenta = Cuenta(0, 0, 0, 0, 0,)

        cuentas.append(caja_de_ahorro_en_pesos)

        cuentas.append(cuenta_corriente)

        cuentas.append(caja_de_ahorro_en_dolares)

        super().__init__(
            cuentas=cuentas,
            tarjetas_de_credito_permitidas=5,
            chequeras_permitidas=2,
            direccion=direccion,
            nombre=nombre,
            apellido=apellido,
            numero=numero,
            dni=dni,
        )

    def puede_crear_chequera(self) -> bool:
        return False

    def puede_crear_tarjeta_credito(self) -> bool:
        return False

    def puede_comprar_dolar(self) -> bool:
        return False
