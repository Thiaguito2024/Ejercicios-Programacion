from funciones import swap
#1 
def invertir_cadena(cadena:str) -> str:
    """
    Invierte la cadena pasada por parametro
    """
    length = len(cadena)
    aux = ""
    for i in range(length):
        aux += cadena[length - i - 1] 
    return aux

cadena = input("Ingrese una frase: ")

while cadena.isalpha() == False:
    cadena = input("Ingrese una frase (No numeros): ")
retorno = invertir_cadena(cadena)
print(retorno)

#2 
def contar_palabras(cadena:str) -> int:
    """
    Cuenta las palabras de la cadena pasada por parametro
    """
    palabras = cadena.split()
    return len(palabras)

cadena = input("Ingrese una frase: ")

while cadena.isalpha() == False:
    cadena = input("Ingrese una frase (No numeros): ")
numero_palabras = contar_palabras(cadena)
print(numero_palabras)

#3
def reemplaza_palabras(cadena:str, palabra_a_reemplazar:str, palabra:str):
    """
    Reemplaza una palabra que el usuario quiera de la cadena pasada por parametro
    """
    return cadena.replace(palabra_a_reemplazar, palabra) 

cadena = input("Ingrese una frase: ")

while cadena.isalpha() == False:
    cadena = input("Ingrese una frase (No numeros): ")

palabra_1 = input("Ingrese palabra a reemplazar: ")
palabra_2 = input("Ingrese la palabra nueva")

cadena_nueva = reemplaza_palabras(cadena, palabra_1, palabra_2)
print(cadena_nueva)

#4
def recomendar_peliculas(lista_peli):
    for lista in lista_peli:
        peliculas = ', '.join(lista[:-1])
        recomendacion = f'Se recomienda ver "{peliculas}" y "{lista[-1]}"'
        print(recomendacion)


lista_peli = [
    ["Matrix", "El Padrino", "Titanic"],
    ["Forrest Gump", "Pulp Fiction", "Gladiador"],
    ["Blade Runner", "El Rey León", "Volver al Futuro"],
    ["La La Land", "El Gran Lebowski", "Blade Runner"],
    ["Jurassic Park", "Avatar", "El Resplandor", "El Sexto Sentido"],
    ["Harry Potter", "Forrest Gump", "Pulp Fiction"],
    ["Titanic", "Star Wars", "El Señor de los Anillos"],
    ["The Truman Show", "The Shape of Water", "The Big Lebowski"],
    ["Forrest Gump", "The Godfather", "Goodfellas"],
    ["The Terminator", "The Sixth Sense", "The Great Gatsby"]
]

recomendar_peliculas(lista_peli)

#5
def mayusculas(cadena:str):
    """
    Pasa a mayuscula la primer letra de la cadena pasada por parametro
    """
    return cadena.capitalize()

cadena = input("Ingrese una cadena para poner la primer letra en mayuscula: ")

retorno = mayusculas(cadena)
print(retorno)

#6
def palindromo(cadena:str) -> bool:
    """
    Verifica que la cadena pasada por parametro sea un palidromo, que se igual de izquierda a derecha
    que de derecha a izquierda
    """
    palindromo = False
    
    if cadena == cadena[::-1]:
        palindromo = True
    
    return palindromo

cadena = input("Ingrese una palabra para saber si es palindromo o no: ")

if palindromo(cadena) == True:
    print("Es palindromo")
else:
    print("No es palindromo")

#7 
def ordenado(cadena:str, numero:int)-> list:
    """
    Ordena la cadena pasada por parametro de mayor a menor o menor a mayor 
    segun lo quiera el usuario
    """
    lista_cadena = []
    for letra in range(len(cadena)):
        lista_cadena.append(cadena[letra])
    
    for i in range(len(lista_cadena)-1):
        for j in range(i+1,len(lista_cadena)):
            if numero == 1 and lista_cadena[i] > lista_cadena[j]:
                swap(lista_cadena,i,j)
            elif numero == -1 and lista_cadena[i] < lista_cadena[j]:
                swap(lista_cadena,i,j)
    return lista_cadena



cadena = input("Ingrese una frase: ")

while cadena.isalpha() == False:
    cadena = input("Ingrese una frase (No numeros): ")

numero = int(input("Ingrese un numero para ordenar de manera ascendente(1) o descendente(-1): "))

while numero > 1 or numero < -1:
    numero = int(input("Ingrese un numero para ordenar de manera ascendente(1) o descendente(-1): "))

cadena_ordenada = ordenado(cadena, numero)
print(cadena_ordenada)