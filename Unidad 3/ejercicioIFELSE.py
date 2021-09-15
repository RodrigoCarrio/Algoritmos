Ford=10000
Renault=11000
Chevrolet=15000
try:
    usuario=float(input("Ingrese su dinero disponible:"))
    if usuario >= Chevrolet:
        print("Usted puede comprar cualquier auto")
    elif usuario < Chevrolet and usuario>= Ford:
        print("Usted puede comprarse un ford o renault")
    else:          
        print("Usted no tiene dinero para comprar un auto")
except:
    print("Error")

