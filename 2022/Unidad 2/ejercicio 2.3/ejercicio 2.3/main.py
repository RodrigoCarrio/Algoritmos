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

asd=input("Ingrese el valor para reemplazar: ")
asd_que_reemplaza=input("Ingrese el valor nuevo: ")

print("Pila al inicio")
pila_1.ver_pila()

pila_aux=pi.Pila()

for i in range(pila_1.get_tamanio()):
    elemento=pila_1.desapilar()
    if elemento==asd:
        pila_aux.apilar(asd_que_reemplaza)
    else:
        pila_aux.apilar(elemento)

print("Pila con el elemento reemplazado y desordenada")
pila_aux.ver_pila()

#volvemos a apilar la pila inicial
for i in range(pila_aux.get_tamanio()):
    pila_1.apilar(pila_aux.desapilar())

print("Pila con el elemento reemplazado y ordenada")
pila_1.ver_pila()
