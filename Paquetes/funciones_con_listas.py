"""
Nombre: Thiago
Apellido: LA Grotta 
Div: 213
Prof: Yanina Scudero Mariano Guevara
"""
from listas_personas import *
from opciones import *
#1
def ingreso_nombre_secuencial(lista_vacia: list)->list:
    """ 
    Pide 10 nombres y los acomoda en la lista de forma secuencial 
    """
    lista_vacia = []
    nombres_ing = 0
    
    while nombres_ing < 10:
        nombre = input("Ingrese un nombre: ")
        lista_vacia.append(nombre)
        nombres_ing += 1

    return lista_vacia

lista = []
lista = ingreso_nombre_secuencial(lista)
print("Los diez nombres ingresados son: ", lista)

#2
def agregar_num_aleatorio(numero:int, posicion:int, lista:list)->list|bool:
    """ 
    Cambia los numero que el usuario quiere, la cantidad de veces que este quiera,
    de forma aleatoria(o sea, segun quiera el usuario). 
    """
    if posicion > len(lista):
        retorno = False
    else:
        lista[posicion] = numero
        retorno = lista
    return retorno

numero = int(input("Ingrese un numero para guardar en la lista: "))
posicion = int(input("Ingrese un numero para guardar esa posicion (0-9): "))

lista = [0]*10
lista = agregar_num_aleatorio(numero, posicion, lista)

if lista == False:
    print("Posicion incorrecta")
else:
    print("La lista con los cambios realizados por el usuario es ", lista)

#3
def ingreso_num_rango(lista_vacia:list, minimo:int, maximo:int)->list: 
    """ 
    Pide 10 numeros al usuario, los valida y los agrega a una lista
    """  
    lista_vacia = []
    for i in range(0, 10+1):
        numero = int(input("Ingrese un numero: "))
        while numero < minimo or numero > maximo:
            numero = int(input("RE Ingrese un numero: "))
        lista_vacia.append(numero)
    return lista_vacia

lista = []
resultado = ingreso_num_rango(lista, 0, 100)
print("La lista con los numeros ingresados por el usuario es: ", resultado)

#4
def buscar_num(lista:list, num:int)->bool:
    """ 
    Recibe por parametro una lista y un numero y lo busca dentro de la lista ingresada 
    y devuleve true si esta y false si no esta.
    """ 
    retorno = False
    for i in range(len(lista)):
        if (lista[i] == num):
            retorno = True
        else:
            retorno = False 

        if retorno == True:
            mensaje = "El numero ingresado se encuentra en la lista"   
        else:
            mensaje = "El numero ingresado no se encuentra en la lista"
        
        return mensaje

lista = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
num = int(input("Ingrese un numero para buscar en la lista: "))
retorno = buscar_num(lista, num)
print(retorno)

#5
Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
def buscar_nombre(Nombres:list, edades:list)->str: 
    edad_min = edades[0]
    
    for i in range(len(edades)):
        if edades[i] < edad_min:
            edad_min = edades[i]
    for i in range(len(edades)):
        if edades[i] == edad_min:
            print("La/s persona/s mas joven/es es/son", Nombres[i], "y su edad es", edades[i])

buscar_nombre(Nombres, edades)

#6
def muestra_nombres(lista_vacia:list)->list:
    """ 
    muestra los nombres de la lista nombres
    """
    lista_vacia = nombres
    lista_vacia.append(nombres)
    print(lista_vacia)
lista = []
muestra_nombres(lista)

#7 
from opciones import *
nombres1 = nombres
telefonos1 = telefonos
mails1 = mails
address1 = address
postalZip1 = postalZip
region1 = region
country1 = country
edades1 = edades
def startup()->str:
    opciones = int(input("""
                        1-Importar listas
                        2-Listar los datos de los usuarios de México
                        3-Listar los nombre, mail y teléfono de los usuarios de Brasil
                        4-Listar los datos del/los usuario/s más joven/es
                        5-Obtener un promedio de edad de los usuarios
                        6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
                        7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000
                        8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.
                        9-Salir
                        
                        Ingrese un numero: """))
    return opciones
seguir = "s"
while seguir == "s":
    opcion = startup()
    if opcion == 1:
        nombres1 = nombres
        telefonos1 = telefonos
        mails1 = mails
        address1 = address
        postalZip1 = postalZip
        region1 = region
        country1 = country
        edades1 = edades
    if opcion == 2:
        usuarios_mexico(nombres1, telefonos1, mails1, address1, postalZip1, region1, country1, edades1)
    if opcion == 3:
        usuarios_brazil(nombres1, mails1, telefonos1)
    if opcion == 4:
        usuarios_jovenes(nombres1, telefonos1, mails1, address1, postalZip1, region1, country1, edades1)
    if opcion == 5:
        promedio_edad(edades1)
    if opcion == 6:
        usuarios_mayores(edades1)
    if opcion == 7:
        usuarios_mx_y_brasil(nombres1, telefonos1, mails1, address1, postalZip1, region1, country1, edades1)
    if opcion == 8:
        usuarios_italianos(nombres1, mails1, telefonos1)
    if opcion == 9:
        seguir = "n"