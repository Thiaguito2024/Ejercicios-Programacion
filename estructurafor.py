""" 
Alumno Thiago La Grotta 
Div 213
Profesores: Yanina Escudero Mariano Guevara
1. Mostrar los números ascendentes desde el 1 al 10
2. Mostrar los números descendentes desde el 10 al 1
3. Ingresar un número. Mostrar los números desde 0 hasta el número
ingresado.
4. Ingresar un número y mostrar la tabla de multiplicar de ese número. Por
ejemplo si se ingresa el numero 5:
5 x 0 = 0
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15 …
5. Se ingresan un máximo de 10 números o hasta que el usuario ingrese el
número 0. Mostrar la suma y el promedio de todos los números.
6. Imprimir los números múltiplos de 3 entre el 1 y el 10 (*)
7. Mostrar los números pares que hay desde la unidad hasta el número 50 (*)
8. Realizar un programa que permita mostrar una pirámide de números. Por
ejemplo: si se ingresa el numero 5, la salida del programa será la
siguiente:
9. Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta
el número ingresado. Mostrar la cantidad de divisores encontrados.
10.Ingresar un número. Determinar si el número es primo o no.
11.Ingresar un número. Mostrar cada número primo que hay entre el 1 y el
número ingresado. Informar cuántos números primos se encontraron.
"""
# # 1. Mostrar los números ascendentes desde el 1 al 10
print("Numeros ascendentes")
for i in range(0, 11):
    print(f"{i}")

# # 2. Mostrar los números descendentes desde el 10 al 1
print("Números descendentes del 10 al 1:")
for i in range(10, 0, -1):
    print(i, end=' ')

# # 3. Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.
num = int(input("Ingrese un numero: "))
for i in range(0,num+1):
    print(i)

# # 4. Ingresar un número y mostrar la tabla de multiplicar de ese número
num = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {num}:")
for i in range(0, 11):
    print(f"{num} x {i} = {num * i}")

# # 5. Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.
suma = 0
contador = 0
print("Ingrese un máximo de 10 números o 0 para terminar:")
for i in range(10):
    num = int(input(f"Ingrese número {i + 1}: "))
    if num == 0:
        break
    suma += num
    contador += 1

if contador > 0:
    promedio = suma / contador
    print(f"Suma de los números: {suma}")
    print(f"Promedio de los números: {promedio}")
else:
    print("No se ingresaron números.")

# # 6. Imprimir los números múltiplos de 3 entre el 1 y el 10
print("Números múltiplos de 3 entre 1 y 10:")
for i in range(1, 11):
    if i % 3 == 0:
        print(i, end=' ')


# # 7. Mostrar los números pares que hay desde la unidad hasta el número 50
print("Números pares desde 1 hasta 50:")
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=' ')


# # 8. Mostrar una pirámide de números
num = int(input("Ingrese un número para mostrar una pirámide: "))
print("Pirámide de números:")
for i in range(1, num + 1):
    for o in range(1, i + 1):
        print(o, end=' ')
    print()


# # 9. Ingresar un número. Mostrar todos los divisores y la cantidad.
num = int(input("Ingrese un numero: "))
contador_primos = 0
for i in range(1, num+1):
    divisores = num % 1
    if divisores == 0:
        contador_primos += 1
        print(i, "Es divisor de ", num)
print(num, "Tiene un total de: ", contador, "divisores")

# # 10. Ingresar un número. Determinar si el número es primo o no.
num = int(input("Ingrese un número para mostrar los números primos hasta ese número: "))
cont_divisores = 0
for i in range(1, num+1):
    divisores = num % 2
    if divisores == 0:
        cont_divisores += 1

if cont_divisores > 2:
    print("No es primo")
else:
    print("Es primo")


# # 11. Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado.
num = int(input("Ingrese un numero: "))
cantidad = 0
for i in range(2, num+1):
    primo = True
    for j in range(2, i):
        if i % j == 0:
            primo = False
    if primo == True:
        cantidad += 1
        print("los numeros primos son: ", i)
print("La cantidad de primos encontrados entre 1 y el numero ingresado es: ", cantidad)