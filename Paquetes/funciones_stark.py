from data_stark import lista_personajes
from funciones import swap
def menu():
    opciones = int(input(""" 
                1- Listar ordenado por nombre
                2- Listar masculinos debiles
                3- Cantidad por color de ojos
                4- Listar por color de pelo
                5- Listar por inteligencia
                6- Listar promedio 
                7- Asignar IMC
                8- Salir
                
                Ingrese una opcion: """))
    return opciones

def mostrar(mensaje:str):
    print(mensaje)

#1
def ordenamiento_diccionarios(lista:list, clave:str, orden:int):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if orden == 1 and lista[i][clave] > lista[j][clave]:
                swap(lista,i,j)
            elif orden == -1 and lista[i][clave] < lista[j][clave]:
                swap(lista,i,j) 
    for i in range(len(lista)):
        print(lista[i])

#2
def maximo_minimo_diccionario(lista:list, clave:str, accion:str)->dict:
    """
    Obtiene maximo o minimo segun lo requiera el usuario y lo devuelve
    """
    min_max = lista[0]
    for i in range(1, len(lista)):
        if accion == "Maximo" and int(lista[i][clave]) > int(min_max[clave]):
            min_max = lista[i]
        if accion == "Minimo" and int(lista[i][clave]) < int(min_max[clave]):
            min_max = lista[i]
    
    return min_max

#3 
def listar_cant_color_ojos(lista:list):
    cont_Brown = 0
    cont_Blue = 0
    cont_Green = 0
    cont_Yellow_without_irises = 0
    cont_Hazel = 0
    cont_Yellow = 0
    cont_Silver = 0
    cont_Red = 0
    
    for i in range(len(lista)):
        if lista[i]["color_ojos"] == "Brown":
            cont_Brown +=1
        elif lista[i]["color_ojos"] == "Green":
            cont_Green +=1
        elif lista[i]["color_ojos"] == "Hazel":
            cont_Hazel +=1
        elif lista[i]["color_ojos"] == "Red":
            cont_Red +=1
        elif lista[i]["color_ojos"] == "Silver":
            cont_Silver +=1
        elif lista[i]["color_ojos"] == "Yellow":
            cont_Yellow +=1
        elif lista[i]["color_ojos"] == "Yellow (without irises)":
            cont_Yellow_without_irises +=1
        elif lista[i]["color_ojos"] == "Blue" or lista[i]["color_ojos"] == "blue":
            cont_Blue +=1
    
    print(f"La cantidad de superheroes con el color de ojos rojos es {cont_Red}")
    print(f"La cantidad de superheroes con el color de ojos azules es {cont_Blue}")
    print(f"La cantidad de superheroes con el color de ojos marrones  es {cont_Brown}")
    print(f"La cantidad de superheroes con el color de ojos amarillos es {cont_Yellow}")
    print(f"La cantidad de superheroes con el color de ojos amarillos sin iris es {cont_Yellow_without_irises}")
    print(f"La cantidad de superheroes con el color de ojos plata es {cont_Silver}")
    print(f"La cantidad de superheroes con el color de ojos Hazel es {cont_Hazel}")
    print(f"La cantidad de superheroes con el color de ojos verdes es {cont_Green}")

#4
def listar_cant_color_pelo(lista:list):
    cont_Blond = 0
    cont_Black = 0
    cont_no_hair = 0
    cont_Auburn = 0
    cont_Brown_White = 0
    cont_Red_Orange = 0
    cont_White = 0
    cont_Green = 0
    
    for i in range(len(lista)):
        if lista[i]["color_pelo"] == "Blond" or lista[i]["color_pelo"] == "blond":
            cont_Blond +=1
        elif lista[i]["color_pelo"] == "No Hair":
            cont_no_hair +=1
        elif lista[i]["color_pelo"] == "Brown / White":
            cont_Brown_White +=1
        elif lista[i]["color_pelo"] == "Green":
            cont_Green +=1
        elif lista[i]["color_pelo"] == "White":
            cont_White +=1
        elif lista[i]["color_pelo"] == "Red / Orange":
            cont_Red_Orange +=1
        elif lista[i]["color_pelo"] == "Auburn":
            cont_Auburn +=1
        elif lista[i]["color_pelo"] == "Black":
            cont_Black +=1
    
    print(f"La cantidad de superheroes con el color de pelo verde es {cont_Green}")
    print(f"La cantidad de superheroes con el color de pelo negro es {cont_Black}")
    print(f"La cantidad de superheroes con el color de pelo rubio es {cont_Blond}")
    print(f"La cantidad de superheroes con el color de pelo rojo/naranja es {cont_Red_Orange}")
    print(f"La cantidad de superheroes con el color de pelo auburn {cont_Auburn}")
    print(f"La cantidad de superheroes con el color de pelo blanco es {cont_White}")
    print(f"La cantidad de superheroes con el color de pelo marron/blanco es {cont_Brown_White}")
    print(f"La cantidad de superheroes sin pelo son {cont_no_hair}")

#5
def listar_tipo_inteligencia(lista:list):
    cont_high = 0
    cont_good = 0
    cont_average = 0
    cont_desconocido = 0
    
    for i in range(len(lista)):
        if lista[i]["inteligencia"] == "good":
            cont_good +=1
        elif lista[i]["inteligencia"] == "average":
            cont_average += 1
        elif lista[i]["inteligencia"] == "high": 
            cont_high += 1
        else:
            cont_desconocido += 1
    print(f"La cantidad de superheroes cuyo tipo de inteligencia es average es: {cont_average}")
    print(f"La cantidad de superheroes cuyo tipo de inteligencia es high es: {cont_high}")
    print(f"La cantidad de superheroes cuyo tipo de inteligencia es good es: {cont_good}")
    print(f"La cantidad de superheroes de los cuales no sabemos su inteligencia es: {cont_desconocido}")
