import random

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
        fila = int(input(f"Re-ingrese una fila(entre {min} y {max}): "))
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
        columna = int(input(f"Re-ingrese una columna(entre {min} y {max}): "))
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
    rango = range(1, len(lista) - fila) if direccion == 1 else range(1, fila + 1)

    for i in rango:
        fila_actual = fila + i if direccion == 1 else fila - i
        if lista[fila_actual][clave][columna] == num_seleccionado:
            cont_iguales += 1
            if cont_iguales == 3:
                break
        else:
            break    
    return cont_iguales

def generar_csv(nombre_archivo:str, lista:list):
    """
    Recibe una lista y genera un archivo csv con los datos de la lista
    """
    nombre_archivo += ".csv"
    try:
        with open(nombre_archivo, "a") as archivo: 
            for e_tema in lista:
                archivo.write(f"{e_tema}\n")
                
    except FileNotFoundError:
        with open(nombre_archivo, "w") as archivo: 
            for e_tema in lista:
                archivo.write(f"{e_tema}\n")
                
def recorrer_lista(lista:list, puntos:list):
    """
    Recorre la lista pasada por parametro
    """
    primera_vez = True
    for i in range(len(lista)):
        if primera_vez:
            primera_vez = False
        elif lista[i] == lista[0]:
            lista[1] += puntos

def chequear_posiciones(matriz:list, clave:str, fila:int, columna:int):
    """
    Llama a otras funciones para chequear si dos columnas abajo o arriba hay 
    tres unos, tres dos o tres tres 
    """
    puntos = 0
    lista = []
    separador = ", "
    
    contador_arriba = recorrer_lista_diccionarios(matriz, clave, fila, columna,1)    
    contador_abajo = recorrer_lista_diccionarios(matriz, clave, fila, columna, -1)    
    
    if (contador_abajo + contador_arriba) >= 3:
        puntos += 10    

    nombre = input("Ingrese su nombre: ").capitalize()
    
    puntaje = separador.join([nombre, str(puntos)])
    lista.append(puntaje)
    
    recorrer_lista(lista, puntos) 
    mostrar(nombre, puntos)
    generar_csv("Lista_jugadores", lista) 