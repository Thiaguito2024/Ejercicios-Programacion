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
    fila = int(input("Ingrese una fila: "))
    while fila < min or fila > max:
        fila = int(input(f"Ingrese una fila(entre {min} y {max}): "))
        
    return fila

def pedir_columna(min:int, max:int)-> int: 
    """
    Pide la columna al usuario y lo retorna 
    """
    columna = int(input("Ingrese una columna: "))
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

def recorrer_lista_diccionarios(lista:list, clave:str, fila:int, columna:int)->int:
    """ 
    Recorre la lista pasada por parametro desde la fila y columna pasada por el usuario
    Retorna los puntos que obtuvo el usuario 
    """
    num_seleccionado = lista[fila][clave][columna]
    puntos = 0
    cont_iguales = 0
    cont_vueltas = 0
    for i in range(len(lista)):
            cont_vueltas += 1
            if lista[i][clave][columna] == num_seleccionado: 
                cont_iguales += 1
                if cont_vueltas == 3 and cont_iguales < 3:
                    break
                elif cont_vueltas > 3 and cont_iguales <= 3:
                    break
                elif cont_iguales == 3:
                    puntos += 10
                    break
    return puntos

def recorrer_lista_diccionarios_desde_anteultima_fila(lista:list, clave:str, fila:int, columna:int)->int:
    """
    Recorre la lista pasada por parametro desde la fila y columna pasada por el usuario, para arriba 
    Retorna los puntos que obtuvo el usuario 
    """
    num_seleccionado = lista[fila][clave][columna]
    puntos = 0
    cont_iguales = 0
    cont_vueltas = 0
    for i in range(len(lista)-2, -1, -1):
        cont_vueltas += 1
        if lista[i][clave][columna] == num_seleccionado: 
            cont_iguales += 1
            if cont_vueltas == 3 and cont_iguales < 3:
                break
            elif cont_vueltas > 3 and cont_iguales < 3:
                break
            elif cont_iguales == 3:
                puntos += 10
                break
    return puntos

def recorrer_lista_diccionarios_desde_ultima_fila(lista:list, clave:str, fila:int, columna:int)->int:
    """ 
    Recorre la lista pasada por parametro desde la fila y columna pasada por el usuario, para arriba 
    Retorna los puntos que obtuvo el usuario 
    """
    num_seleccionado = lista[fila][clave][columna]
    puntos = 0
    cont_iguales = 0
    cont_vueltas = 0
    for i in range(len(lista)-1, -1, -1):
        cont_vueltas += 1
        if lista[i][clave][columna] == num_seleccionado: 
            cont_iguales += 1
            if cont_vueltas == 3 and cont_iguales < 3:
                break
            elif cont_vueltas > 3 and cont_iguales <= 3:
                break
            elif cont_iguales == 3:
                puntos += 10
                break
    return puntos

def generar_csv(nombre_archivo:str, lista:list):
    """
    Recibe una lista y genera un archivo csv con los datos de la lista
    """
    nombre_archivo += ".csv"
    with open(nombre_archivo, "w") as archivo:
        for e_tema in lista:
            archivo.write(f"{e_tema}\n")

def recorrer_lista(lista:list, puntos:list):
    """
    Recorre la lista pasada por parametro
    """
    for i in range(len(lista)):
        if lista[i] == lista:
            lista[1] += puntos

def chequear_posiciones(matriz:list, clave:str, fila:int, columna:int):
    """
    Llama a otras funciones para chequear si dos columnas abajo o arriba hay 
    tres unos, tres dos o tres tres 
    """
    puntos = 0
    separador = ", "
    lista = []
    
    if fila == len(matriz) -1:
        puntos = recorrer_lista_diccionarios_desde_ultima_fila(matriz, clave, fila, columna)
    elif fila == len(matriz) -2:
        puntos = recorrer_lista_diccionarios_desde_anteultima_fila(matriz, clave, fila, columna)
    else:
        puntos = recorrer_lista_diccionarios(matriz, clave, fila, columna)

    nombre = input("Ingrese su nombre: ").capitalize()
    mostrar(nombre, puntos)

    puntaje = separador.join([nombre, str(puntos)])
    lista.append(puntaje)
    generar_csv("Lista_jugadores", lista)

    recorrer_lista(lista, puntos)