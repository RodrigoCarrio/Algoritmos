"""
#### **Ejercicio 7.4**
Crear una programa para leer el un archivo.csv.
Crear funciones para:
*   obtener los titulos de cada columna (1° Fila)
*   Contar la cantidad de columnas 
*   Contar la cantidad de filas """
#import os
#from posixpath import split
#path = os.path.abspath(os.path.dirname(__file__))#probar este 1°
#path_tabla = path+"\\tabla.csv"
#print(path)

def leer_titulos():
    try:
        tabla=open("tabla.csv", "r")
        titulos=tabla.readline()
        lista_titulos=titulos.split(",")
        print("Los titulos son: ",end="")        
        cont=0
        
        for i in lista_titulos:
            print(i,end="-")
            cont+=1
        print(f"La cantidad de columnas son: {cont} ")
        tabla.close()



    except:
        print("Error")

def contar_filas():
    try:
        tabla=open("tabla.csv", "r")
        cont=0
        while True:
            linea=tabla.readline()
            print(linea)
            if linea=="":
                break
            cont+=1
        print(f"La cantidad de filas son {cont} ")
        tabla.close()



    except:
        print("Error")

leer_titulos()
contar_filas()