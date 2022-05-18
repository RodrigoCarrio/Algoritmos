"""#### **Ejercicio 7.3**
Crear una funcion para leer el un archivo.txt.

Crear funciones para:
*   Contar la cantidad de letrar que tiene el archivo (letras no espacios ni puntos)
*   Contar la cantidad de palabras que tiene el archivo"""

def contar_letras_palabras():
    try:
        fichero=open("texto.txt", "r")
        contador_letras=0
        while True:
            letra = fichero.readline(1)
            if letra=="":
                break
            elif letra!="." and letra !=" ":   
                contador_letras+=1

        fichero.close()
        print(contador_letras)
    except:
        print("No existe el arhcivo")
    
contar_letras_palabras()
