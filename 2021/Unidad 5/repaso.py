flag=True
while flag:
    try:
        inicio=int(input("Ingrese un numero:"))
        limite=int(input("Ingrese otro numero:"))    
        if (inicio<limite):
            while inicio<=limite:
                print(inicio)
                inicio+=1
            flag=False
        else:
            print("El primer numero ingresado es mayor al ultimo")
    except:
        print("Error")

flag=True
while flag:
    try:
        num1=int(input("Ingrese un dato numerico:"))
        num2=int(input("Ingrese otro dato numerico:"))
        num3=int(input("Ingrese otro dato numerico:"))
        num4=int(input("Ingrese otro dato numerico:"))
        num5=int(input("Ingrese otro dato numerico:"))
        print(f"El promedio es: {(num1+num2+num3+num4+num5)/5} ")
        flag=False
    except:
        print("vuelva a ingresar los 5 datos numericos")

