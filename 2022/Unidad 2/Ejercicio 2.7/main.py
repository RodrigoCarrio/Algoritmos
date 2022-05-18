"""
### EJERCICIO 2.7 
Utilizando la clase Cola y sus métodos

*   Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos.
"""
import ClaseCola as co

cola_1=co.Cola()

def son_primos(numero):
    divisores=0
    for i in range(1,numero+1):
        if numero % i ==0:
            divisores+=1
    if divisores==2:
        return True
    else:
        return False

while True:
    try:
        usuario=int(input("Ingrese numeros unicamente, o ingrese cualquier letra o simbolo para salir: "))
        
        cola_1.encolar(usuario)
    except:
        break

cola_1.ver_cola()

for i in range(cola_1.get_tamaño()):
    numero=cola_1.desencolar()
    if son_primos(numero):
        cola_1.encolar(numero)

cola_1.ver_cola()

