from ..cliente import Cliente
from ..transaccion import Transaccion


class HtmlProcessor:
    def __init__(self) -> None:
        pass

    def crear_html(self, cliente: Cliente, transacciones: list[Transaccion]):
        html_transacciones = ""
        for e in transacciones:
            html_transacciones += """
            <tr>
              <td>{fecha}</td>
              <td>{tipo}</td>
              <td>{estado}</td>
              <td>{monto}</td>
              <td>{razon}</td>
            </tr>
          """.format(
                fecha=e.fecha,
                tipo=e.tipo.replace(
                    "_",
                    " ",
                ),
                estado=e.estado,
                monto=e.monto,
                razon=e.justificar(cliente),
            )

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
            <body>
             <main class="container mt-5 py-5">
              <div class="mb-4">
                  <h1>{apellido}, {nombre}</h1>
                  <div><b>Numero cliente</b>: {numero} </div>
                  <div><b>DNI</b>: {dni} </div>
                  <div><b>Direccion</b>: {direccion}  </div>
              </div>
              <table class="table table-striped table-hover mt-3">
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
              </main>
            </body>
          </html>
        """.format(
            direccion=cliente.direccion,
            numero=cliente.numero,
            nombre=cliente.nombre,
            apellido=cliente.apellido,
            dni=cliente.dni,
            transacciones=html_transacciones,
        )

        archivo = open("./index.html", "w+")
        archivo.write(html)
        archivo.close()
