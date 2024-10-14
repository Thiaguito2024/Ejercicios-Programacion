from listas_personas import *

def usuarios_mexico(nombres:list, telefonos:list, mails:list, address:list, postalZip:list, region:list, country:list, edades:list):
    for i in range(len(country)):
        if country[i] == "Mexico":
            print(f"Datos de los usuarios de mexico: Nombre: {nombres[i]}, Teléfono: {telefonos[i]}, \n Email: {mails[i]}, Dirección: {address[i]}, Código Postal: {postalZip[i]},  Región: {region[i]}, Edad: {edades[i]}")

def usuarios_brazil(nombres:list, telefonos:list, mails:list):
    for i in range (len(country)):
        if country[i] == "Brazil":
            print(f"Datos de los usuarios de Brazil: Nombre: {nombres[i]}, Email: {mails[i]}, Teléfono: {telefonos[i]}")

def usuarios_jovenes(nombres:list, telefonos:list, mails:list, address:list, postalZip:list, region:list, country:list, edades:list):
    min_edad = edades[0]
    
    for i in range(len(edades)):
        if edades[i] == min_edad:
            print(f"Datos de el o los usuarios mas jovenes: Nombre: {nombres[i]},  Edad: {edades[i]}, Pais: {country[i]}, Teléfono: {telefonos[i]}, \n Email: {mails[i]}, Dirección: {address[i]}, Código Postal: {postalZip[i]}, Región: {region[i]}")

def promedio_edad(edades): 
    suma_edad = 0
    for i in edades:
        suma_edad += i
        
    promedio = suma_edad / len(edades)        
    print("El promedio de edades es: ", promedio)  
    

def usuarios_mayores(edades):
    max_edad = edades[0]
    
    for i in range(len(edades)):
        if edades[i] > max_edad:
            max_edad = edades[i]
            
    for i in range(len(edades)):
        if edades[i] == max_edad:
            print(f"El usuario de mayor edad en Brasil es: {nombres[i]}, Edad: {edades[i]}, Email: {mails[i]}, Teléfono: {telefonos[i]}")

def usuarios_mx_y_brasil(nombres:list, telefonos:list, mails:list, address:list, postalZip:list, region:list, country:list, edades:list):
    for i in range(len(country)):
        if country[i] == "Brazil" or country[i] == "Mexico" and postalZip[i] >= 8000:
            print(f"Datos de los usuarios de Brazil o Mexico: Nombre: {nombres[i]}, Teléfono: {telefonos[i]}, \n Email: {mails[i]}, Dirección: {address[i]}, Código Postal: {postalZip[i]},  Región: {region[i]}, Edad: {edades[i]}")

def usuarios_italianos(nombres, mails, telefonos):
    for i in range(len(country)):
        if country[i] == "Italy" and edades[i] >= 40:
            print(f"Su nombre es: {nombres[i]}, su mail: {mails[i]}, y su telefono: {telefonos[i]}")            