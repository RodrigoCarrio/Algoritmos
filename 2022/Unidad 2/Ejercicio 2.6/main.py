"""
### EJERCICIO 2.6
Utilizando la clase Cola y Pila  y sus metodos
* Invertir el contenido de una cola.
"""
import ClaseCola as co
import clasePila as pi

pila_1=pi.Pila()
cola_1 = co.Cola()

cola_1.encolar(3)
cola_1.encolar(4)
cola_1.encolar(5)
cola_1.encolar(6)
cola_1.encolar(7)
cola_1.encolar(8)
cola_1.ver_cola()

#recorremos la cola desencolamos y apilamos en una pila
for i in range(cola_1.get_tamaño()):
    pila_1.apilar(cola_1.desencolar())
    
cola_1.ver_cola()
pila_1.ver_pila_2()

for i in range(pila_1.get_tamanio()):
    cola_1.encolar(pila_1.desapilar())
    
print("Datos invertidos")  
cola_1.ver_cola()
pila_1.ver_pila_2()