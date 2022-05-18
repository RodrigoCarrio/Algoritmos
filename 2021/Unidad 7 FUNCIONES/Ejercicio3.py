"""
###**Ejercicio 4.3 (Palabras)**
El programa debe:
*   Contar con 3 funciones:
    1. Contador de letras (letra,palabra): Debe contar la cantidad de letras que tiene una palabra o 
    frase (Ambos parametros)
    2. Comparador de palabras (palabra1 vs palabra2): debe comparar que palabra tiene mas letra.
    IMPORANTE:deben ser palabras y no frases (verificar)
    3. Quitador de vocales(palabra a retirar las vocales): debe recibir una palabra o frase y 
    quitar todas las vocales
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los parametros y devolver el resultado al usuario
*   Gestionar posibles errores
"""
def contador_de_letras(letra,palabra_o_frase):
    contador=0
    for i in palabra_o_frase:
        if i == letra:
            contador +=1
    return contador

def comparador_de_palabras(palabra_1,palabra_2):
    contador_1=0
    contador_2=0
    for i in palabra_1:
        if i != " ":
            contador_1+=1
        else:
            contador_1 = -1
            break

    for i in palabra_2:
        if i!=" ":
            contador_2+=1
        else:
            contador_2=-1
            break
    
    if contador_1 == -1 or contador_2 == -1:
        return "Se ha ingresado una frase"
    elif contador_1>contador_2:
        return "La palabra 1 tiene más letras"
    elif contador_1==contador_2:
        return "Las palabras tienen la misma cantidad de letras"
    else:
        return "La palabra 2 tiene más letras"

def quitador_vocales(palabra_o_frase):
    palabra_auxiliar=""
    for i in palabra_o_frase:
        if i != ("a" and i !="e" and i != "i" and i != "o" and i != "u"):
            palabra_auxiliar = palabra_auxiliar + i
    
    return palabra_auxiliar

while True:
    condicion=input(
""" Por favor ingrese una opcion
    1. Contador de letras
    2. Comparador de palabras
    3. Quitador de vocales
    4. Salir
Numero: """)
    if (condicion=="1"):
        while True:
            letra= input("Ingrese una letra:")
            if letra.isalpha():
                if len(letra)==1:
                    break
        while True:
            palabra= input("Ingrese una letra:")
            if len(palabra)>3:
                break
        print(f"La cantidad de letras {letra} en {palabra} es: {contador_de_letras(letra,palabra)} ")
    elif (condicion=="2"):

    elif (condicion=="3"):

    elif (condicion=="4"):
        
    else:
        print("No ingreso una opcion correcta")


#letras = contador_de_letras("a","hola buen dia")
#print(f"Cantidad de letras a {letras}")