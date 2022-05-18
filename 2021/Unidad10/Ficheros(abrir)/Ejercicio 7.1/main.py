"""#### **Ejercicio 7.1**
Crear una funcion para leer un archivo.txt hasta encontrar un punto.
"""
#import os
#path = os.path.abspath(os.path.dirname(__file__))#probar este 1°
#print(path)
#path = os.path.abspath(os.path.dirname('__file__'))#probar este 2°
#path = os.path.dirname(os.path.abspath("__file__"))#probar este 3°
def leer_archivo():
    try:
        fichero=open("texto.txt", "r")
        while True:
            caracter=fichero.readline(1)
            print(caracter,end="")
            if caracter==".":
                break
        fichero.close()
    except:
        print("No existe el arhcivo")

def imprimir_hasta_punto_for():
    try:
        fichero = open("texto.txt", 'r')
        for c in fichero.readline():
            print(c,end="")
            if(c=="."):
                break
        fichero.close()
    except:
        print("no existe el archivo")
    
leer_archivo()
