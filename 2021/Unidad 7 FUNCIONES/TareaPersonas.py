"""
El programa debe:
*    Pedir al usuario cantidad de personas
*    Pedir al usuario una a una la edad de las personas
*    Finalizado la carga de las edades debe imprimir por pantalla la edad mayor
*    no deben generar errores
"""

personas=[]
while True:
    try:
        usuario=int(input("Ingrese la cantidad de personas:"))
        for i in range(usuario):
            personas.append(int(input("A continuacion ingrese las edades de c/u:")))
        print(f"Le edad mas grande ingresada es",max(personas))
        break
    except:
        print("Ingrese un numero")


