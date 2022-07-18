class Direccion:
    calle: str = ""
    numero: str = ""
    ciudad: str = ""
    provincia: str = ""
    pais: str = ""
    

    def __init__(
        self, calle: str, numero: str, ciudad: str, provincia: str, pais: str
    ) -> None:
        self.calle = calle
        self.numero = numero
        self.ciudad = ciudad
        self.provincia = provincia
        self.pais = pais

    def validate(
        self,
    ) -> bool:
        return True

    def __str__(self) -> str:
        return "{calle} {numero}, {ciudad}, {provincia}, {pais}.".format(
            calle=self.calle,
            numero=self.numero,
            ciudad=self.ciudad,
            provincia=self.provincia,
            pais=self.pais,
        )
