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
import datetime as dt
from tkinter.filedialog import Open

# Defino constantes y variables
opciones = ""
print("Bienvenido al programa de control de cheques")
print("Por favor seleccione una opciones")
print("1. Cargar un nuevo cheque")
...
print("3. Salir")
""
runtime = True
datetime = dt.date.today()

# defino funciones


def readFile(urlfile):
    cheques = []
    file = open(urlfile, "r")
    print(file)
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


def buscarPorDni(dni, tipo):
    busqueda = []
    cantidad = 0
    cheques = readFile(urlfile)
    for cheque in cheques:
        if cheque['DNI'] == dni and cheque['Tipo'] == tipo:
            cantidad += 1
            print("cheque encontrado")
            busqueda.append(cheque)
    print(f"Se encontraron {cantidad} de cheques")
    return busqueda

def grabarCSV(dni, busqueda):
    file = open(dni+"_"+datetime+".csv", "w")
    csvfile = csv.writer(file)
    for row in busqueda:
        csvfile.writerow([row['NroCheque'], row["CodigoBanco"], row["CodigoSucursal"],
        row["NumeroCuentaOrigen"], row["NumeroCuentaDestino"], row["Valor"],
        row["FechaOrigen"], row["FechaPago"], row["DNI"], row["Tipo"], row["Estado"]])
    file.close()
    print("El archivo CSV se gravo correctamente.")

if __name__ == "__main__":
    while runtime:
        print(opciones)
        op = input()
        if op == "1":
            urlfile = input("Ingrese el nombre del archivo que contiene los cheques: ")
            dni = input("Ingrese el dni del usuario a consultar: ")
            tipo = input("Selecciones el tipo de cheque a buscar EMITIDO o DEPOSITADO: ")
            salida = input("Elija si desea recibir la salida por pantalla o CSV: ")
            print(urlfile, dni, tipo, salida)
            try:
                resultado = buscarPorDni(dni, tipo)
                if salida == "PANTALLA":
                    print(resultado)
                elif salida == "CSV":
                    grabarCSV(resultado)
                else:
                    print("Opcion invalida")
            except Exception as error: 
                print("ingreso un dni erroneo")
                print(error)
            continue

        else:
            runtime = False
