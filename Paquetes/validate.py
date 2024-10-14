def validate_number(num:int|float, min:int|float, max:int|float)->bool:
    """ 
    valida que un numero este dentro del rango
    """
    if num >= min or num <= max:
        retorno = True
    else:
        retorno = False
    return retorno

def validate_length(longitud:int, minimo:int, maximo: int)->bool:
    """ 
    Valida el largo de una cadena de caracteres
    """
    retorno = False
    if longitud <= maximo:
        retorno = True
    return retorno