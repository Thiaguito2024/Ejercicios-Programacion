import random
from b import *
def generar_matriz(lista:list, cant_columnas:int):
    """
    Genera una matriz con la lista y cantidad de columnas pasadas por el usuario
    """
    for i in range(len(lista)):
        for j in range(cant_columnas):
            numero = random.randint(1,3)
            lista[i]["piezas"].append(numero)
    

def pedir_fila(min:int, max:int)->int: 
    """
    Pide la columna al usuario y lo retorna
    """
    fila = input("Ingrese una fila: ")
    while not fila.isdigit():
        fila = input("Re-ingrese una fila: ")
    fila = int(fila)    
    while fila < min or fila > max:
        fila = int(input(f"Ingrese una fila(entre {min} y {max}): "))
    return fila

def pedir_columna(min:int, max:int)-> int: 
    """
    Pide la columna al usuario y lo retorna 
    """
    columna = input("Ingrese una columna: ")
    while not columna.isdigit():
        columna = input("Re-ingrese una columna: ")
    columna = int(columna)
    while columna < min or columna > max:
        columna = int(input(f"Ingrese una columna(entre {min} y {max}): "))
    return columna

def mostrar(nombre:str, puntos:int):
    """
    Muestra el nombre y los puntos que gano el usuario
    """
    if puntos == 10:
        print("Gano 10 puntos")   
        print(f"El jugador {nombre} tiene {puntos} puntos")
    else:
        print("SEGUI PARTICIPANDO")
        print(f"El jugador {nombre} tiene {puntos} puntos")

def recorrer_lista_diccionarios(lista:list, clave:str, fila:int, columna:int, direccion:int)->int:
    num_seleccionado = lista[fila][clave][columna]
    cont_iguales = 1
    cont_vueltas = 0 
    rango = range(1, len(lista) - fila) if direccion == 1 else range(1, fila + 1)
    # if direccion == 1: 
        # for i in range(1, len(lista) - fila):
    for i in rango:
        fila_actual = fila + i if direccion == 1 else fila - i
        # cont_vueltas += 1 
        if lista[fila_actual][clave][columna] == num_seleccionado:
            cont_iguales += 1
            if cont_iguales == 3:
                break
        else:
            break  
    # elif direccion == -1: 
    #     for i in range(1, fila+1):
    #         if lista[fila-i][clave][columna] == num_seleccionado:
    #             cont_iguales += 1
    #             if cont_iguales == 3:
    #                 break
    #         else:
    #             break  
    return cont_iguales

def generar_csv(nombre_archivo:str, lista:list):
    """
    Recibe una lista y genera un archivo csv con los datos de la lista
    """
    nombre_archivo += ".csv"
    with open(nombre_archivo, "a") as archivo: 
        for e_tema in lista:
            archivo.write(f"{e_tema}\n")

def recorrer_lista(lista:list, puntos:list):
    """
    Recorre la lista pasada por parametro
    """
    for i in range(len(lista)):
        if lista[i] == lista[0]:
            lista[1] += puntos

def chequear_posiciones(matriz:list, clave:str, fila:int, columna:int):
    """
    Llama a otras funciones para chequear si dos columnas abajo o arriba hay 
    tres unos, tres dos o tres tres 
    """
    puntos = 0
    separador = ", "
    lista = []
    
    contador_arriba = recorrer_lista_diccionarios(matriz, clave, fila, columna,1)    
    contador_abajo = recorrer_lista_diccionarios(matriz, clave, fila, columna, -1)    
    
    if (contador_abajo + contador_arriba) >= 3:
        puntos += 10    
    # if fila == len(matriz) -1:
    #     puntos = recorrer_lista_diccionarios(matriz, clave, fila, columna,-1)
    # else:
    #     puntos = recorrer_lista_diccionarios(matriz, clave, fila, columna)

    nombre = input("Ingrese su nombre: ").capitalize()
    mostrar(nombre, puntos)

    # puntaje = separador.join([nombre, str(puntos)])
    lista.append(nombre)
    lista.append(puntos)
    recorrer_lista(lista, puntos) 
    
    generar_csv("Lista_jugadores", lista) 