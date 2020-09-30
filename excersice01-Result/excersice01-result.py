""" 
Este es un programa de python que recibe el nombre del cliente, un producto y el costo de este.
El programa va guardando la información de todos los clientes que se introducen.
Al correr el código, se puede escoger una de las tres opciones:
1: Introducir un cliente nuevo
2. Obtener el reporte actual
3. Cerrar el programa

"""

# creando la lista vacia
listaRegistro = []
clientes = 0
eleccion = 0
costoTotal = 0

while eleccion != " ":
    print(" ")
    print("1. Para introducir el nombre de un cliente nuevo: escriba 'cliente'")
    print("2. Para obtener el reporte actual del día: escriba 'reporte'")
    print("3. Para finalizar programa presione Enter")
    print(" ")
    eleccion = str(input("¿Qué desea hacer?"))

    # si se elige la primera opción, se tiene que introducir los datos del cliente
    if eleccion == "cliente":

        cliente = input("nombre del cliente: ")
        producto = input("producto: ")
        costo = float(input("costo ($0.00): "))

        registro = dict(cliente=cliente, producto=producto, costo=costo)

        listaRegistro.append(registro)
        clientes += 1
        costoTotal += float(registro["costo"])
    # si se quiere ver el reporte, se imprime el numero de clientes y el total de costos

    if eleccion == "reporte":
        print(" ")
        print("El reporte actual es:")
        print("Se han ingresado " + str(clientes) + " clientes")
        print("Los costos suman un total de " + str(costoTotal) + " dólares")
        print(" ")


# Si no se selecciona la opción 1 o 2, se cierra el programa
print("Se ha cerrado el programa")
