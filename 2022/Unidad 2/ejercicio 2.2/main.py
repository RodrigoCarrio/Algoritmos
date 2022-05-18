""" Ejercicio 2.2
Utilizando la clase Pila y sus metodos
*  Permitir que el usuario cargue valores en una Pila
*  Determinar el número de ocurrencias de un determinado elemento en una pila."""

import clasePila as pi 

pila_1=pi.Pila()

while True:
    usuario=str(input("Ingrese valores o exit para salir: "))
    if usuario=="exit":
        break
    else:
        pila_1.apilar(usuario)

pila_aux=pi.Pila()
cont_ocurrencias=0
asd=input("Ingrese el valor para saber su numero de ocurrencias: ")
for i in range(pila_1.get_tamanio()):
    dato=pila_1.desapilar()
    if dato==asd:
        cont_ocurrencias+=1
    pila_aux.apilar(dato)

for i in range(pila_aux.get_tamanio()):
    pila_1.apilar(pila_aux.desapilar())

print(f"El valor {asd} esta {cont_ocurrencias} veces ")

