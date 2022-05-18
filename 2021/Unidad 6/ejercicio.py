inversion=int(input("Cantidad a invertir:"))
interes=float(input("Interes anual:"))
años=int(input("Años:"))
for i in range(1,años+1):
    inversion+=inversion*interes/100
    print(f"El capital obtenido en el año {i} es de ${inversion}")