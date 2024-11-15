def verificar_coordenada(lista:list, x:int ,y:int)->bool:
    """
    Verifica si en las coordenadas pasadas por el usuario hay una mina, si la hay retorna true, sino false
    """
    if lista[x][y] == 1:
        explotado = True
    else:
        explotado = False
    return explotado

tablero = [[0,0,1,0,0],
           [0,1,0,1,0],
           [1,0,0,1,0],
           [0,0,1,0,1],
           [0,0,0,0,1]]

seguir = "Si"
contador = 0

while seguir == "Si":
    fila = int(input("Ingrese una fila: "))
    while fila < 0 or fila > 4:
        fila = int(input("Re-ingrese una fila(0-4): "))
    
    columna = int(input("Ingrese una columna: "))
    while columna < 0 or columna > 4:
        columna = int(input("Re-ingrese una columna(0-4): "))
    
    mina = verificar_coordenada(tablero, fila, columna)
    
    if mina:
        tablero[fila][columna] = 0
        contador += 1
    
    seguir = input("Desea seguir: ")
    while seguir != "Si" and seguir != "No":
        seguir = input("Desea seguir(Si/no): ")
    
if contador != 0:
    print(f"Usted exploto {contador} mina/s")
else:
    print("Usted no exploto ninguna minas")