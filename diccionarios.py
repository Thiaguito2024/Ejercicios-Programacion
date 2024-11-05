from funciones_diccionarios import *
seguir = "si"

while seguir == "si":
    opciones = menu()
    if opciones == 1:
        ordenamiento(estudiantes) 
    elif opciones == 2:
        mostrar_promedios(estudiantes)
    elif opciones == 3:
        programa(estudiantes)
    elif opciones == 4:
        promedio_edad(estudiantes)
    elif opciones == 5:
        mostrar_promedios(estudiantes)
    elif opciones == 6:
        obtener_grupo(estudiantes)
    elif opciones == 7:
        listar_alumnos_mas_jovenes(estudiantes)
    else:
        seguir = "no"