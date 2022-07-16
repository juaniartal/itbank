from pkg.html import HtmlProcessor
from pkg.buscador_problema import BuscadorProblema
from pkg.parser import Parser

if __name__ == "__main__":
    parser = Parser()
    cliente, eventos = parser.execute('../resources/json/test.json')
    salida = HtmlProcessor()

    #buscador = BuscadorProblema(cliente)
    # podria crear una app parecida a la del profe
    print(cliente.nombre)
    print(cliente.apellido)
    print(cliente.dni)

    #for e in eventos:
        #print("transaccion:", e.estado)
        #salida.append(buscador.getResultado(e))

    salida.crear_html(cliente)

#Deberiamos importar el buscador problema