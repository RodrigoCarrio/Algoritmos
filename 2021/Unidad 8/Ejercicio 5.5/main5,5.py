##**Ejercicio 5.5**
"""
Crear una funcion que debe:
*    Tener almacenado el abcedario en una lista
*    Pedir al usuario un numero (2 o 3) - VERIFICAR 
*    Elimina de la lista las letras que ocupen posiciones múltiplos de ese numero
*   Mostrar por pantalla la lista resultante.
*   No deben aparecer y se deben tener en cuenta todos los posibles errores
"""
import string as _str
def lista_abecedario():
    abecedario=list(_str.ascii_lowercase)
    print(abecedario) 
    while True: 
        usuario=input("Ingrese el Nro 2 o Nro 3:")    
        if (usuario=="2"):
            print("El Nro ingresado es: 2")
            break
        elif (usuario=="3"):
            print("El Nro ingresado es: 3")
            break
        else:
            print("No ingreso uno de esos numeros")
    letras_a_borrar=[]   
    for i in range(len(abecedario)):
        if i%int(usuario)==0:
            letras_a_borrar.append(abecedario[i])
    print(f"Las letras a borrar son: {letras_a_borrar}")

    for letra in letras_a_borrar:
        abecedario.remove(letra)
    print(f"La lista resultante quedaria de la siguiente forma: {abecedario}")

lista_abecedario()