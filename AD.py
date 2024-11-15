# Nota: 5
# Porque se entra en un bucle sin salida
# Solucion: Poner las verificaciones dentro del while principal y eliminar la definicion de la var hundido
def verificar_coordenada(lista:list, x:int ,y:int)->bool:
    """
    Verifica si en las coordenadas pasadas por el usuario hay un barco, o esta hundido
    """
    if lista[x][y] == 1:
        hundido = True
    else:
        hundido = False
    return hundido

tablero = [[0,0,1,0,0],
           [0,1,0,1,0],
           [1,0,0,1,0],
           [0,0,1,0,1],
           [0,0,0,0,1]]

cont_hundido = 0
cont_agua = 0

seguir = "s"
while seguir == "s":
    fila = int(input("Ingrese una fila: "))
    while fila < 0 or fila > 4:
            fila = int(input("Re-ingrese una fila(0-4): "))
    
    columna = int(input("Ingrese una columna: "))
    while columna < 0 or columna > 4:
        columna = int(input("Re-ingrese una columna(0-4): "))
    
    barcos = verificar_coordenada(tablero, fila, columna)
    
    if barcos:
        tablero[fila][columna] = 0
        cont_hundido += 1
    else:
        cont_agua += 1
    
    
    seguir = input("Desea seguir: ")
    while seguir != "s" and seguir != "n":
        seguir = input("Desea seguir(Si/No): ")
    

if cont_hundido > cont_agua:
    print(f"Usted hundio {cont_hundido} barco/s")
else:
    print(f"Usted fallo {cont_agua} tiro/s")
