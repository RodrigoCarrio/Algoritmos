try:
    numero=int(input("Ingrese un numero:"))
    if numero < 0:
        print("Pedi un numero positivo")
    else:
        print("Soy un numero positivo")

    print(f"El numero que ingresaste fue:{numero}")
except:
    print("No ingreso un numero")
