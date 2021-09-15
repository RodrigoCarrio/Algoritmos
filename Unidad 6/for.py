frase=input("Ingrese una frase:")
letra=input("Ingrese la letra que quiere contar")
contador=0
for i in frase:
    if i ==letra:
        contador+=1
print(f"El numero de veces de la letra: {letra} es {contador}")

