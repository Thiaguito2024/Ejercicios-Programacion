from estudiantes import *
from funciones import swap
def menu():
    opciones = int(input(""" 
                1-Listar los alumnos por orden ascendente de apellido, si se repite, ordenar por nombre. 
                Mostrar legajo, nombre, apellido y edad
                2-2
                3-Listar legajo, nombre, apellido y edad de los estudiantes que cursan el programa de “Ingenieria en Informatica”
                4-Obtener un promedio de edad de los estudiantes. Mostrar nombre y apellido
                5-Informar el alumno con mayor pomedio de notas. Mostrar nombre y apellido
                6-Listar nombre y apellido de los alumnos que forman el grupo “Club de
                Informática” con sus respectivos promedios
                7-Listar legajo, nombre, apellido y programas que cursan los alumnos más jóvenes.
                8- Salir
                
                Ingrese una opcion: """))
    return opciones

def mostrar(mensaje:str)->str:
    print(mensaje)

def preguntar():
    accion = input("Ingrese la accion a realizar: ")
    while accion != "Promedio" and accion != "Mayor" or accion.isalpha() == False:
        accion = input("Ingrese la accion a realizar(Promedio o Mayor): ")
    return accion

def mostrar_lista(lista:list, lista2:list):
    for i in range(len(lista)):
        print(f"Este el promedio de notas de {lista[i]["nombre"]} apellido {lista[i]["apellido"]} legajo {lista[i]["legajo"]} es: {lista2[i]}")

#1
def ordenamiento(estudiantes)->str:
    for i in range(len(estudiantes)-1):
        for j in range(i+1, len(estudiantes)):
            if estudiantes[i]["apellido"] > estudiantes[j]["apellido"]:
                swap(estudiantes, i, j)
            elif estudiantes[i]["apellido"] == estudiantes[j]["apellido"]:
                if estudiantes[i]["nombre"] > estudiantes[j]["nombre"]:
                    swap(estudiantes, i, j)
    for e in range(len(estudiantes)):
        mensaje = f"Legajo: {estudiantes[e]['legajo']}, Nombre: {estudiantes[e]['nombre']}, Apellido: {estudiantes[e]['apellido']}, Edad: {estudiantes[e]['edad']}"
        mostrar(mensaje)

#2 a 5 
def calcular_promedios(estudiantes) -> None:
    acumulador = 0
    contador_notas = 0
    promedios = []
    for i in range(len(estudiantes)):
        for j in range(len(estudiantes[i]["notas"])):
            acumulador += estudiantes[i]["notas"][j]
            contador_notas += 1 
        promedio = acumulador / contador_notas
        promedios.append(promedio)
    return promedios   

def calcular_mayor_promedio(estudiantes):
    promedios = calcular_promedios(estudiantes)
    mayor_promedio = promedios[0]
    indice_mayor = 0

    for i in range(1, len(promedios)):
        if promedios[i] > mayor_promedio:
            mayor_promedio = promedios[i]
            indice_mayor = i
    estudiante = estudiantes[indice_mayor]
    mensaje = f"El mayor promedio de notas es de {estudiante["nombre"]} {estudiante["apellido"]} y tiene {mayor_promedio}"
    mostrar(mensaje)

#3
def programa(estudiantes)-> str:
    for i in range(len(estudiantes)):
        if estudiantes[i]["programa"]["nombre"] == "Ingenieria en Informatica": 
            mensaje = f"Legajo: {estudiantes[i]['legajo']}, Nombre: {estudiantes[i]['nombre']}, Apellido: {estudiantes[i]['apellido']}, Edad: {estudiantes[i]['edad']}"
            mostrar(mensaje)

#4
def promedio_edad(estudiantes)->str:
    suma_edades = 0
    for i in range(len(estudiantes)):
        suma_edades += estudiantes[i]["edad"]
    
    promedio = suma_edades / len(estudiantes)
    mensaje = f"El promedio de edades es: {promedio}"
    mostrar(mensaje)

#5
def mostrar_promedios(estudiantes:list):
    promedio = calcular_promedios(estudiantes)
    accion = preguntar()
    if accion == "Promedio":  
        mostrar_lista(estudiantes, promedio)
    elif accion == "Mayor":
        calcular_mayor_promedio(estudiantes)

#6 
def obtener_grupo(estudiantes: list) -> str:
    promedio = calcular_promedios(estudiantes)
    for i in range(len(estudiantes)):
        if "grupos" in estudiantes[i]:
            for j in range(len(estudiantes[i]["grupos"])):
                if estudiantes[i]["grupos"][j].get("nombre") == "Club de Informatica": 
                    mensaje = f"Legajo: {estudiantes[i]['legajo']}, Nombre: {estudiantes[i]['nombre']}, Apellido: {estudiantes[i]['apellido']}, su promedio es {promedio[i]}"
                    mostrar(mensaje)

#7
def listar_alumnos_mas_jovenes(estudiantes: list):
    edad_minima = estudiantes[0]["edad"]
    for estudiante in estudiantes:
        if estudiante["edad"] < edad_minima:
            edad_minima = estudiante["edad"]

    for estudiante in estudiantes:
        if estudiante["edad"] == edad_minima:
            legajo = estudiante["legajo"]
            nombre = estudiante["nombre"]
            apellido = estudiante["apellido"]
            mensaje = f"Legajo: {legajo}, Nombre: {nombre}, Apellido: {apellido}"
            mostrar(mensaje)
