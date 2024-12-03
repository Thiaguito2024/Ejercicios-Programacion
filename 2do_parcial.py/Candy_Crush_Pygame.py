import pygame 
import colores as color

pygame.init()
##################### DISEÑO LA PANTALLA ##################################
tamaño_celda = 64
columnas = 8
filas = 8
ancho_ventana = columnas * tamaño_celda
alto_ventana = filas * tamaño_celda  
pantalla = pygame.display.set_mode((ancho_ventana, alto_ventana))
############################################################################

############## CARGO IMAGENES #######################
rombo = pygame.image.load("rombo.png")
rombo = pygame.transform.scale(rombo,(80,80))

cuadrado = pygame.image.load("cuadrado.png")
cuadrado = pygame.transform.scale(cuadrado,(80,80))

circulo = pygame.image.load("circulo.png")
circulo = pygame.transform.scale(circulo,(80,80))
###################################################
pygame.display.set_caption("Candy Crush")

flag_correr = True
while flag_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False


    pantalla.fill(color.LIGHTBLUE)   
    # pygame.draw.rect(pantalla,color.RED1)
    # pantalla.blit(circulo)

    
    pygame.display.flip()   

pygame.quit()