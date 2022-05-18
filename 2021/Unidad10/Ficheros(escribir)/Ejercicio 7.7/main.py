"""
#### **Ejercicio 7.7**
Crear una programa con cuatro opciones:
1.  Crear un archivo en blanco, con el nombre que desee el usuario
2.  Escribir datos en el archivo sin pisar los existentes
3.  borrar los datos del archivo
4.  leer linea a linea el archivo
"""
import os
path = os.path.abspath(os.path.dirname(__file__))#probar este 1°

def crear_archivo():
    nombre=input("Ingrese el nombre del archivo: ")
    global path_archivo
    path_archivo=path+f"\\{nombre}.txt"
    try:
        fichero=open(path_archivo, "w")
        fichero.close()
    except:
        print("Error")

def borrar_archivo():
    try:
        fichero=open(path_archivo, "w")
        fichero.close()
    except:
        print("Error")
        

def escribir_en_archivo(palabra):
    try:
        fichero=open(path_archivo, "a")
        fichero.write(palabra+"\n")
        fichero.close()
    except:
        print("Error")

def pedir_palabras():
    while True:
        palabra=input("Ingrese una palabra o ingrese salir para finalizar: ")
        if palabra=="salir":
            break
        else:
            escribir_en_archivo(palabra)

def leer_archivo():
    try:
        fichero=open(path_archivo, "r")
        while True:
            linea=fichero.readline()
            if linea=="":
                break
            print(linea,end="")
        fichero.close()
    except:
        print("Error")



while True:
    opcion=input("""Ingrese una opcion
    1. Crear un archivo en blanco
    2. Escribir datos en el archivo
    3. borrar los datos del archivo
    4. leer linea a linea el archivo
    5. Salir

    Opcion:"""
    )
    if opcion=="1":
        crear_archivo()
    elif opcion=="2":
        pedir_palabras()
    elif opcion=="3":
        borrar_archivo()
    elif opcion=="4":
        leer_archivo()
    elif opcion=="5":
        break
    else:
        print("Error en el ingreso")


    





