from Paquetes.funciones_stark_archivos import *
from data_stark import *

seguir = "si"

while seguir == "si":
    opcion = menu()
    if opcion == 1:
        try:
            leer_json(input("Ingrese nombre de archivo: ")) # EJEMPLO: C:\Users\thiag\Desktop\UTN\Programacion I/data.json
        except FileNotFoundError:
            print("El archivo no existe")            
    elif opcion == 2:
        ordenamiento_diccionarios(lista_personajes, input("Por cual clave quiere buscar: "), 1)
    elif opcion == 3:
        generar_csv(input("Ingrese el nombre que le va a poner al archivo: "), lista_personajes)
    elif opcion == 4:
        seguir = "no"
    else:
        print("opcion incorrecta")