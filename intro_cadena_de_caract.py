"""
Ejercicio 1: Desarrollar una función que reciba una letra y una cadena.
Debe retornar las veces que la letra está incluida en el texto.
"""
def cuenta_letras(letra:str, cadena:str):
    cont = 0
    while letra not in cadena: 
      letra = input("Reingrese una letra para buscar en el texto: ")
      
    for i in cadena:
        if i == letra:
            cont += 1
    print(f"La cantidad de veces que aparece la letra: {letra} en el texto: {msj}, es: {cont}")

msj = "mensaje para ver si funciona este codigo"
letra = input("Ingrese una letra para buscar en el texto: ")

letra_cadena = cuenta_letras(letra, msj)

"""
Ejercicio 2: Desarrollar una función que reciba una cadena y dos índices.
Se debe retornar la cadena que va entre las posiciones indicadas por los índices.
Si las posiciones no son válidas se debe informar.
"""
def subcadena_indice(cadena:str, inicio:int, fin:int):  
    while inicio < 0 or fin > len(cadena) or inicio > fin:
        print("Los indices son invalidos")
        inicio = int(input("Reingrese un indice de inicio: "))
        fin = int(input("Reingrese un indice de final: "))
    return cadena[inicio:fin+1]

msj = "hola como estas"
inicio = int(input("Ingrese un numero de inicio: "))
fin = int(input("Ingrese un indice de final: "))
cadena = subcadena_indice(msj, inicio, fin)
print(cadena)

"""
Ejercicio 3: Desarrollar una función “char_at” que recibe una cadena y un número.
Se debe retornar el caracter en la posición indicada por el número si ésta es válida.
"""
def char_at(cadena:str, indice:int)->str:
    while indice < 0 or indice > len(cadena):
        print("Indice invalido")
        indice = int(input("Reingrese un indice: "))
    else: 
        return cadena[indice-1]

msj = "hola mundo"
indice = int(input("Ingrese un indice: "))
cadena = char_at(msj, indice)
print(cadena)