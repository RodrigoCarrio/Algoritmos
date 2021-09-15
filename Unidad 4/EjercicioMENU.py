try:
    condicion=input("Por favor ingrese una opcion\nimprimir\n1\n2\nsalir\n:")
    if condicion.isalpha():
        if condicion=="imprimir":   
            print("Elegiste imprimir")
        elif condicion=="salir":
            print("Gracias por salir")
        else:
            print("no ingresaste una opcion alfabetica correcta")
    elif condicion.isdigit():
        if int(condicion)==1:
            print("Ingresaste 1")
        elif int(condicion)==2:
            print("Ingresaste 2")
        else:
            print("No ingresaste una opcion numerica correcta")
    else:
        print("Ingresaste datos muy mal")        
except:
    print("Error")