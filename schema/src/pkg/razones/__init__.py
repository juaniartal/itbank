from http import client
from pydoc import cli
from ..cliente import Cliente
from ..transaccion import Transaccion

class Razones:
    def __init__(self) -> None:
        pass

    def justificar(cliente : Cliente, transaccion : Transaccion) -> str:
        
        return "-"