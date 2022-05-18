"""El programa debe:

pedir al usuario una palabra
pedir un numero al usuario
mostrar la palabra por pantalla la cantidad de veces que diga el numero
no debe generar errores"""
i=1
try:
    palabra=str(input("Ingrese una palabra:"))
    numero=int(input("Ingrese un numero:"))
    while i<=numero:
    print(f"{palabra}")
    i+=1
except:
    print("Error")


    """
i=1
try:
    palabra=str(input("Ingrese una palabra: "))
    numero=int(input("Ingrese cuantas veces desea mostrarla: "))
    while i<=numero:
        print(f"{palabra}")
        i+=1
except:
    print("ingreso datos incorrectos.")"""