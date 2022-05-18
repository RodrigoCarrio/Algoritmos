"""Calculadora
El programa debe:
* Contar con 4 funciones (suma, resta , division y multiplicacion)
* Contar con un menu donde debe pedir al usuario que operacion realizar 
* pedir los dos numeros para operar y devolver el resultado al usuario
* Gestionar posibles errores
"""
def sum(a,b):
    suma=(a)+(b)
    return suma

def resta(a,b):
    restador=(a)-(b)
    return restador

def div(a,b):
    try:
        division=(a)/(b)
    except:
        print("La division genero un error")
        division="Error"
    return division

def multi(a,b):
    multiplicar=(a)*(b)
    return multiplicar

def pedir_numero():
    while True:
        try:
            num1=float(input("1er argumento:"))
            num2=float(input("2do argumento:"))
            break
        except:
            print("Argumentos incorrectos")
    return num1,num2

while True:
    condicion=input(
"""Por favor ingrese una opcion
    1. suma
    2. resta
    3. mutliplicacion
    4. division
    5. salir

Numero:   """)
    if (condicion=="1"):
        a,b=pedir_numero()
        print(f"La suma de {a}+{b} = {sum(a,b)}")
    elif (condicion=="2"):
        a,b=pedir_numero()
        print(f"La resta de {a}-{b} = {resta(a,b)}")
    elif (condicion=="3"):
        a,b=pedir_numero()
        print(f"El producto de {a}*{b} = {multi(a,b)}")
    elif (condicion=="4"):
        a,b=pedir_numero()
        print(f"La division de {a}/{b} = {div(a,b)}")
    elif (condicion=="5"):
        break
        
    else:
        print("Ninguna opcion es correcta")

    