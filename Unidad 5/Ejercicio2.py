while True:#despues vemos como salir
    try:
        numero_inicial=int(input("Ingrese un numero inicial:"))
        numero_limite=int(input("Ingrese un numero limite:"))     
    except:
        print("Dije un numero") 
    if(numero_inicial<numero_limite):   
        while numero_inicial<=numero_limite:
                print(numero_inicial) 
                numero_inicial+=1 
    else:
        print("El numero inicial debe ser menor al numero limite")