duracion=[]
print("Programa para calcular tiempo total")
while True:
    try:
        tramos=int(input("Ingrese cantidad de tramos de su viaje:"))
        for i in range(tramos):
            duracion.append(int(input("Ingrese cantidad de minutos de cada tramo:")))
        """duracion_total=0 
        for i in range(tramos): 
            duracion_total=duracion_total+duracion[i]
        print(f"El tiempo total del viaje es de:{duracion_total}")"""
        print(f"El tiempo total del viaje es de:{sum(duracion)} minutos")
        break
    except:
        print("Error")