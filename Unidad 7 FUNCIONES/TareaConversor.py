"""
El programa debe:

*   Contar con 4 funciones:
  1.  Conversor de Grados Celcius a Fahrenheit(temperatura en °C).(buscar regla)
  2.  Conversor de cm3 a litros (cantidad de cm3)
  3.  Conversor de litros a cm3 (cantidad de litros)
  4.  Pesos a Dolares (pesos)
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los parametros y devolver el resultado al usuario
*   Gestionar posibles errores
"""
def celcius_a_far():
    while True:
        try:
            celcius=int(input("Ingrese la Temperatura en °C:"))
            print(f"La temperatura de {celcius}°C equivale a {((celcius*1.8)+32)} °F. ")
            break       
        except:
            print("No ingreso un numero")

def cm3_a_litros():
    while True:
        try:
            liquido1=float(input("Ingrese cantidad de cm3:"))
            print(f"El volumen de {liquido1}cm3 equivale a {(liquido1*(1/1000))} Lts. ")
            break
        except:
            print("No ingreso un numero")

def litros_a_cm3():
    while True:
        try:
            liquido2=float(input("Ingrese cantidad de Lts:"))
            print(f"El volumen de {liquido2} Lts equivale a {(liquido2*1000)}cm3 ")
            break
        except:
            print("No ingreso un numero")
        
def pesos_a_usd():
    while True:
        try:
            pesos=int(input("Ingrese cantidad de pesos a convertir:"))
            print(f"La cantidad de ${pesos} equivale a {pesos/182}USD ")
            break
        except:
            print("No ingreso un numero")

while True:
    condicion=input(
""" Por favor ingrese una opcion
    1. Conversor de °C a °F
    2. Conversor de cm3 a Lts
    3. Conversor de Lts a cm3
    4. Conversor de Pesos a USD
    5. Salir
Numero: """)
    if (condicion=="1"):
        celcius_a_far()
    elif (condicion=="2"):
        cm3_a_litros()
    elif (condicion=="3"):
        litros_a_cm3()
    elif (condicion=="4"):
        pesos_a_usd()
    elif (condicion=="5"):
        break
    else:
        print("No ingreso una opcion correcta")

