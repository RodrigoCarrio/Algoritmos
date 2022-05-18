"""
Crear una funcion para leer el un archivo.txt.
*   pedir al usuario una palabra y encontrar la cantidad de veces que 
     aparece esa palabra en el archivo
"""
try:
    fichero = open("texto.txt", "r")
    palabras = fichero.read()
    lista_palabras = palabras.split()
    print(lista_palabras)
    palabra_a_contar = input("Ingrese la palabra a contar: ")
    contador = 0
    for i in lista_palabras:
        if i == palabra_a_contar:
            contador += 1
    print(f"La palabra {palabra_a_contar} esta {contador} de veces en el texto")
except:
    print("Archivo no existe")



