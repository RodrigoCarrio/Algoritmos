import clasePila as pi

"""
.Permitir 
.Reemplazar todas las ocurrencias de un determindado elemento en una pila

"""

pila_1=pi.Pila()

while True:
    usuario=str(input("Ingrese valores o exit para salir: "))
    if usuario=="exit":
        break
    else:
        pila_1.apilar(usuario)

pila_aux=pi.Pila()
asd=input("Ingrese el valor para reemplazar: ")


print("Pila al inicio")
pila_1.ver_pila()



for i in range(pila_1.get_tamanio()):
    dato=pila_1.desapilar()
    if dato==asd:
        valor_nuevo=input("Ingrese el valor nuevo: ")
        pila_aux.apilar(valor_nuevo)
    else:
        pila_aux.apilar(dato)

print("Pila con el elemento reemplazado y desordenada")
pila_aux.ver_pila()

#volvemos a apilar la pila inicial
for i in range(pila_aux.get_tamanio()):
    pila_1.apilar(pila_aux.desapilar())

print("Pila con el elemento reemplazado y ordenada")
pila_1.ver_pila()
