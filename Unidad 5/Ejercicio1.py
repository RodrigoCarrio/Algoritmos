i=1
while i<=10:
    print(f"Numero: {i}")
    i+=1

i=1
try:
    palabra=str(input("Ingrese una palabra: "))
    numero=int(input("Ingrese cuantas veces desea mostrarla: "))
    while i<=numero:
        print(f"{palabra}")
        i+=1
except:
    print("ingreso datos incorrectos.")