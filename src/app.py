from clases import Parser

if __name__ == "__main__":
    parse = Parser()
    cliente, eventos = parser.execute('eventos.json')
    salida = ProcesadorHtml()

    buscador = BuscadorProblema(cliente)
    # podria crear una app parecida a la del profe
    print(cliente.nombre)
    print(cliente.apellido)
    print(cliente.dni)
    print(cliente.cuenta.limite_extraccion_diario)

for e in eventos:
    #print("transaccion:", e.estado)
    salida.append(buscador.getResultado(e))
salida.crear_html(cliente)

#Deberiamos importar el buscador problema