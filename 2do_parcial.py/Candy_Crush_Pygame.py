import pygame
from colores import * 
from funciones_candy_pygame import * 
pygame.init()
############################### CREO PANTALLA ###########################
ancho_ventana = 800
alto_ventana = 600
pantalla = pygame.display.set_mode((ancho_ventana,alto_ventana))
pygame.display.set_caption("Candy Crush")
########################################################################
 
corriendo = True
lista = [
{"piezas":[]},
{"piezas":[]},
{"piezas":[]},
{"piezas":[]}]
lista_puntaje = []
separador = ", "
puntos = 0
reloj = pygame.time.Clock()
input_rect = pygame.Rect(300,400,400,75)
play_rect = pygame.Rect(300,300,300,75)
scoreboard_rect = pygame.Rect(10,100,250,400)
scoreboard_inactivo = RED1
scoreboard_activo = GREEN1
color_input = scoreboard_inactivo
active = False # Bandera input 
nombre = "Ingrese su nombre: " # Texto input
tipo_letra = pygame.font.Font(None,36) # Fuente 
tipo_letra_scoreboard = pygame.font.Font(None,30) # Fuente scoreboard
# imagen_fondo_general = pygame.image.load("fondo_candy_3.png")
# imagen_fondo_general = pygame.transform.scale(imagen_fondo_general,(800,800))

while corriendo:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            corriendo = False
            
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(evento.pos):
                active = True
            else:
                active = False
        
            if play_rect.collidepoint(evento.pos):
                imagen_fondo = pygame.image.load("fondo_candy_crush_1.png")
                pantalla.blit(imagen_fondo, (0, 0))
                puntos = juego_principal(pantalla)
                
        if evento.type == pygame.KEYDOWN and active:
                if evento.key == pygame.K_BACKSPACE: # Si presiona el DELETE, borra
                    nombre = nombre[:-1]
                elif evento.key == pygame.K_RETURN: #Si presiona enter, arranca el nuevo juego
                    puntos = juego_principal(pantalla)
                else: # Si presiona una tecla de texto, lo introduce a la cadena 
                    nombre += evento.unicode 
                    
    puntaje = separador.join([nombre, str(puntos)])
    lista_puntaje.append(puntaje)
    
    pantalla.fill(LIGHTBLUE)
    # pantalla.blit(imagen_fondo_general, (100, 100))
    color_input = scoreboard_activo if active else scoreboard_inactivo
    pygame.draw.rect(pantalla, color_input, input_rect) 
    pygame.draw.rect(pantalla, colores.WHEAT, play_rect)
    pygame.draw.rect(pantalla, colores.BLACK, scoreboard_rect)
    scoreboard_texto = tipo_letra.render("SCOREBOARD", True, colores.RED1) # Titulo de Scoreboard
    play_texto = tipo_letra.render("PLAY",True, colores.GREEN) # Texto de boton PLAY
    texto_renderizado = tipo_letra.render(nombre, True, (0, 0, 0)) # Texto de input
    # Bliteo en pantalla de los textos 
    # pantalla.blit(imagen_fondo,(0,0))
    pantalla.blit(texto_renderizado, (input_rect.x + 10, input_rect.y + 20)) 
    pantalla.blit(play_texto, (play_rect.x+120, play_rect.y+25))
    pantalla.blit(scoreboard_texto, (scoreboard_rect.x+15, scoreboard_rect.y))
    espacio = 30
    lista_scoreboard = obtener_scoreboard() #Scoreboard
    # Recorrido de la lista con el FOR
    for persona in lista_scoreboard:
        cadena_separada = persona.split(",") # Separo cada linea de la lista, con "," 
        pantalla.blit(tipo_letra.render(f"{cadena_separada[0]}", True, colores.GREEN),(scoreboard_rect.x, scoreboard_rect.y+espacio)) # Bliteo el nombre 
        pantalla.blit(tipo_letra.render(f"{cadena_separada[1][:-1]}", True, colores.GREEN),(scoreboard_rect.x+150, scoreboard_rect.y+espacio) ) # Bliteo el puntaje
        espacio += 20 # Sumo 20 de espacio para que no se junten todos
    
    reloj.tick(30)
    pygame.display.flip()
    
pygame.quit()

#Falta resolver puntaje y tiempo