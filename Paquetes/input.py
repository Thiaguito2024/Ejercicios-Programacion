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

def get_string(longitud:int, mensaje:str)-> str|None:
    
    while len(mensaje) > longitud:
        print("Escribir un mensaje que no sea mayor a", longitud, "caracteres")