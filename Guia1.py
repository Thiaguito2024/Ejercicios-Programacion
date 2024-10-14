"""
Guia 1
Thiago La Grotta
Div 213
Turno Tarde
Profesores: Yanina Escudero y Mariano Guevara
"""
""" 
Ejercicio 1:
Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su sueldo para esa persona.
Ejercicio 2:
Pedir una edad. Informar si la persona es mayor de edad (más de 18 años), adolescente (entre 13 y 17 años) o niño (menor a 13 años).
Ejercicio 3:
Ingresar 5 números enteros, distintos de cero.
Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos.
Ejercicio 4:
Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO ser soltero.'
Ejercicio 5:
Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000 por cada estadía como base, se pide el ingreso de una estación del año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del Plata/Córdoba) para vacacionar para poder calcular el precio final: -en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un descuento del 10% Mar del Plata tiene un descuento del 20% -en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene un aumento del 10% Mar del Plata tiene un aumento del 20% -en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el precio sin descuento.
Validar el ingreso de datos. 
"""

""" #Ejercicio 1
nombre = input("Ingrese su nombre: ")
sueldo = float(input("Ingrese su sueldo: "))    
incremento = sueldo * 0.1
sueldo_inc = incremento + sueldo
print(nombre)
print(sueldo_inc)
"""

""" # Ejericio 2 

edad = input("Ingrese su edad: ")
edad = int(edad)

if edad >= 18:
    print("Es mayor")
elif edad >= 13:
    print("Es adolescente")
elif edad >= 0:
    print("Es niño")
else:
    print("No existen edades negativas")

"""

""" 
Ejercicio 3:
Ingresar 5 números enteros, distintos de cero. 
for i in range(1,6):
    print(i)
"""
#ejercicio 4
# Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil distinto a "Soltero",
# mostrar el siguiente mensaje: 'Es muy pequeño para NO ser soltero.'
"""
edad = int(input("ingrese su edad: "))
estado_civil = input("Ingrese su estado civil: ")

if edad < 18 and estado_civil != "Soltero":
    print("Es muy pequeño para NO ser soltero.")
else:
    print("Es mayor de 18 o el estado civil es distinto de Soltero") 
"""
# Ejercicio 5

"""
Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000 por cada estadía como base,
se pide el ingreso de una estación del año(Invierno/Verano/Otoño/Primavera) 
y localidad(Bariloche/Cataratas/Mar del Plata/Córdoba) para vacacionar para poder calcular el precio final: 
-en INVIERNO: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un descuento del 10% Mar del Plata
tiene un descuento del 20% 
-en VERANO: Bariloche tiene un descuento del 20% Cataratas y 
Córdoba tiene un aumento del 10% Mar del Plata tiene un aumento del 20% 
-en OTOÑO y PRIMAVERA: Bariloche tiene un aumento del 10% Cataratas tiene un aumento del 10% 
Mar del Plata tiene un aumento del 10% y Córdoba tiene el precio sin descuento.
Validar el ingreso de datos

precio = 15000
estacion = input("Introducir una estancia del año [Invierno/Verano/Otoño/Primavera]: ")
while estacion != "Invierno" and estacion !="Verano" and estacion !="Otoño"and estacion !="Primavera":
    estacion = input("Introducir una estancia del año [Invierno/Verano/Otoño/Primavera]: ")
localidad = input("Introducir una localidad [Bariloche/Cataratas/Mar del Plata/Cordoba]: ")
while localidad != "Bariloche" and localidad != "Cataratas" and localidad != "Mar Del Plata" and localidad != "Cordoba":
    localidad = input("Introducir una localidad [Bariloche/Cataratas/Mar del Plata/Cordoba]: ")

    

if estacion == "Invierno":
    if localidad == "Bariloche":
        precio_final= precio + (precio*20/100)
    elif localidad == "Cataratas" or "Cordoba":
        precio_final= precio - (precio*10/100)
    else:
        precio_final= precio - (precio *20/100)    
elif estacion == "Verano":
    if localidad == "Bariloche":
        precio_final=precio - (precio *20/100) 
    elif localidad == "Cataratas" or "Cordoba":
        precio_final= precio + (precio*10/100)
    else:
        precio_final= precio + (precio*20/100)
else:
    if localidad == "Cordoba":
        precio_final= precio
    else:
        precio_final= precio + (precio*10/100)
    
print(f"El valor del viaje en {estacion} para la localidad {localidad} es de ${precio_final}")
"""

#No se como hacer el ejercicio 3