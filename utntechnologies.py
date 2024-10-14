""" 
Nombre: Thiago
Apellido: LA Grotta 
Div: 213
Prof: Yanina Scudero Mariano Guevara
UTN Technologies, una reconocida software factory se encuentra en la búsqueda
de ideas para su próximo desarrollo en Python, que promete revolucionar el
mercado.
Las posibles aplicaciones son las siguientes:
● Inteligencia artificial (IA),
● Realidad virtual/aumentada (RV/RA),
● Internet de las cosas (IOT)
Para ello, la empresa realiza entre sus empleados una encuesta, con el
propósito de conocer ciertas métricas.
A) Los datos a ingresar por cada empleado encuestado son:
● nombre del empleado
● edad (no menor a 18)
● género (Masculino - Femenino - Otro)
● tecnologia (IA, RV/RA, IOT)
B) Cargar por terminal 10 encuestas.
C) Determinar:
1. Cantidad de empleados de género masculino que votaron por IOT o IA,
cuya edad esté entre 25 y 50 años inclusive.
2. Porcentaje de empleados que no votaron por IA, siempre y cuando su
género no sea Femenino o su edad se encuentre entre los 33 y 40.
3. Nombre y tecnología que votó, de los empleados de género masculino con
mayor edad de ese género.
"""
cont_gen_m = 0
cont_empleados_no_votaron_ia = 0
cont_empleados = 0
edad_max = 0
nombre_edad_max = ""
tecnologia_max = ""



for i in range(10):
    nombre_empleado = input("Ingrese su nombre: ")
    cont_empleados += 1
    edad_empleado = int(input("Ingrese su edad: "))
    while edad_empleado < 18 or edad_empleado >= 100: 
        edad_empleado = int(input("RE Ingrese su edad(18-100): "))
    genero = input("Ingrese su genero: ")
    while genero != "masculino" and genero != "femenino" and genero != "otro":
        genero = input("RE Ingrese su genero(masculino - femenino - otro): ")
    tecnologia_votada = input("Ingrese su tecnologia: ")
    while tecnologia_votada != "ia" and tecnologia_votada != "rv" and tecnologia_votada != "ra" and tecnologia_votada != "iot":
        tecnologia_votada = input("RE Ingrese su tecnologia(IA, RV/RA, IOT): ")
    if genero == "masculino" and tecnologia_votada == "IA" or tecnologia_votada == "IOT" and edad_empleado >= 25 and edad_empleado <= 50:
        cont_gen_m += 1
    if tecnologia_votada != "IA" and genero != "femenino" and edad_empleado >= 33 and edad_empleado <= 40:
        cont_empleados_no_votaron_ia += 1
    if genero == "masculino":
        if edad_empleado > edad_max:
            edad_max = edad_empleado
            nombre_edad_max = nombre_empleado
            tecnologia_max = tecnologia_votada

empleados_no_votaron_ia = cont_empleados_no_votaron_ia * 100 / cont_empleados
#ejercicio C1
print(f"la cantidad de empleados masculinos es de: {cont_gen_m}")
#ejercicio C2
print(f"El porcentaje de empleados que no votaron IA es: {empleados_no_votaron_ia}")
#ejercicios C3
print(f"El nombre de empleado con mas edad es {nombre_edad_max} y la tecnologia elegida es {tecnologia_max} y tiene {edad_max} años")