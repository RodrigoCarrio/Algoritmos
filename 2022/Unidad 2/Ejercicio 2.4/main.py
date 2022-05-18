"""
Ejercicio 2.4
Utilizando la clase Pila y sus métodos
*  Permitir que el usuario cargue una palabra y cargar letra a letra en una Pila
*  Con métodos de la pila visualizarla en forma inversa.
"""
import clasePila as pi

pila_1=pi.Pila()

while True:    
    usuario=input("Ingrese una palabra o letra y/o exit para salir: ")
    if usuario=="exit":
        break
    else:
        pila_1.apilar(usuario)  
        
print("pila al inicio")
pila_1.ver_pila_2()

pila_aux=pi.Pila()

for i in range(pila_1.get_tamanio()):
    elemento=pila_1.desapilar() 
    pila_aux.apilar(elemento)
         
print("Pila auxiliar")
pila_1=pila_aux
pila_1.ver_pila_2()

print(type("str")==type("str"))