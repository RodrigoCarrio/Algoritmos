"""
#### **Ejercicio 7.6**
Crear una funcion que lo que le pida palabras al usuario 
y que las vaya escribiendo en un archivo txt cada palabra una bajo la otra."""

def escribir_en_archivo(palabra):
    try:
        fichero=open("texto.txt", "a")
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

pedir_palabras()
