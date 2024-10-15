Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]

def swap(lista,i,j):
    """
    Hace el swap de la lista pasada por parametros
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux
    return lista

def ordenamiento_ascendente_mixto_por_2_listas(lista:list, lista2:list):
    """
    Ordena la lista pasada por parametro de forma ascendente pero el segundo criterio lo hace
    de forma descendente
    """
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if (lista[i] > lista[j]):
                swap(lista,i,j)
                swap(lista2, i,j)
            elif lista[i] == lista[j]:
                    if lista2[i] < lista2[j]:
                        swap(lista2, i,j)
                        swap(lista, i,j)
    
    for i in range(len(lista)):
        print(lista[i], lista2[i])
    
ordenamiento_ascendente_mixto_por_2_listas(Nombres, Puntos)