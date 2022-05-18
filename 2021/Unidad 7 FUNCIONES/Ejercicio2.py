"""
###**Ejercicio 4.2 (Mediciones)**
El programa debe:
*   Contar con 4 funciones (calcular Area (cuadrado), calcular Perimetro(cuadrado),
    calcular Area (circulo), calcular Perimetro(circulo))
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los dos parametros y devolver el resultado al usuario
*   Gestionar posibles errores
"""

import math as mt

def cir_perimetro():
    while True:
        try:
            radio=float(input("Ingrese el radio del circulo:"))
            if (radio<=0):
                print("El radio debe ser mayor a cero")
            else:
                return round(2*mt.pi*radio,0),radio
        except:
            print("Datos erroneos")
perimetro,radio=cir_perimetro()
print(f"El radio del circulo es {radio}cm y el perimetro {cir_perimetro()}cm ")

def area_circulo():
    while True:
        try:
            radio2=float(input("Ingrese el radio del circulo:"))
            if (radio2<=0):
                print("El radio debe ser mayor a cero")
            else:
                return round(mt.pi*(radio2*radio2),2),radio2
        except:
            print("Datos erroneos")
area,radio2=area_circulo()
print(f"El radio del circulo es {radio2}cm y el area {area_circulo}cm")

def perimetro_cuadrado():
    while True:
        try:
            lado_cuadrado= float(input("Ingrese cuanto mide un lado del cuadrado: "))
            if (lado_cuadrado <= 0):
                print("Ingrese un numero mayor o distinto de cero")
            else:
                 break 
        except:
            print("ERROR. Datos erroneos")
    print(f"el perimetro del cuadrado")
    return lado_cuadrado*4 

def area_cuadrado():
    while True:
        try:
            lado=float(input("Ingrese el lado del cuadrado:"))
            if lado<=0:
                print("El lado de un cuadrado no puede ser negativo")
            else:
                break
        
            

while True:
    condicion=input(
"""Por favor ingrese una opcion
    1. Area (cuadrado)
    2. Perimetro(cuadrado)
    3. Area (circulo)
    4. Perimetro(circulo)
    5. salir

Numero:   """)

