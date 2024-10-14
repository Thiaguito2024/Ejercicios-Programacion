"""
Thiago La Grotta
47311007
Div 213
Prof Yanina Escudero Mariano Guevara
Enunciado/s:
Tabla de Posiciones de Torneo de Ping-Pong
Cargar los datos de los jugadores con el propósito de realizar estadísticas (no se sabe cuántos):.
Los datos que se cargarán son:
Nombre del jugador
Edad (validar)
Cantidad de puntos (validar-número entero positivo, hasta 60).
Número de partidos ganados (validar-número entero positivo, hasta 35).
Tipo de saque ("plano", "liftado", "cortado")
Categoría ("elite", "experto", "avanzado")
Se necesita saber
Tema A:
1-Cantidad de jugadores de la categoría "elite" con tipo de saque “plano”, cuya edad esté entre 19 y 25 años
inclusive.
2-Nombre y Categoría del jugador de menor edad con más de 50 puntos.
3-Porcentaje de jugadores de categoría "experto".
4-Mostrar el promedio de edad de los jugadores cuya categoría es “avanzado”.
5-Determinar el tipo de saque más usado por los jugadores, cuya categoría sea “elite”.
"""
cont_jugadores1 = 0
cont_jugadores_in = 0
cont_avanzado = 0
cont_saque_cortado = 0
cont_saque_plano = 0
cont_saque_liftado = 0
edad_min = 101
cont_experto = 0
suma_edad_avanzados = 0
nombre_edad_min = ""
categoria_min = ""
promedio_avanzado = 0 
seguir = "si"
while seguir == "si":
    nombre_jugador = input("Ingrese su nombre: ")
    cont_jugadores_in += 1
    edad = int(input("Ingrese su edad: "))
    while edad < 18 or edad > 100: 
        edad = int(input("RE Ingrese su edad(18-S100): "))
    cant_puntos = int(input("Ingrese cantidad de puntos: "))
    while cant_puntos < 0 or cant_puntos > 60:
        cant_puntos = int(input("RE Ingrese cantidad de puntos(0-60): "))
    num_part_ganados = int(input("Ingrese cantidad de partidos ganados: "))
    while num_part_ganados < 0 or num_part_ganados > 35:
        num_part_ganados = int(input("RE Ingrese cantidad de partidos ganados(0-35): "))
    tipo_saque = input("Ingrese tipo de saque: ").lower()
    while tipo_saque != "plano" and tipo_saque != "liftado" and tipo_saque != "cortado":
        tipo_saque = input("RE Ingrese tipo de saque(plano, liftado, cortado): ").lower()
    categoria = input("Ingrese su categoria: ").lower()
    if categoria == "avanzado":
        cont_avanzado += 1
    while categoria != "elite" and categoria != "experto" and categoria != "avanzado":
        categoria = input("RE Ingrese su categoria(elite, experto, avanzado): ").lower()
    if categoria == "elite" and tipo_saque == "plano" and edad >= 19 and edad <= 25:
        cont_jugadores1 += 1
    if cant_puntos > 50:
        if edad < edad_min:
            nombre_edad_min = nombre_jugador
            categoria_min = categoria       
    if categoria == "experto":
        cont_experto += 1 
    elif categoria == "avanzado":
        suma_edad_avanzados += edad
    if categoria == "elite":
        if tipo_saque == "plano":
            cont_saque_plano += 1
        elif tipo_saque	== "cortado":
            cont_saque_cortado += 1
        else:
            cont_saque_liftado += 1
    seguir = input("Seguir ingresando: ")    
    while seguir != "si" and seguir != "no":
        seguir = input("Seguir ingresando(si o no): ")

categoria_expertos = cont_experto * 100 / cont_jugadores_in
if cont_avanzado != 0:
    promedio_avanzado = suma_edad_avanzados / cont_avanzado
#ejercicio 1
print(f"cantidad de jugadores de la categoría elite con tipo de saque plano, cuya edad esté entre 19 y 25 años inclusive es: {cont_jugadores1}")
#ejercicio 2
print(f"El nombre del menor jugador es {nombre_edad_min} y la categoria es {categoria_min}")
#ejercicio 3
print(f"El porcentaje de jugadores expertos es de {categoria_expertos}")
#ejercicio 4
print(f"{promedio_avanzado} es el promedio de edad de jugadores con categoria avanzada")
#ejercicio 5
if cont_saque_cortado > cont_saque_liftado and cont_saque_cortado > cont_saque_plano:
    print("El saque mas usado es el cortado")
elif cont_saque_liftado > cont_saque_cortado:
    print("El saque mas usado es el liftado")
else:
    print("El saque mas usado es el plano")