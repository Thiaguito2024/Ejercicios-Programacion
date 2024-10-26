#1 
def invertir(cadena: str) -> str:
    length = len(cadena)
    aux = ""
    for i in range(length):
        aux += cadena[length - i - 1] 
    return aux

cadena = "hola"

reotrno = invertir(cadena)
print(reotrno)

#2 
def contar_palabras(cadena: str) -> int:
    palabras = cadena.split()
    return len(palabras)

cadena = "Hola, ¿cómo estás?"
numero_palabras = contar_palabras(cadena)
print(numero_palabras)

#3
def reemplaza_palabras(cadena:str, palabra_a_reemplazar:str, palabra:str):
    return cadena.replace(palabra_a_reemplazar, palabra) 

cadena = "hola mundo"
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
    return cadena.capitalize()

cadena = input("Ingrese una cadena para poner la primer letra en mayuscula: ")
# while cadena.isalpha() == False:
#     cadena = input("Reingrese una cadena para poner la primer letra en mayuscula: ")
retorno = mayusculas(cadena)
print(retorno)

#6
