'''
************************************************************
 MATERIA: Algoritmos y Estructuras de Datos 1
 EXAMEN: 1° Examen
 APELLIDO Y NOMBRE: CARRIO RODRIGO
 DNI: 40030222
 CARRERA: 
 AÑO: 2021 
 Se envia mail con asunto: "[AYEDI 2021 - Apellido, Nombre - 1°Examen]"
 ************************************************************
 Items a evaluar:
 1. Requerimientos y comprension de consignas
 2. Estructura (modularización), legibilidad y comentarios del codigo.

¡Cualquier duda con el enunciado consultar al docente!
************************************************************
ENUNCIADO: "Programa de Gestión de alumnos y Materias"

Introduccion: 
    El siguiente programa consiste en un software de gestion de alumnos y gestion de materias
    de una institucion educativa.
    El programa debe permitir agregar y quitar alumnos al sistema junto con su informacion personal: 
    Nombre, Edad y mail.
    El programa debe permitir agregar Materias al sistema.

Requerimientos:
El programa debe:
*   Contar con un menu donde permita al usuario elegir entre las siguientes funciones:
    1. Ver lista de alumnos (Formato: nombre_usuario - Edad - Mail) -->LISTO
    2. Permitir al usuario del programa agregar un nuevo alumno (Indicando: nombre_usuario - Edad - Mail)
       Verificando: Que el nombre_usuario no exista previamente, la edad entre 10 y 18 años y que el mail cuente con un @. --->LISTO
       (Ayuda: metodo in de list sirve tambien para strings)
    3. Editar la edad de un alumno verificando que este entre 10 y 18 años, se edita mediante el nombre.
    4. Ver lista de materias (Formato: Materias) ---> listo
    5. Agregar materias al sistema (verificando que no exista previamente)
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''
alumnos=[["alumno_1","alumno_2","alumno_3"],[12,15,17],["alumno_1@gmail.com","alumno_2@gmail.com","alumno_3@gmail.com"]]
import funciones as fun
print(f"-----------GESTION DE ALUMNOS Y MATERIAS-----------")
while True:
    opcion=input("""
    MENU
    1.Mostrar lista de alumnos 
    2.Agregar un nuevo alumno
    3.Editar la edad de un alumno
    4.Ver lista de materias
    5.Agregar materias al sistema
    6.Salir   

    Ingreso: """)
    if opcion=="1":
        fun.listar_alumnos()
    elif opcion=="2":
        fun.agregar_alumno()
    elif opcion=="3":
        fun.editar_edad()
    elif opcion=="4":
        fun.listar_materias()
    elif opcion=="5":
        fun.agregar_materias()
    elif opcion=="6":
        break
    else:
        print("No ingreso una opcion correcta")