from funciones_parcial import *
lista = [
 {"piezas":[]},
 {"piezas":[]},
 {"piezas":[]},
 {"piezas":[]}]

# seguir = "Si"

# while seguir == "Si":
generar_matriz(lista, 7)
for i in range(len(lista)):
    print(lista[i]["piezas"])

fila = pedir_fila(0,3)
columna = pedir_columna(0,6)
chequear_posiciones(lista, "piezas", fila, columna)
    
    # seguir = input("Desea seguir jugando: ")
    
    # while seguir != "Si" and seguir != "No" or seguir.isalpha() == False:
    #     seguir = input("Desea seguir jugando(Si/No): ")
        
# No hacer hasta que lo haga de manera consecutiva, crear archivo csv con nombre y puntos de los jugadores
# arreglar que sean consecutivos, no agregar nombre y generar csv hasta que lo haga de manera consecutiva
# Preguntar isdigit()-> da error en la verificacion de la fila y columna
# Si el usuario ingresa Si cuando se le pregunta si quiere seguir, me muestra una matriz de 14 columnas