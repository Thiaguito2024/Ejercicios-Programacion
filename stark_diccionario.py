from Paquetes.funciones_stark import *

seguir = "si"
######################################## REHACER TODOS LOS PUNTOS CON UN FILTER #################################################33
while seguir == "si":
    opciones = menu()
    if opciones == 1:
        ordenamiento_diccionarios(lista_personajes, "nombre", 1)
    elif opciones == 2:
        maximo_minimo_diccionario(lista_personajes, "fuerza", "Minimo") 
    elif opciones == 3:
        listar_cant_color_ojos(lista_personajes)
    elif opciones == 4:
        listar_cant_color_pelo(lista_personajes)
    elif opciones == 5:
        listar_tipo_inteligencia(lista_personajes)
    elif opciones == 6:
        pass
    elif opciones == 7:
        pass
    elif opciones == 8:
        seguir = "no"
    else:
        print("Opcion invalida")