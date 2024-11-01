#1
sueldo = int(input("Ingrese su sueldo: "))
print((lambda sueldo : sueldo * 1.1)(sueldo)) 

#2
edad  = int(input("Ingrese su edad: "))
print((lambda edad : "Es mayor" if edad > 18 else "No es mayor")(edad))

#3
numero = int(input("Ingrese un numero para saber si es par: "))
print((lambda numero : "Es par" if numero % 2 == 0 else "No es par")(numero))

#4 
numero = int(input("Ingrese un numero para saber si es positivo o negativo: "))
print((lambda numero : "Es negativo" if numero <= 0 else "Es positivo")(numero))

#5
descuento = 100/int(input("Ingrese el descuento a realizar: "))
precio = int(input("Ingrese el precio: "))
print((lambda precio, descuento : precio - descuento)(precio, descuento))

#6
numero = int(input("Ingrese un numero: "))
print((lambda numero : numero * 2)(numero))

#7
genero = input("Ingrese la letra f o m: ")
print((lambda genero : "Es femenino" if genero == "f" else "Es masculino")(genero))