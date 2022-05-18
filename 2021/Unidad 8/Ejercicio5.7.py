"""##**Ejercicio 5.7 (Estadisiticas)**
El programa debe:
*   Simular un programa que calcule estadisticas
*   Pedir al usuario una serie de numeros enteros el 1 al 10 (verificar) y guardarlos en una lista, hasta que el usuario ingrese "fin"
*   Luego mostrar un menu con 4 opciones
  1.  Calcular promedio
  2.  Verificar cuantos numeros son menores que el numero indicado por el usuario
  3.  Verificar cuantos numeros son mayores o igual que el numero indicado por el usuario
  4.  Verificar si un numero que desee el usuario esta en la lista
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio"""

print("Programa para calcular estadisticas")


def pedir_numeros():
    lista_numeros=[]
    contador=1
    while True:
        usuario=input(f"Ingrese el {contador}° numero entre 1 al 10 o fin: ")
        if usuario!="fin":
            try:
                if int(usuario)>0 and int(usuario)<10:
                    lista_numeros.append(int(usuario))
                    contador+=1
                else:
                    print("Datos incorrectos")
            except:
                print("No ingreso un numero")
        else:
            break
    return lista_numeros   
#Calcular promedio
def promedios(lista_principal):
    suma_total=sum(lista_principal)
    total_numero=len(lista_principal)
    return round(suma_total/total_numero,2)

#Verificar cuantos numeros de la lista son menores que el numero indicado por el usuario
def cantidad_numeros_menores(lista_principal):
    while True:
        try:
            numero_comparar=int(input("Indique el numero a comparar:"))
            break
        except:
            print("Por favor ingrese un numero")
    contador=0       
    for i in lista_principal:
        if i<numero_comparar:
            contador+=1

    return contador

def verificar_numero_lista(lista_principal):
    while True:
        try:
            numero_a_verificar=int(input("Ingrese un numero a verificar:"))
            break
        except:
            print("Dato incorrecto")
    if numero_a_verificar in lista_principal:
        contador=True
        print(contador)
    else:
        contador=False
        print(contador)
    return contador


lista_principal=pedir_numeros()
print(lista_principal)
print(f"El promedio de la lista es: {promedios(lista_principal)}")
verificar_numero_lista(lista_principal)


