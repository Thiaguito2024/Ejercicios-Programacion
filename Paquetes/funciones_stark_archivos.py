from Paquetes.funciones import swap
from copy import deepcopy
import json

def menu():
    opcion = int(input("""
                       1) Leer archivo json
                       2) Ordenar Heroe
                       3) Guardar el listado ordenado en un CSV
                       4) Salir
                       Ingrese una opcion: """))
    return opcion

#1
def leer_json(nombre_archivo:str):
    with open (nombre_archivo) as file:
        data = json.load(file)
    print(data)

#2
def ordenamiento_diccionarios(lista:list, clave:str, orden:int):
    lista_heroe = deepcopy(lista)
    for i in range(len(lista_heroe)-1):
        for j in range(i+1, len(lista_heroe)):
            if orden == 1 and lista_heroe[i][clave] > lista_heroe[j][clave]:
                swap(lista,i,j)
            elif orden == -1 and lista_heroe[i][clave] < lista_heroe[j][clave]:
                swap(lista,i,j)
    return lista_heroe

#3
def generar_csv(nombre_archivo:str, lista:list):
    nombre_archivo += ".csv"
    with open(nombre_archivo, "w") as archivo:
        for e_tema in lista:
            linea = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}"
            linea = linea.format(
                        e_tema["nombre"],
                        e_tema["identidad"],
                        e_tema["empresa"],
                        e_tema["altura"],
                        e_tema["peso"],
                        e_tema["genero"],
                        e_tema["color_ojos"],
                        e_tema["color_pelo"],
                        e_tema["fuerza"],
                        e_tema["inteligencia"])
            archivo.write(linea + "\n")