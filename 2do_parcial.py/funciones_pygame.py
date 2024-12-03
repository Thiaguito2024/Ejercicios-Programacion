import pygame
from colores import *

def dibujar_grilla(ventana,grilla:dict, filas:int, columnas:int, tamaño_celda:int,imagen1, imagen2, imagen3):
    for fila in filas:
        for columna in columnas:
            if grilla[fila][columna] == 1:
                imagen = imagen1
            elif grilla[fila][columna] == 2:
                imagen = imagen2
            elif grilla[fila][columna] == 3:
                imagen = imagen3
            
            ventana.blit(imagen, (columna * tamaño_celda, fila * tamaño_celda))
            
            pygame.draw.rect(ventana, LIGHTBLUE, (columna * tamaño_celda, fila * tamaño_celda, tamaño_celda, tamaño_celda), 1) # El 1 indica grosor del borde