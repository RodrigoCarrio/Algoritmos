while True:
    try:
        pesos=int(input("Ingrese cantidad de pesos a convertir:"))
        print(f"La cantidad de ${pesos} es de {pesos/182} USD ")
        break
    except:
        print("No ingreso un numero")