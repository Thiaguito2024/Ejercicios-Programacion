def mostrar(numero):
    """
    muestra el num ingresado por print
    """
    print("El numero ingresado es:", numero)

def mostrar()-> int: 
    """
    ingresa numero y lo retorna sin ningun tipo de parametro
    """
    numero = int(input("Ingrese un numero: "))
    return numero

def num_par(num_ingresado:int)-> bool:
    """
    Determina si es true o false dependiendo si es par o no con parametros formales
    """
    
    if num_ingresado % 2 == 0: 
        retorno = True
    else:
        retorno = False
    return retorno

def min_max(minimo:int, maximo:int)->int:
    """
    minimos y maximos
    """
    numero = int(input(f"Ingrese un numero({minimo}/{maximo}): "))
    
    while numero < minimo or numero > maximo:
        numero = int(input(f"RE Ingrese un numero({minimo}/{maximo}): "))
    
    return numero

def mostrar(numero:int, minimo:int, maximo:int)-> int: 
    """
    ingresa numero y lo retorna 
    """
    while numero < minimo or numero > maximo:
        numero = int(input(f"RE Ingrese un numero({min}/{max}): "))
    print("El numero ingresado por el usuario es: ", numero)

def resta_numero_por_pf(num1:int, num2:int) -> int:
    """
    resta numero ingresados por parametros formales
    """
    resultado = num1 - num2
    return resultado

def resta_sin_parametros()-> int:
    """
    Resta numero sin ningun parametro
    """
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    resultado = num1 - num2
    return resultado

def resta_con_ambos_parametros(num1:int, num2:int):
    """
    Resta por parametros formales
    """
    resultado = num1 - num2
    return resultado 

def resta_parametros_reales():
    """
    resta numeros ingresados por prompt y con parametros reales
    """
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    resta = num1 - num2
    print("El resultado es:", resta)

def realizardescuento(numero:int) -> int:
    """
    Aplica descuento del 5% al número ingresado, con ambos parametros.
    """
    descuento = numero * 0.05
    return descuento

def operar(n1:int, n2:int, operacion) -> int:
    """
    Realiza operación solicitada (suma o resta) entre dos números, con ambos parametros. 
    """
    if operacion == "s":
        return n1 + n2
    elif operacion == "r":
        resultado = n1 - n2    
    return resultado

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

def calcular_potencia(base:int, exponente:int)-> int:
    """
    Calcula la potencia de un número
    """
    if exponente == 0:
        return 1
    else:
        return base * calcular_potencia(base, exponente-1)

def suma_digitos(num: int) ->int:
    """ 
    Realiza la suma de los dígitos de un número
    """
    if num < 10:
        return num
    else:
        return num % 10 + suma_digitos(num//10)

def factorial(num: int)->int:
    """
    Calcula el factorial del numero ingresado
    """
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(1 * num -1)

def fibonacci(num:int)->int:
    if num == 0:
        return 0
    elif num == 1:
        return 1 
    else:
        return fibonacci(num-1) + fibonacci(num-2)

def swap(lista,i,j):
    """
    Hace el swap de la lista pasada por parametros 
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux
    
def ordenamiento_ascendente(lista:list):
    """
    Ordena la lista pasada por parametro de forma ascendente
    """
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if (lista[i] > lista[j]):
                swap(lista,i,j)
            if lista[i][1] == lista[j][1]:
                if lista[i][0] > lista[j][0]:
                    swap(lista,i,j)
            
def ordenamiento_descendente(lista:list):
    """
    Ordena la lista pasada por parametro de forma descendente
    """
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if (lista[i] < lista[j]):
                swap(lista,i,j)
            if lista[i][1] == lista[j][1]:
                if lista[i][0] < lista[j][0]:
                    swap(lista,i,j)

def alta_productos(lista)->list:
    """
    Suma un producto a la lista pasada por parametro
    """
    producto = input("Ingrese el nombre de un producto: ")
    cantidad = int(input("Ingrese la cantidad de producto a agregar: "))
    while cantidad <= 0:
        cantidad = int(input("Ingrese la cantidad de producto a agregar(1-100): "))
    
    fila = int(input("Ingrese la fila en la que desea agregar el producto: "))
    while fila < 1 or fila > 5:
        fila = int(input("Ingrese la fila en la que desea agregar el producto(0-5): "))
        
    columna = int(input("Ingrese la columna en la que desea agregar el producto: "))
    while columna < 1 or columna > 3:
        columna = int(input("Ingrese la columna en la que desea agregar el producto(1-3): "))
    if (len(lista[fila -1][columna -1])) != 0:
        print("Ya hay un producto en esta posicion")
            
    producto = [producto, cantidad, [fila, columna]]    
    lista[fila -1][columna -1] = producto
    for i in range(len(lista)):
        print(lista[i])


def baja_productos(lista):
    """
    Elimina un producto de la lista pasada por parametro
    """
    fila = int(input("Ingrese la fila en la que desea eliminar el producto: "))
    while fila < 0 or fila > 5:
        fila = int(input("Ingrese la fila en la que desea eliminar el producto(0-5): "))
        
    columna = int(input("Ingrese la columna en la que desea eliminar el producto: "))
    while columna < 0 or columna > 3:
        columna = int(input("Ingrese la columna en la que desea eliminar el producto(1-3): "))
    lista[fila-1][columna-1] = []
    for i in range(len(lista)):
        print(lista[i])

def modificar_producto(lista):
    """
    Modifica un producto de la lista pasada por parametro
    """
    print(lista)
    fila = int(input("Ingrese la fila del producto a modificar: "))
    while fila < 0 or fila > 5:
        fila = int(input("Ingrese la fila del producto a modificar(0-5): "))
        
    columna = int(input("Ingrese la columna del producto a modificar: "))
    while columna < 0 or columna > 3:
        columna = int(input("Ingrese la columna del producto a modificar(1-3): "))
    
    producto = input("Ingrese el nombre de un producto: ")
    cantidad = int(input("Ingrese la cantidad de producto que desea modificar: "))
    while cantidad <= 0:
        cantidad = int(input("Ingrese la cantidad de producto a agregar(1-100): "))
    producto = [producto, cantidad, [fila-1 , columna-1]]
    lista[fila-1][columna-1] = producto
    print(lista)

def listar_productos(lista):
    """
    Muestra la lista pasada por parametro
    """
    for i in range(len(lista)):
        print(lista[i])

def lista_ordenado(lista):
    """
    Ordena la lista pasada por parametro
    """
    ordenamiento = input("Ordenar de manera ascendente o descendente: ")
    if ordenamiento == "ascendente":
        ordenamiento_ascendente(lista)
    else:
        ordenamiento_descendente(lista)
    print(lista)
    
def reponer(lista:list):
    """
    Suma la cantidad al producto que se desea reponer

    """
    cantidad = int(input("Ingrese la cantidad de producto que desea reponer: "))
    
    while cantidad <= 0 or cantidad > 100:
        cantidad = int(input("Ingrese la cantidad de producto que desea reponer: "))
    
    fila = int(input("Ingrese la fila del producto a reponer: "))
    while fila < 0 or fila > 4:
        fila = int(input("Ingrese la fila del producto a reponer: "))
    
    lista[fila][1] += cantidad
    for i in range(len(lista)):
        print(lista[i])