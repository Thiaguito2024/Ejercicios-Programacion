from Paquetes.funciones_diccionarios  import *
from estudiantes import*

seguir = "si"
######################################## REHACER TODOS LOS PUNTOS CON UN FILTER #################################################33
while seguir == "si":
    opciones = menu()
    if opciones == 1:
        ordenamiento(estudiantes)
    elif opciones == 2:
        calcular_promedios(estudiantes)
    elif opciones == 3:
        programa(estudiantes)
    elif opciones == 4:
        calcular_mayor_promedio(estudiantes)
    elif opciones == 5:
        promedio_edad(estudiantes)
    elif opciones == 6:
        obtener_grupo(estudiantes)
    elif opciones == 7:
        listar_alumnos_mas_jovenes(estudiantes)
    elif opciones == 8:
        seguir = "no"
    else:
        print("Opcion invalida")