import pygame 
import colores
from funciones_pygame_final import *

pygame.init() 

# CREO LA PANTALLA 
ancho_ventana = 800
alto_ventana = 600
pantalla = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Candy Crush")
icono = pygame.image.load("Candy_icono.png")
pygame.display.set_icon(icono)

# Imagenes
imagen_fondo = cargar_imagen_a_escala("fondo_candy_3.png", (800,600))

# CONSTANTES
lista_jugadores = []
puntajes = leer_csv("Scoreboard.csv")
fuente = pygame.font.SysFont(None, 36)
fuente_scoreboard = pygame.font.SysFont(None, 30)
play_rect = pygame.Rect(300,300,300,75)
input_rect = pygame.Rect(300,400,400,75)
scoreboard_rect = pygame.Rect(0,200,250,400)
scoreboard_inactivo = colores.RED1
scoreboard_activo = colores.GREEN1
color_input = scoreboard_inactivo
nombre = "Ingrese su nombre: " # Texto de el input
primer_input = True
active = False # Bandera input 

running = True

# BUCLE PRINCIPAL
while running:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            running = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(evento.pos):
                active = True
                nombre_jugador = nombre
                if primer_input:  # Si es la primera vez que hace clic, limpia el input
                    nombre = ""
                    primer_input = False

            if play_rect.collidepoint(evento.pos) and active:
                lista_jugadores.append(nombre)
                puntos = juego_principal(pantalla, imagen_fondo)
                lista_jugadores.append(puntos)

        if evento.type == pygame.KEYDOWN and active:
            if evento.key == pygame.K_BACKSPACE: # Si presiona el DELETE, borra
                nombre = nombre[:-1]
            elif evento.key == pygame.K_RETURN: #Si presiona enter, arranca el juego de nuevo
                lista_jugadores.append(nombre)
                puntos = juego_principal(pantalla, imagen_fondo)
                lista_jugadores.append(puntos)
            else: # Si presiona cualquier otro caraceter o numero, se agrega a la cadena 
                nombre += evento.unicode  
        
    # Dibujo en la pantalla
    pantalla.blit(imagen_fondo,(0,0))
    color_input = scoreboard_activo if active else scoreboard_inactivo
    pygame.draw.rect(pantalla, color_input, input_rect) 
    pygame.draw.rect(pantalla, colores.WHEAT, play_rect)
    pygame.draw.rect(pantalla, colores.PINK, scoreboard_rect)

    # Botones
    scoreboard_texto = fuente.render("SCOREBOARD", True, colores.WHITE) # Titulo de Scoreboard
    play_texto = fuente.render("Jugar",True, colores.GREEN) # Boton jugar
    texto_renderizado = fuente.render(nombre, True, colores.BLACK) # Input

    # Bliteo en pantalla de los textos
    pantalla.blit(play_texto,(play_rect.x+120, play_rect.y+25)) 
    pantalla.blit(texto_renderizado, (input_rect.x + 10, input_rect.y + 20))
    pantalla.blit(scoreboard_texto, (scoreboard_rect.x + 15, scoreboard_rect.y + 15))

    # Scoreboard
    espacio = 30
    
    for puntaje in puntajes:
        pantalla.blit(fuente_scoreboard.render(f"{puntaje}", True, colores.WHITE),(scoreboard_rect.x +15, scoreboard_rect.y+espacio + 15)) # Bliteo el historial de nombre y puntos
        espacio += 30 # Para mover el siguiente jugador más abajo en el scoreboard

    for jugador in lista_jugadores:
        pantalla.blit(fuente_scoreboard.render(f"{jugador}", True, colores.WHITE),(scoreboard_rect.x +15, scoreboard_rect.y+espacio + 15)) # Bliteo nombre y puntos
        espacio += 30  # Para mover el siguiente jugador más abajo en el scoreboard
    pygame.display.flip()

generar_csv("Scoreboard", lista_jugadores) # Se guarda afuera pq al estar en el modo append, lo agrega vuelta a vuelta
pygame.quit()