import pygame
import random
import colores

def inicializar_matriz():
    lista = [
        {"piezas":[]},
        {"piezas":[]},
        {"piezas":[]},
        {"piezas":[]}]
    
    return lista

# def generar_csv(nombre_archivo:str, lista:list):
#     """
#     Recibe una lista y genera un archivo csv con los datos de la lista
#     """
#     nombre_archivo += ".csv"
#     try:
#         with open(nombre_archivo, "a") as archivo: 
#             for e_tema in lista:
#                 archivo.write(f"{e_tema}\n")
                
#     except FileNotFoundError:
#         with open(nombre_archivo, "w") as archivo: 
#             for e_tema in lista:
#                 archivo.write(f"{e_tema}\n") 
    
#     return archivo
    
def obtener_scoreboard():
    try:
        with open("scoreboard.csv", "r+") as archivo:
            scoreboard = archivo.readlines()
            
    except FileNotFoundError:
        with open("scoreboard.csv", "w") as archivo:
            archivo.write("Nombre, Puntos\n")
            scoreboard = []
            
    return scoreboard
                
def generar_matriz(lista:list, cant_columnas:int):
    """
    Genera una matriz con la lista y cantidad de columnas pasadas por el usuario
    """
    for i in range(len(lista)):
        for j in range(cant_columnas):
            numero = random.randint(1,3)
            lista[i]["piezas"].append(numero)
            
def verificar_combinacion(grilla, fila, columna, clave):
    """
    Verifica si dos filas para abajo o para arriba hay dos caramelos iguales
    """
    num_seleccionado = grilla[fila][clave][columna]
    retorno = -1

    if fila <= len(grilla) - 3: # Verifica si hay espacio suficiente hacia abajo
        if (grilla[fila + 1][clave][columna] == num_seleccionado and grilla[fila + 2][clave][columna] == num_seleccionado):
            retorno = 10

    
    if fila >= 2: # Verifica si hay espacio suficiente hacia arriba
        if (grilla[fila - 1][clave][columna] == num_seleccionado and grilla[fila - 2][clave][columna] == num_seleccionado):
            retorno = 10

    return retorno

def juego_principal(pantalla):
    tamaño_celda = 100
    fila = 4
    columna = 7

    caramelo_azul = pygame.image.load("caramelo_azul.png")
    caramelo_azul = pygame.transform.scale(caramelo_azul,(100,100))
    caramelo_rojo = pygame.image.load("caramelo_rojo.png")
    caramelo_rojo = pygame.transform.scale(caramelo_rojo,(100,100))
    caramelo_verde = pygame.image.load("caramelo_verde.png")
    caramelo_verde = pygame.transform.scale(caramelo_verde,(100,100))
    rect_caramelos = pygame.Rect(0, 0, 400, 600)
    
    fuente = pygame.font.Font(None, 36)
    puntos = 0
    fin_del_juego = False
    segundos_para_jugar = 11
    cronometro = pygame.USEREVENT
    pygame.time.set_timer(cronometro, 1000) # 1000 milisegundos equivalen a 1 segundo
    lista = [
        {"piezas":[]},
        {"piezas":[]},
        {"piezas":[]},
        {"piezas":[]}]
    generar_matriz(lista, 7)
    # Bucle principal
    while not (fin_del_juego):
        lista_eventos = pygame.event.get() # Me guardo los eventos
        for evento in lista_eventos:
            if evento.type == pygame.QUIT: # Si el usuario preciona la cruz para cerrar el juego, se rompe el bucle
                fin_del_juego = True
                
            if evento.type == pygame.MOUSEBUTTONDOWN: # Si el usuario hizo click
                print("Clic detectado en posición:", evento.pos)
                coordenada_x = int(round(evento.pos[0] / 100,0)-1)
                coordenada_y = int(round((evento.pos[1]-100) / 100,0)-1)
                print("Índices calculados: x =", coordenada_x, "y =", coordenada_y)
                
                if rect_caramelos.collidepoint(evento.pos):
                    print("Rect caramelos")
                    # contador_arriba = recorrer_lista_diccionarios(lista, x, "piezas", y, 1)
                    # contador_abajo = recorrer_lista_diccionarios(lista, x, "piezas", y, -1)
                    puntaje = verificar_combinacion(lista, coordenada_x, coordenada_y, "piezas")
                    print(evento.pos)
                    
                    if puntaje == 10:
                            print("Tiene 10 puntos ")
                            lista = [
                                {"piezas":[]},
                                {"piezas":[]},
                                {"piezas":[]},
                                {"piezas":[]}]  
                            generar_matriz(lista, 7)
                            puntos += 10
                            
                    elif puntaje == -1:
                            print("No tiene 10 puntos")
                            lista = [
                                {"piezas":[]},
                                {"piezas":[]},
                                {"piezas":[]},
                                {"piezas":[]}]
                            generar_matriz(lista, 7)
                            segundos_para_jugar = segundos_para_jugar -1
                            puntos += 0
                            
                    pygame.display.flip()            
                                        
        if evento.type == pygame.USEREVENT: # Si hay un evento del usuario
                if evento.type == cronometro: # Si el userevent corresponde al cronometro
                    if fin_del_juego == False: # Si no se llego al fin del tiempo, se resta 1 segundo
                        segundos_para_jugar = segundos_para_jugar -1
                        if segundos_para_jugar <= 0: 
                            fin_del_juego = True # Pongo la bandera en true para que rompa el bucle 
                            return puntos 
        cronometro_texto = fuente.render(str(segundos_para_jugar), True, "green") # Texto de el cronometro
        pantalla.blit(cronometro_texto, (100,20)) # Blit del texto de el cronometro
        imprimir_caramelos(lista,pantalla, caramelo_rojo,caramelo_azul,caramelo_verde) 
        pygame.display.flip() # Actualizo

def imprimir_caramelos(lista, screen, caramelo_rojo, caramelo_azul, caramelo_verde):
    """
    Imprime caramelos en la pantalla
    """
    tamaño_celda = 64
    fila = 8
    columna = 8
    rect_caramelos = pygame.Rect(fila, columna, tamaño_celda * fila, tamaño_celda * columna)
    coordenadas_fila = 150 # Ubicacion de la primera fila
    for e_dict in lista:
        coordenadas_columna = 50 # Ubicacion de la primera columna
        for caramelo in e_dict["piezas"]:
            if caramelo == 1: 
                # pygame.draw.rect(screen, colores.BLUE,rect_caramelos)
                screen.blit(caramelo_rojo, (coordenadas_columna, coordenadas_fila), rect_caramelos)
            elif caramelo == 2:
                # pygame.draw.rect(screen, colores.BLUE,rect_caramelos)
                screen.blit(caramelo_azul, (coordenadas_columna, coordenadas_fila), rect_caramelos)
            elif caramelo == 3:
                # pygame.draw.rect(screen, colores.BLUE,rect_caramelos)
                screen.blit(caramelo_verde, (coordenadas_columna, coordenadas_fila), rect_caramelos)
            
            coordenadas_columna += 100 # Se le suma 100 a la coordenada para que no esten pegados
            if coordenadas_columna >= 700: # Cuando llega a 700, empieza de nuevo
                coordenadas_columna = 100
        if coordenadas_fila >= 400: # Cuando llega a 400, empieza de nuevo
            coordenadas_fila = 150
        coordenadas_fila += 100 # Con cada fila, se suma 100 a la coordenada, para que no esten pegadas