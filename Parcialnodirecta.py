# Nota de aprobacion no directa: 4 
# Porque si se ingresaba un 0 se tomaba como valido
# Solucion: cambiar el 0 por un 1
def buscar_numero(lista:list, num_ing:int)->int: 
    """
    Se el pasa or parametro y lo busca en la lista
    """
    cont = 0
    for i in range(len(lista)):
        if lista[i] == num_ing:
            cont += 1
    return cont

lista = [1,2,3,4,5,6,7,8,9]
numero_ingresado = int(input("Ingrese un numero para buscar en la lista: "))
while numero_ingresado < 1 or numero_ingresado > 9:
    numero_ingresado = int(input("Reingrese un numero para buscar en la lista(1-9): "))

numero = buscar_numero(lista, numero_ingresado)
print(f"La cantidad de veces que aparece el numero {numero_ingresado} en la lista {lista} es {numero}")