def recorrer_lista_diccionarios(lista:list, clave:str, fila:int, columna:int, direccion:int)->int:
    num_seleccionado = lista[fila][clave][columna]
    cont_iguales = 1
    cont_vueltas = 0 
    if direccion == 1: 
        for i in range(1, len(lista) - fila):
            cont_vueltas += 1 
            if lista[fila][clave][columna] == num_seleccionado:
                cont_iguales += 1
                if cont_iguales == 3:
                    break
            else:
                break  
    elif direccion == -1: 
        for i in range(1, fila+1):
            if lista[fila-i][clave][columna] == num_seleccionado:
                cont_iguales += 1
                if cont_iguales == 3:
                    break
            else:
                break  
    return cont_iguales