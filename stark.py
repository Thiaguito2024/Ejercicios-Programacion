from funciones_stark import *

seguir = "si"

while seguir == "si":
    opciones = menu()
    if opciones == 1:
        ordenamiento_diccionarios(lista_personajes, "nombre", 1)
    elif opciones == 2:
        maximo_minimo_diccionario(lista_personajes, "fuerza", "Minimo")
    elif opciones == 3:
        pass
    elif opciones == 4:
        pass
    elif opciones == 5:
        pass
    elif opciones == 6:
        pass
    elif opciones == 7:
        pass
    elif opciones == 8:
        seguir = "no"
    else:
        print("Opcion invalida")