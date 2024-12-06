import pygame
from colores import *
import random

def generar_grilla(lista, columnas, filas):
    """
    Llena una lista de diccionarios con números aleatorios entre 1 y 3.
    """
    for i in range(filas):
        for j in range(columnas):
            numero = random.randint(1, 3)
            lista[i]["piezas"].append(numero)

def imprimir_carmelos(lista,screen, caramelo_rojo,caramelo_azul,caramelo_verde): # Funcion para imprimir caramelos
    coordenadas_fila = 150 # Donde va a estar la primera fila
    for objeto in lista: # Por cada diccionario en la lista:
        coordenadas_columna = 50 # Donde va a estar la primera columna
        for caramelo in objeto["piezas"]: # Por cada caramelo en el diccionario:
            # Dependiendo del valor (1,2,3), blitea un caramelo del color correspondiente, en las coordenadas correspondientes
            if caramelo == 1: 
                screen.blit(caramelo_rojo,(coordenadas_columna, coordenadas_fila))
            elif caramelo == 2:
                screen.blit(caramelo_azul,(coordenadas_columna, coordenadas_fila))
            elif caramelo == 3:
                screen.blit(caramelo_verde,(coordenadas_columna, coordenadas_fila))
            coordenadas_columna+=100 # Con cada caramelo, se suma 100 a la coordenada, para que no esten pegados
            if coordenadas_columna >= 700: # Cuando llega a 700, resetea
                coordenadas_columna = 100
        if coordenadas_fila >= 400: # Cuando llega a 400, resetea
            coordenadas_fila = 150
        coordenadas_fila+=100 # Con cada fila, se suma 100 a la coordenada, para que no esten pegadas

def verificar_combinacion(grilla, fila, columna, clave):
    num_seleccionado = grilla[fila][clave][columna]
    retorno = False

    if fila <= len(grilla) - 3: # Se fija si puede ir dos filas para abajo para que no se vaya de el rango
        if (grilla[fila + 1][clave][columna] == num_seleccionado and grilla[fila + 2][clave][columna] == num_seleccionado):
            retorno = 10
    if fila >= 2: # Se fija si puede ir dos filas para arriba para que no se vaya de el rango
        if (grilla[fila - 1][clave][columna] == num_seleccionado and grilla[fila - 2][clave][columna] == num_seleccionado):
            retorno = 10
    else: 
        retorno = -1        
    
    return retorno

def manejar_click(grilla, pos_click, tamaño_celda, pantalla):
    columna = pos_click[0] // tamaño_celda # Calculo la posicion de el click
    fila = pos_click[1] // tamaño_celda

    # Chequeo que el click este dentro de la grilla
    if fila < len(grilla) and columna < len(grilla[fila]):
        if verificar_combinacion(grilla, fila, columna):
            puntaje += 10
            nombre = input("Ingrese su nombre: ")

            imprimir_carmelos
            pygame.display.flip()
            
def obtener_scoreboard():
    try:
        with open("scoreboard.csv", "r+") as archivo:
            scoreboard = archivo.readlines()
    except FileNotFoundError:
        with open("scoreboard.csv", "w") as archivo:
            archivo.write("Nombre, Puntos\n")
            scoreboard = []
    return scoreboard

def agregar_y_mostrar_scoreboard(puntos): # CHEQUEAR FUNCION
    # Obtener el contenido actual del scoreboard
    scoreboard = obtener_scoreboard()

    # Pedir el nombre del jugador
    nombre = input("Ingrese su nombre: ")

    # Agregar la nueva entrada al archivo
    with open("scoreboard.csv", "a") as archivo:
        archivo.write(f"{nombre}, {puntos}\n")