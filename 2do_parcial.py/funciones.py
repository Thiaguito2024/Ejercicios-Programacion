import random

def generar_matriz(lista:list, cant_columnas:int):
    for i in range(len(lista)):
        for j in range(cant_columnas):
            numero = random.randint(1,3)
            lista[i]["piezas"].append(numero)
    

def pedir_fila(min:int, max:int): 
    fila = int(input("Ingrese una fila: "))
    while fila < min or fila > max:
        fila = int(input(f"Ingrese una fila(entre {min} y {max}): "))
        
    return fila

def pedir_columna(min:int, max:int): 
    columna = int(input("Ingrese una columna: "))
    while columna < min or columna > max:
        columna = int(input(f"Ingrese una columna(entre {min} y {max}): "))
        
    return columna

def recorrer_lista_diccionarios(lista:list, clave:str, fila:int, columna:int)->int:
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
                elif cont_vueltas > 3 and cont_iguales == 3:
                    break
                elif cont_iguales == 3:
                    puntos += 10
                    break
    return puntos

def recorrer_lista_diccionarios_al_reves(lista:list, clave:str, fila:int, columna:int)->int:
    num_seleccionado = lista[fila][clave][columna]
    puntos = 0
    cont_iguales = 0
    cont_vueltas = 0
    for i in range(len(lista)-1, -1, -1):
        cont_vueltas += 1
        if lista[i][clave][columna] == num_seleccionado: # Si la columna es 3,3,2,3 printea que gano diez puntos
            cont_iguales += 1
            if cont_vueltas == 3 and cont_iguales < 3:
                break
            elif cont_vueltas > 3 and cont_iguales == 3:
                break
            elif cont_iguales == 3:
                puntos += 10
                break
    return puntos

def recorrer_lista_diccionarios_al_reves_2(lista:list, clave:str, fila:int, columna:int)->int:
    num_seleccionado = lista[fila][clave][columna]
    puntos = 0
    cont_iguales = 0
    cont_vueltas = 0
    for i in range(len(lista)-2, -1, -1):
        cont_vueltas += 1
        if lista[i][clave][columna] == num_seleccionado: # Si la columna es 3,3,2,3 printea que gano diez puntos
            cont_iguales += 1
            if cont_vueltas == 3 and cont_iguales < 3:
                break
            elif cont_vueltas > 3 and cont_iguales == 3:
                break
            elif cont_iguales == 3:
                puntos += 10
                break
    return puntos

def generar_csv(nombre_archivo:str, lista:list):
    nombre_archivo += ".csv"
    with open(nombre_archivo, "w") as archivo:
        for e_tema in lista:
            archivo.write(f"{e_tema}\n")

def chequear_posiciones(matriz:list, clave:str, fila:int, columna:int):
    puntos = 0
    lista = []
    if fila == len(matriz) -1:
        puntos = recorrer_lista_diccionarios_al_reves(matriz, clave, fila, columna)
    elif fila == len(matriz) -2:
        puntos = recorrer_lista_diccionarios_al_reves_2(matriz, clave, fila, columna)
    else:
        puntos = recorrer_lista_diccionarios(matriz, clave, fila, columna)

    nombre = input("Ingrese su nombre: ")
    if puntos == 10:
        print("Gano 10 puntos")   
        print(f"El jugador {nombre} tiene {puntos} puntos")
    else:
        print("SEGUI PARTICIPANDO")
        print(f"El jugador {nombre} tiene {puntos} puntos")
    