"""
Ejercicio 2.8
Crear metodo de cola que permita agregar un elemento con cierta prioridad.

P = 0, se agrega al frente de la cola
P = 1, se agrega segundo en la cola
P = 2, se agrega a la mitad de la cola
"""
import ClaseCola as co

cola_1 = co.Cola()

cola_1.encolar(1)
cola_1.encolar(2)
cola_1.encolar(3)
cola_1.encolar(4)
cola_1.encolar(5)
cola_1.encolar(6)
cola_1.encolar(7)
cola_1.encolar(8)
cola_1.ver_cola()

cola_1.agregar_con_prioridad(10,0)
cola_1.agregar_con_prioridad("hola",2)
cola_1.agregar_con_prioridad("segundo",0)

cola_1.ver_cola()