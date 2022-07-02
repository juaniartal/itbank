# 1. El script de Python se debe llamar listado_chesques.py
# 2. El orden de los argumentos son los siguientes:
# a. Nombre del archivo csv.
# b. DNI del cliente donde se filtraran.
# c. Salida: PANTALLA o CSV
# d. Tipo de cheque: EMITIDO o DEPOSITADO
# e. Estado del cheque: PENDIENTE, APROBADO, RECHAZADO. (Opcional)
# f. Rango fecha: xx-xx-xxxx:yy-yy-yyyy (Opcional)
# 3. Si para un DNI dado un número de cheque de una misma cuenta se repite se
# debe mostrar el error por pantalla, indicando que ese es el problema.
# 4. Si el parámetro “Salida” es PANTALLA se deberá imprimir por pantalla todos
# los valores que se tienen, y si “Salida” es CSV se deberá exportar a un csv
# con las siguientes condiciones:
# a. El nombre de archivo tiene que tener el formato
# <DNI><TIMESTAMPS ACTUAL>.csv
# b. Se tiene que exportar las dos fechas, el valor del cheque y la cuenta.
# 5. Si el estado del cheque no se pasa, se deberán imprimir los cheques sin
# filtrar por estado
# En la descripción de los campos, falta el campo TIPO, que es un string que puede tener los siguientes valores  "EMITIDO" o "DEPOSITADO"

# Defino librerias a utilizar
import csv

# Defino constantes y variables
opciones = ""
print("Bienvenido al programa de control de cheques")
print("Por favor seleccione una opciones")
print("1. Cargar un nuevo cheque")
...
print("3. Salir")
""
runtime = True

# defino funciones


def readFile(urlfile):
    cheques = []
    file = open(urlfile, "r")
    csvfile = csv.reader(file)
    for row in csvfile:
        if row != []:
            data = {"NroCheque": row[0], "CodigoBanco": row[1], "CodigoSucursal": row[2],
                    "NumeroCuentaOrigen": row[3], "NumeroCuentaDestino": row[4], "Valor": row[5],
                    "FechaOrigen": row[6], "FechaPago": row[7], "DNI": row[8], "Tipo": row[9],
                    "Estado": row[10]}
            cheques.append(data)
    file.close()
    return cheques


def filtrarCSV(filters):
    busqueda = []
    cheques = readFile(urlfile)
    
    for cheque in cheques:
        if all(f(cheque) for f in filters):
            busqueda.append(cheque)

    print(f"Se encontraron {len(busqueda)} de cheques")
    return busqueda


if __name__ == "__main__":
    while runtime:
        print(opciones)
        op = input()
        if op == "1":
            urlfile = input("Ingrese el path del archivo: ")
            dni = input("Ingrese el DNI del usuario a consultar: ")
            salida = input("Elija si desea recibir la salida por pantalla o CSV: ")
            tipo = input("Selecciones el tipo de cheque a buscar EMITIDO o DEPOSITADO: ")
            estado = input("Selecciones el estado del cheque PENDIENTE, APROBADO, RECHAZADO (Opcional): ")
            rango = input("Ingrese el rango de fechas en el formato xx-xx-xxxx:yy-yy-yyyy (Opcional): ")

            filters = [lambda cheque: cheque["DNI"] == dni, lambda cheque: estado.upper() in cheque["Estado"].upper(),]

            try:
                resultado = filtrarCSV(filters)
                print(resultado)
            except:
                print("No se encontraron resultados")
            continue

        else:
            runtime = False
