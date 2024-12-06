import pygame
from funciones_pygame import *
from funciones_consola import *

grilla = [
 {"piezas":[]},
 {"piezas":[]},
 {"piezas":[]},
 {"piezas":[]}]
# Inicializa pygame y configura la pantalla
pygame.init()
tamaño_celda = 64
columnas = 8
filas = 8
ancho_ventana = columnas * tamaño_celda
alto_ventana = filas * tamaño_celda  
pantalla = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Candy Crush")

# Variables de el juego
caramelo_rojo  = pygame.image.load("caramelo_rojo.png")
caramelo_rojo = pygame.transform.scale(caramelo_rojo,(100,100))
caramelo_azul  = pygame.image.load("caramelo_azul.png")
caramelo_azul = pygame.transform.scale(caramelo_azul,(100,100))
caramelo_verde  = pygame.image.load("caramelo_verde.png")
caramelo_verde = pygame.transform.scale(caramelo_verde,(100,100))
corriendo = True
puntaje = 0

# Bucle principal
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Botón izquierdo del mouse
                pos_click = evento.pos
                manejar_click(grilla, pos_click, tamaño_celda, pantalla)

    # Actualizar y mostrar la pantalla
    pantalla.fill((0, 0, 0))  # Fondo negro
    imprimir_carmelos(grilla, pantalla, caramelo_azul, caramelo_rojo, caramelo_verde)
    # mostrar_puntaje(pantalla, puntaje, fuente, color, (10, 10))
    pygame.display.flip()

    # Control de FPS
    pygame.time.Clock().tick(60)

pygame.quit()