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

imagen_fondo = pygame.image.load("Fondo_Candy.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo, (800,600))
# CONSTANTES
lista_jugadores = []
fuente = pygame.font.SysFont(None, 36)
play_rect = pygame.Rect(300,300,300,75)
input_rect = pygame.Rect(300,400,400,75)
scoreboard_rect = pygame.Rect(10,100,250,400)
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
                puntos = juego_principal(pantalla)

        if evento.type == pygame.KEYDOWN and active:
            if evento.key == pygame.K_BACKSPACE: # Si presiona el DELETE, borra
                nombre = nombre[:-1]
            elif evento.key == pygame.K_RETURN: #Si presiona enter, arranca el juego de nuevo
                lista_jugadores.append(nombre)
                puntos = juego_principal(pantalla)
                lista_jugadores.append(puntos)
            else: # Si presiona cualquier otra letra, se agrega a la cadena 
                nombre += evento.unicode 

    # Dibujo en la pantalla
    pantalla.fill(colores.LIGHTBLUE)
    color_input = scoreboard_activo if active else scoreboard_inactivo
    pygame.draw.rect(pantalla, color_input, input_rect) 
    pygame.draw.rect(pantalla, colores.WHEAT, play_rect)
    pygame.draw.rect(pantalla, colores.BLACK, scoreboard_rect)

    # Botones
    scoreboard_texto = fuente.render("SCOREBOARD", True, colores.RED1) # Titulo de Scoreboard
    play_texto = fuente.render("Jugar",True, colores.GREEN) # Boton jugar
    texto_renderizado = fuente.render(nombre, True, colores.BLACK) # Input

    # Bliteo en pantalla de los textos
    pantalla.blit(play_texto,(play_rect.x+120, play_rect.y+25)) 
    pantalla.blit(texto_renderizado, (input_rect.x + 10, input_rect.y + 20))
    pantalla.blit(scoreboard_texto, (scoreboard_rect.x + 15, scoreboard_rect.y + 15))

    # Scoreboard
    generar_csv("Scoreboard", lista_jugadores)
    espacio = 30
    for persona in lista_jugadores:
        pantalla.blit(fuente.render(f"{persona}", True, colores.GREEN),(scoreboard_rect.x +15, scoreboard_rect.y+espacio+15)) # Bliteo nombre y puntos
        espacio += 20 

    pygame.display.flip()
print(lista_jugadores)
pygame.quit()