"""
### EJERCICIO 2.5
Utilizando la clase cola y sus metodos 
* Eliminar el i-esimo elemento despues del frente de la cola.
"""

import ClaseCola as co

cola_1 = co.Cola()
print(cola_1.es_vacia())

cola_1.encolar(3)
cola_1.encolar(4)
cola_1.encolar(5)
cola_1.encolar(6)
cola_1.encolar(7)
cola_1.encolar(8)
cola_1.ver_cola()

while True:
    try:
        numero=int(input("ingrese el numero de elemento de la cola a eliminar(no puede ser el primero): "))
    except:
        print("Error")
    if (numero<=1 or numero>cola_1.get_tamaño()):
        print("No puede ser el primer valor o el numero es mas grande que la cola")
    else:
        break
    
for i in range(cola_1.get_tamaño()):
    if i == (numero-1):
        print(f"Se elimino el elemento {cola_1.desencolar()}")        
    else:
        cola_1.mover_al_final()


