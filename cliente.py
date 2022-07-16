
CLASSIC = "CLASSIC"
BLACK = "BLACK"
GOLD = "GOLD"


class Cliente:
    def __init__(self, **kwargs) -> None:
        self.cuenta = Cuenta(**kwargs)

    def inicializar(self, datos):
        self.numero = datos["numero"]
        self.nombre = datos["numero"]
        self.apellido = datos["apellido"]
        self.direccion = Direccion(**datos["direccion"])  # para las clases etc
