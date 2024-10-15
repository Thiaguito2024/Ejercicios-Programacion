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
    return lista

def ordenamiento_ascendente(lista:list, lista2:list):
    """
    Ordena la lista pasada por parametro de forma ascendente
    """
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if (lista[i] > lista[j]):
                swap(lista,i,j)
                swap(lista2,i,j)
    for i in range(len(lista)):
        print(lista[i], lista2[i])
                
ordenamiento_ascendente(Nombres, Edades)            
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

"""
Ejercicio 3:
Estudiantes =
["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Anto
nio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos =
[“Sosa”,”Gutierrez”,”Alsina”,”Martinez”,”Sosa”,”Ramirez”,”Perez”,”Lopez”,”Arregui”
,”Mitre”,”Andrade”,”Loza”,”Antares”,”Roca”,”Perez”]
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]
Desarrollar una función que realice el ordenamiento de las listas por apellido de
manera ascendente, si el apellido es el mismo, debe ordenar por nombre de manera
ascendente, si el nombre también es el mismo, debe ordenar por nota de manera
descendente.
"""
Estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui","Mitre","Andrade","Loza","Antares","Roca","Perez"]
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]

# < DESCENDENTE, > ASCENDENTE
def ordenamiento_por_3_listas(lista:list, lista2:list, lista3:list):
    """
    Realiza el ordenamiento de manera ascendente, siempre y cuando no llegue a la ultima condicion
    """
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if (lista[i] > lista[j]):
                swap(lista,i,j)
                swap(lista2, i,j)
                swap(lista3, i, j)
            elif lista[i] == lista[j]:
                if lista2[i] > lista2[j]:
                    swap(lista, i,j)
                    swap(lista2, i,j)
                    swap(lista3, i, j)
            else:
                if lista3[i] < lista3[j]:
                    swap(lista, i,j)
                    swap(lista2, i,j)
                    swap(lista3, i, j)
    
    for i in range(len(lista)):
        print(lista[i], lista2[i], lista3[i])



ordenamiento_por_3_listas(Estudiantes,Apellidos,Nota)


