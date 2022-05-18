while True:
    palabra=input("ingrese una palabra:")
    if palabra=="salir":
        print(palabra)
        break
    elif palabra=="hola" or "chau":
        continue
    else:
        print("ingrese otra palabra")

