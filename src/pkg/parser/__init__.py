from ..cliente import *
from ..transaccion import Transaccion
import json


class Parser:
    target_json_file: str

    cliente: Cliente

    transacciones: list[Transaccion]

    def __init__(self, target_json_file: str) -> None:
        self.target_json_file = target_json_file
        self.transacciones = list()
        self.cliente = Cliente(
            [],
            0,
            0,
            Direccion(
                "",
                "",
                "",
                "",
                "",
            ),
            "",
            "",
            "",
            "",
        )

    def execute(self):
        with open(self.target_json_file) as jsonFile:
            try:
                data = json.load(jsonFile)
            except Exception as error:
                print(error)
                raise Exception("Failed to load " + self.target_json_file)

            try:
                self.__parsearCliente(data)
            except Exception as error:
                print(error)
                raise Exception("Failed to parse Cliente from " + self.target_json_file)

            try:
                self.__parsearTransacciones(data)
            except Exception as error:
                print(error)
                raise Exception(
                    "Failed to parse Transacciones from " + self.target_json_file
                )

    def __parsearTransacciones(self, data: str) -> None:
        for transaccion in data["transacciones"]:
            self.transacciones.append(
                Transaccion(
                    estado=transaccion["estado"],
                    tipo=transaccion["tipo"],
                    cuentaNumero=transaccion["cuentaNumero"],
                    cupoDiarioRestante=transaccion["cupoDiarioRestante"],
                    monto=transaccion["monto"],
                    fecha=transaccion["fecha"],
                    numero=transaccion["numero"],
                    saldoEnCuenta=transaccion["saldoEnCuenta"],
                    totalTarjetasDeCreditoActualmente=transaccion[
                        "totalTarjetasDeCreditoActualmente"
                    ],
                    totalChequerasActualmente=transaccion["totalChequerasActualmente"],
                )
            )

    def __parsearCliente(self, data) -> None:
        direccion: Direccion = Direccion(
            calle=data["direccion"]["calle"],
            numero=data["direccion"]["numero"],
            ciudad=data["direccion"]["ciudad"],
            provincia=data["direccion"]["provincia"],
            pais=data["direccion"]["pais"],
        )
   
        tipo: str = data["tipo"]

        if tipo == CLASSIC:
            self.cliente = ClienteClassic(
                direccion=direccion,
                nombre=data["nombre"],
                apellido=data["apellido"],
                numero=data["numero"],
                dni=data["dni"],
            )
        elif tipo == GOLD:
            self.cliente = ClienteGold(
                direccion=direccion,
                nombre=data["nombre"],
                apellido=data["apellido"],
                numero=data["numero"],
                dni=data["dni"],
            )
        elif tipo == BLACK:
            self.cliente = ClienteBlack(
                direccion=direccion,
                nombre=data["nombre"],
                apellido=data["apellido"],
                numero=data["numero"],
                dni=data["dni"],
            )
        else:
            raise Exception("Tipo de cliente no existe")
