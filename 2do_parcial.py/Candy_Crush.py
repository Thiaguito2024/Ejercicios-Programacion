from funciones import *
lista = [
 {"piezas":[]},
 {"piezas":[]},
 {"piezas":[]},
 {"piezas":[]}]


generar_matriz(lista, 7)
for i in range(len(lista)):
    print(lista[i]["piezas"])

fila = pedir_fila(0,3)
columna = pedir_columna(0,6)
chequear_posiciones(lista, "piezas", fila, columna)

# No hacer hasta que lo haga de manera consecutiva, crear archivo csv con nombre y puntos de los jugadores
# arreglar que sean consecutivos, no agregar nombre y generar csv hasta que lo haga de manera consecutiva