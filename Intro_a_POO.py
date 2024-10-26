#1
class Persona:
    def __init__(self,nombre:str,edad:int):
        self.name = nombre
        self.años = edad
    
    def mostrar(self):
        print(f"Hola mi Nombre es {self.name} y tengó {self.años} años.")

persona = Persona("Thiago", 18)
persona.mostrar()
#2
class Libro:
    def __init__(self, titulo, nombre, año_publicacion):
        self.__titulo = titulo
        self.__nombre = nombre
        self.__año_publicacion =  año_publicacion
    
    def mostrar(self):
        print("El titulo del libro es: ", self.__titulo)
        print("El nombre del libro es: ", self.__nombre)
        print("Su año de publicaion es: ", self.__año_publicacion)

titulo = Libro("Clases","ej2","22/10")
titulo.mostrar()

#3
class Rectangulo:
    def __init__(self, base:int, altura:int):
        self.base = base
        self.altura = altura
    def area(self):
        area = self.base * self.altura
        print(f"El area de este rectangulo es: {area}")
    def perimetro(self):
        perimetro = 2 * (self.base + self.altura)
        print(f"El perimetro de este rectangulo es: {perimetro}")
        
medidas = Rectangulo(5, 3)
medidas.area()
medidas.perimetro()

#4
class Calculadora: 
    def __init__(self, num_1:int, num_2:int):
        self.numero_1 = num_1
        self.numero_2 = num_2

    ############## Bucle calculadora ###############

    def ejecutar_calculadora(self):
        while True:
            opciones  = self.__mostrarmenu()

            match (opciones):
                case 1: 
                    self.suma()
                case 2:
                    self.resta()
                case 3:
                    self.multiplicacion()
                case 4:
                    self.division()
                case 5:
                    self.reemplazo_nums()

            if (opciones > 5 or opciones < 0):
                break

    
    def __mostrarmenu(self):
        return int(input("""
                        1 sumar
                        2 restar
                        3 multiplicar
                        4 dividir
                        5 cambiar numeros
                             """))
    

    ################ 4 operaciones básicas ###############
    def suma(self):
        suma = self.numero_1 + self.numero_2 
        print(f"El resultado de la suma es: {suma}")
    
    def resta(self):
        resta = self.numero_1 - self.numero_2 
        print(f"El resultado de la resta es: {resta}")
    
    def multiplicacion(self):
        multiplicacion = self.numero_1 * self.numero_2 
        print(f"El resultado de la multiplicacion es: {multiplicacion}")
    
    def division(self):
        division = self.numero_1 / self.numero_2 
        print(f"El resultado de la division es: {division}")

    ################ Reemplazo de atributos ###############
    def reemplazo_nums(self):
        self.numero_1 = int(input("Ingrese un numero : "))
        self.numero_2 = int(input("Ingrese otro numero : "))



numero_ing_1 = int(input("Ingrese un numero : "))
numero_ing_2 = int(input("Ingrese otro numero : "))
numeros = Calculadora(numero_ing_1,numero_ing_2)
numeros.suma()
numeros.reemplazo_nums()

#5
class Animal:
    def __init__(self, nombre:str):
        self.name = nombre
        
class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def Mostrar_sonido_perro(self):
        print("Guau Guau")
        
class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def Mostrar_sonido_gato(self):
        print("Miau")
        
perro = Perro("luna")
gato = Gato("Michi")

perro.Mostrar_sonido_perro()
gato.Mostrar_sonido_gato()

#6
class Cuenta_Bancaria:
    def __init__(self, titular: str, saldo: float):
        self.__titular = titular
        self.__saldo = saldo

    def mostrar_saldo(self):
        return f"El saldo que hay en la cuenta es: {self.__saldo}"

    def retirar_saldo(self, retiro: float):
        if retiro > self.__saldo:
            print("Fondos insuficientes")
        else:
            self.__saldo -= retiro
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")

    def depositar_saldo(self, deposito: float):
        self.__saldo += deposito
        print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
