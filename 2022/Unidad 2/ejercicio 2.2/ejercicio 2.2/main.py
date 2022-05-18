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

cont_ocurrencias=0
asd=input("Ingrese el valor para saber su numero de ocurrencias: ")
for i in range(pila_1.get_tamanio()):
    if pila_1.desapilar()==asd:
        cont_ocurrencias+=1

print(f"El valor {asd} esta {cont_ocurrencias} veces ")

