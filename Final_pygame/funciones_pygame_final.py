import pygame
import random
import colores

def generar_matriz(lista:list, cant_columnas:int):
    """
    Genera una matriz con la lista y cantidad de columnas pasadas por el usuario
    """
    for i in range(len(lista)):
        for j in range(cant_columnas):
            numero = random.randint(1,3)
            lista[i]["piezas"].append(numero)

def generar_csv(nombre_archivo: str, lista: list):
    """
    Recibe una lista y genera un archivo CSV con los datos de la lista
    separados por comas en una sola línea, sin usar map.
    """
    nombre_archivo += ".csv"
    contenido = ", ".join(str(elemento) for elemento in lista)

    with open(nombre_archivo, "a") as archivo:
            archivo.write(contenido + "\n")

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
    # IMAGENES 
    caramelo_azul = pygame.image.load("caramelo_azul.png")
    caramelo_azul = pygame.transform.scale(caramelo_azul,(100,100))
    caramelo_rojo = pygame.image.load("caramelo_rojo.png")
    caramelo_rojo = pygame.transform.scale(caramelo_rojo,(100,100))
    caramelo_verde = pygame.image.load("caramelo_verde.png")
    caramelo_verde = pygame.transform.scale(caramelo_verde,(100,100))
    # RECT
    tamaño_celda = 100
    fila = 4
    columna = 7
    rect_caramelos = pygame.Rect(fila, columna, tamaño_celda * fila, tamaño_celda * columna)
    # TIMER
    puntos = 0
    segundos_para_jugar = "10"
    pos_timer = (100, 100)
    # SONIDO 
    pygame.mixer.init()
    sonido_fondo = pygame.mixer.Sound("y2mate.mp3")
    volumen = 0.10
    sonido_fondo.set_volume(volumen)
    # CONSTANTES
    fuente = pygame.font.SysFont("Arial", 50)
    fin_del_tiempo = False
    cronometro = pygame.USEREVENT
    pygame.time.set_timer(cronometro, 1000) # 1000 milisegundos = 1 segundo
    lista = [
        {"piezas":[]},
        {"piezas":[]},
        {"piezas":[]},
        {"piezas":[]}]
    generar_matriz(lista, 7)

    while not (fin_del_tiempo):
        sonido_fondo.play()
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                fin_del_tiempo = True
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                print("click", evento.pos)
                coordenada_x = (evento.pos[0] - 50) // 100  # Restamos margen izquierdo
                coordenada_y = (evento.pos[1] - 150) // 100  # Restamos margen superior
                print("x", coordenada_x, "y", coordenada_y)
                puntaje = verificar_combinacion(lista, coordenada_y, coordenada_x, "piezas")
                
                if puntaje == 10:
                    print("¡Ganaste 10 puntos!")
                    lista = [
                        {"piezas":[]},
                        {"piezas":[]},
                        {"piezas":[]},
                        {"piezas":[]}]
                    generar_matriz(lista, 7)
                    puntos += 10

                elif puntaje == -1:
                    print("Sigue participando")
                    lista = [
                        {"piezas":[]},
                        {"piezas":[]},
                        {"piezas":[]},
                        {"piezas":[]}]
                    generar_matriz(lista, 7)
                    segundos_para_jugar = int(segundos_para_jugar) - 1
                    volumen = volumen - 0.01
                    sonido_fondo.set_volume(volumen)
                    puntos -= 1
                pygame.display.flip()

            if evento.type == pygame.USEREVENT:
                if evento.type == cronometro:
                    if fin_del_tiempo == False:
                        segundos_para_jugar = int(segundos_para_jugar) -1
                        volumen = volumen - 0.01
                        sonido_fondo.set_volume(volumen)
                    if segundos_para_jugar <= 0:
                        sonido_fondo.stop()
                        fin_del_tiempo = True
                        return puntos

        pantalla.fill(colores.LIGHTBLUE) # Vuelvo a pintar la pantalla de un color para que no se vean los numeros anteriores
        imprimir_caramelos(lista, pantalla, caramelo_azul, caramelo_rojo, caramelo_verde)
        segundos_texto = fuente.render(str(segundos_para_jugar), True, colores.WHITE)
        pantalla.blit(segundos_texto, pos_timer)
        pygame.display.flip()
    sonido_fondo.stop()

        
def imprimir_caramelos(lista, screen, caramelo_rojo, caramelo_azul, caramelo_verde):
    """
    Imprime caramelos en la pantalla
    """
    tamaño_celda = 100
    fila = 4
    columna = 7
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