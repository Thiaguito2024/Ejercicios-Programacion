"""
Ejercicio 1: Dadas las siguientes listas:
Nombres =
["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Anto
nio", "Eugenia", "Soledad", "Mario", "Mariela"]
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
Desarrollar una función que realice el ordenamiento de las listas por nombre de
manera ascendente.
"""
Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

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
                
ordenamiento_ascendente(Nombres)
ordenamiento_ascendente(Edades)
print(ordenamiento_ascendente(Nombres))    
print(ordenamiento_ascendente(Edades))            
"""
Ejercicio 2: Dadas las siguientes listas:
Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias
Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos",
"Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]
Desarrollar una función que realice el ordenamiento de las listas por nombre de
manera ascendente, si el nombre es el mismo, debe ordenar por puntos de manera
descendente.
"""
Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]
def ordenamiento_ascendente_mixto(lista:list, lista2:list):
    """
    Ordena la lista pasada por parametro de forma ascendente pero el segundo criterio lo hace
    de forma descendente
    """
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            # matematica > ingles
            if (lista[i] > lista[j]):
                swap(lista,i,j)
                swap(lista2, i,j)
            elif lista[i] == lista[j]:
                    if lista2[i] < lista2[j]:
                        swap(lista2, i,j)
                        swap(lista, i,j)

ordenamiento_ascendente_mixto()