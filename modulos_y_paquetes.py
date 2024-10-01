def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int|None:
    """ 
    Pide numeros enteros por consola
    """ 
    while reintentos > 0:
        num = int(input(f"{mensaje}"))
        if num >= minimo and num <= maximo:
            return num
        else:
            num = int(input(f"{mensaje_error}"))
            return get_int(mensaje, mensaje_error, minimo, maximo, reintentos-1)
mensaje = "Ingrese un numero: "
mensaje_error = "RE Ingrese un numero entre (1-10): "
minimo = 1
minimo = int(minimo)
maximo = 10
maximo = int(maximo)
reintentos = 3
numero = get_int(mensaje, mensaje_error, 1, 10, reintentos)
if numero:
    print("El numero ingresado es: ", numero) 
else:
    print("El resultado es", None)


def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) -> float|None:
    """ 
    Pide un numero decimales por consola
    """ 
    while reintentos > 0:
        num = float(input(f"{mensaje}"))
        if num >= minimo and num <= maximo:
            return num
        else:
            num = float(input(f"{mensaje_error}"))
            return get_float(mensaje, mensaje_error, minimo, maximo, reintentos - 1)
mensaje = "Ingrese un numero: "
mensaje_error = "RE Ingrese un numero entre (1.2-10.99): "
minimo = 1.2
minimo = float(minimo)
maximo = 10.99
maximo = float(maximo)
reintentos = 3
numero = get_float(mensaje, mensaje_error, 1.2, 10.99, reintentos)
if numero:
    print("El numero ingresado es: ", numero) 
else:
    print("El resultado es", None, "ya que el usuario ingreso", reintentos, "veces un numero erroneo")

def get_string(longitud:int)-> str|None:
    
    while len(mensaje) > longitud:
        print("Escribir un mensaje que no sea mayor a", longitud, "caracteres")