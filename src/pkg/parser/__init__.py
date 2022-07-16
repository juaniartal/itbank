from typing import Tuple
#from .evento import Evento
from ..cliente import *
import json


class Parser:
    def execute(self, file_name: str):
        transacciones = []
        with open(file_name) as jsonFile:
            eventos = json.load(jsonFile)
            cliente = self.parsearCliente(eventos)
            for t in eventos["transacciones"]:
                # utilizamos una forma simple para crear el objeto
                #transacciones.append(Evento(**t))
                continue
            return (cliente, transacciones)


    def parsearCliente(self, datos) -> Cliente:
        tipo = datos["tipo"]

        if (tipo == CLASSIC):
            cliente = ClienteClassic(
                direccion=Direccion("", "", "", "", "",),
                nombre=datos["nombre"],
                apellido=datos["apellido"],
                numero=datos["numero"],
                dni=datos["DNI"],
            )
        elif (tipo == GOLD):
            cliente = ClienteGold(
                direccion=Direccion("", "", "", "", "",),
                nombre=datos["nombre"],
                apellido=datos["apellido"],
                numero=datos["numero"],
                dni=datos["DNI"],                
            )
        elif (tipo == BLACK):
            cliente = ClienteBlack(
                direccion=Direccion("", "", "", "", "",),
                nombre=datos["nombre"],
                apellido=datos["apellido"],
                numero=datos["numero"],
                dni=datos["DNI"],
            )
        else:
            raise Exception("Tipo de cliente no existe")

        return cliente