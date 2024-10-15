"""
Thiago La Grotta
213
Yanina escudero, Mariano Guevara
"""
# Punto 1
from funciones import *
"Ejercicio 1: El almacén de barrio nos pide un programa para almacenar, ordenar y controlar stock de su mercadería por día."
stock = [
    [["caramelo", 10, [1, 1]],["Botellas", 3,[1, 2]],[],["Frascos", 8,[1, 4]],[]],      
    [[],[],["Fideos", 4,[2, 3]],[],[]],
    [[],[],[],["Leche", 6,[3, 4]],[]]
]
# corchete violeta = fila, corchete azul = columna


def menu_almacenes():
        opciones = int(input(""" 
                            1-Alta de productos (producto nuevo)
                            2-Baja de productos (producto existente)
                            3-Modificar productos (cantidad, ubicación)
                            4-Listar productos
                            5-Lista de productos ordenado por nombre
                            6-Salir
                            
                            Ingrese un numero: """))   
        return opciones

seguir = "s"
while seguir == "s":      
    opcion = menu_almacenes()
    if opcion == 1:
        alta_productos(stock)
    elif opcion == 2: 
        baja_productos(stock)
    elif opcion == 3:
        modificar_producto(stock)
    elif opcion == 4: 
        listar_productos(stock)
    elif opcion == 5:
        lista_ordenado(stock)
    elif opcion == 6:
        seguir = "n"
    else:
        print("Numero ingresado incorrecto")   


# Punto 2
stock = [["to12", 65], ["to30", 68], ["to16", 86], ["to35", 73],
        ["to20", 65], ["to40", 85], ["to25", 45], ["to45", 89],
        ["ta4", 58], ["ta5", 48], ["ta6", 64], ["ta7", 96],
        ["ta8", 36], ["ta10", 72], ["ta12", 78], ["ta14", 71]]

def reponer(lista:list):
    cantidad = int(input("Ingrese la cantidad de producto que desea reponer: "))
    while cantidad <= 0 or cantidad > 100:
        cantidad = int(input("Ingrese la cantidad de producto que desea reponer: "))
    
    fila = int(input("Ingrese la fila del producto a reponer: "))
    while fila < 0 or fila > 4:
        fila = int(input("Ingrese la fila del producto a reponer: "))
    
    lista[fila][1] += cantidad
    for i in range(len(lista)):
        print(lista[i])
            
reponer(stock)