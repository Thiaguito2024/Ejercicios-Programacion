""" 
Alumno: Thiago La Grotta
Div: 213
Prof: Yanina Scudero, Mariano Guevara
""" 
def suma_naturales(num:int)-> int:
    """ 
    Realiza la suma de números naturales
    """
    while num < 0:
        num = int(input("Re ingrese un numero mayor a 0: "))
    if num == 0:
        return  0
    else:
        return num + suma_naturales(num -1)
num = int(input("Ingrese un numero: "))
retorno = suma_naturales(num)
print("El resultado de la suma de los numeros naturales es: ", retorno)

def calcular_potencia(base:int, exponente:int)-> int:
    """
    Calcula la potencia de un número
    """
    if exponente == 0:
        return 1
    else:
        return base * calcular_potencia(base, exponente-1)
base = int(input("Ingrese la base del numero(mayor a 0): "))
exponente = int(input("Ingrese el exponente del numero(mayor a 0): "))
print("La potencia de la base", base, "con exponente", exponente, "es", calcular_potencia(base, exponente))

def suma_digitos(num: int) ->int:
    """ 
    Realiza la suma de los dígitos de un número
    """
    if num < 10:
        return num
    else:
        return num % 10 + suma_digitos(num//10)
num = int(input("Ingrese un numero para mostrar la suma de sus digitos: "))
resultado = suma_digitos(num)
print("La suma de los digitos del numero ingresado es: ", resultado)

def factorial(num: int)->int:
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(1 * num -1)
num = int(input("Ingrese un numero para calcular el factorial: "))
resultado = factorial(num)
print("El factorial de", num, "es", resultado)

def fibonacci(num:int)->int:
    if num == 0:
        return 0
    elif num == 1:
        return 1 
    else:
        return fibonacci(num-1) + fibonacci(num-2)