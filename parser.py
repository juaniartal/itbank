from multiprocessing import Event
from typing import Tuple
from .evento import Evento
from .cliente import *
import json


class Parser:
    def execute(self, file_name: str) -> Tuple[Cliente, 'list[Evento]']:
        transacciones = []
        with open(files_name) as jsonFile:
            eventos = json.load(jsonFile)
            cliente = self.parsearCliente(eventos)
            for t in eventos["transacciones"]:
                # utilizamos una forma simple para crear el objeto
                transacciones.append(Evento(**t))
            return (cliente, transacciones)


def parsearCliente(self, datos) -> Cliente:
    tipo = datos["tipo"]

    if (tipo == CLASSIC):
        cliente = ClienteClassic(**BuilderCliente.getDatosClientesClassic())
    elif (tipo == GOLD):
        cliente = ClienteGold(**BuildCliente.getDatosClientesGold())
    elif (tipo == BLACK):
        cliente = ClienteBlack(**BuilderCliente.getDatosClienteBlack())
    else:
        raise Exception("Tipo de cliente no existe")

    cliente.inicializar(datos)

    return cliente