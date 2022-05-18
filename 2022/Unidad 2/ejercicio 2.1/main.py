"""
Ejercicio 2.1
Utilizando la clase Pila y sus metodos

Dada una pila de letras determinar cuántas vocales contiene.
"""

import clasePila as pi

pila_1=pi.Pila()

def cantidad_vocales(pila):
  pila_aux=pi.Pila()
  cont=0
  for i in range(pila.get_tamanio()):
    dato=pila.desapilar()
    if dato == "a" or dato == "e" or dato == "i" or dato == "o" or dato == "u":
      cont+=1
    pila_aux.apilar(dato)

  for i in range(pila_aux.get_tamanio()):
    pila_1.apilar(pila_aux.desapilar())

  print(f"Cant vocales en la pila: {cont}")

pila_1.apilar(2)
pila_1.apilar("a")
pila_1.apilar("e")
pila_1.apilar(5)
pila_1.apilar(6)
pila_1.apilar("u")
pila_1.ver_pila()

cantidad_vocales(pila_1)

pila_1.ver_pila()