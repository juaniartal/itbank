from ..cliente import Cliente

class HtmlProcessor:

    def __init__(self) -> None:
        self.elementos = []

    def append(self, elemento: dict):
        self.elementos.append(elemento)

    def crear_html(self, cliente: Cliente):
        transacciones = ""
        for e in self.elementos:
            transacciones += "<tr><td>{fecha}</td><>td>{tipo}</td><td>{estado}</td><td>{monto}</td><td>{razon}</td></tr>".format
            fecha = e["fecha"]
            tipo = e["tipo"].replace("_", " ",)
            estado = e["estado"],
            monto = e["monto"],
            razon = e["razon"]

            html = """              
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Listado de transacciones</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor"
      crossorigin="anonymous"
    />
    <link rel="stylesheet" href="index.css">
  </head>
  <body class="body">
    <div class="intro">
        <h1>{apellido}, {nombre}</h1>
        <div>Numero cliente: {numero} </div>
        <div> DNI: {dni} </div>
        <div> Direccion: {direccion}  </div>
    </div> 
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Fecha</th>
          <th scope="col">Tipo</th>
          <th scope="col">Estado</th>
          <th scope="col">Monto</th>
          <th scope="col">Razon</th>
        </tr>
      </thead>
      {transacciones}
    </table>
  </body>
</html>
            """.format(
                direccion=str[cliente.direccion],
                numero=cliente.numero,
                nombre=cliente.nombre,
                apellido=cliente.apellido,
                dni=cliente.dni,
                transacciones=transacciones
            )

            archivo = open("../index.html", "w")
            archivo.write(html)
            archivo.close()
