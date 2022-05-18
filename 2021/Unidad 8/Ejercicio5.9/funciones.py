
taxis=[["auto_1","auto_2","auto_3"],["chofer_1","chofer_2","chofer_3"],[45,50,30]]

def listar():
    print(f"AUTO - CHOFER - RECORRIDO ")
    for i in range(len(taxis[0])):
        print(f"{taxis[0][i]} - {taxis[1][i]} - {taxis[2][i]}")

def recorrido_viaje(): #funcion rodri(igual que gustavo)
    while True:
        try:
            distancia=float(input("Ingrese la distancia del viaje a recorrer: "))
            if (distancia<=0):
                print("La distancia debe ser mayor a cero")
            else:
                print("Posible autos que podrian realizar el viaje: ")
                for columnas in range (len(taxis[2])):
                    if (distancia<=taxis[2][columnas]):
                        print(f"Auto: {taxis[0][columnas]} - Chofer: {taxis[1][columnas]}")
                        return
                    else:
                        if (distancia>taxis[2][columnas]):
                            print("La distancia ingresada es mayor a los recorridos posibles")
                return

        except:
            print("Debe ingresar una distancia valida")

def change_name():
    listar()
    print(f"SE PROCEDERA A CAMBIAR EL NOMBRE DEL CHOFER")
    while True:
        opcion=input("Ingrese nombre del auto a modificar: ")
        if opcion in taxis[0]:
            taxis[1][taxis[0].index(opcion)]=input("Nuevo nombre del chofer: ")
            listar()
            break
        else:
            print("No existe ese auto")

def change_ruta():
    listar()
    print(f"SE PROCEDERA A CAMBIAR EL RECORRIDO")
    while True:
        ruta_nueva=input("Ingrese nombre del auto: ")
        if ruta_nueva in taxis[0]:
            taxis[2][taxis[0].index(ruta_nueva)]=input("Nuevo recorrido del auto: ")
            listar()
            break
        else:
            print("No existe ese auto")
     

def nuevo_viaje(): #funcion de gustavo
    while True:
        try:
            while True:
                distancia = float(input("Ingrese la distancia del viaje:"))
                if(distancia <= 0):
                    print("La distancia debe ser mayor que cero")
                else:
                    print("Posibles autos que podrían realizar el viaje:")
                    for columnas in range(len(Taxis)):
                        if(distancia <= Taxis[2][columnas]):
                            print(f"Auto: {Taxis[0][columnas]} - Chofer: {Taxis[1][columnas]}")
                    return
        except:
            print("Debe ingresar una distancia válida")

def informacion_chofer():
    chofer=input("Por favor ingrese el nombre del chofer: ")
    if chofer.isalpha():
        if chofer in taxis[1]:
            print(f"El chofer maneja el {taxis[0][taxis[1].index(chofer)]} y hace {taxis[2][taxis[1].index(chofer)]} kilometros. ")
        else:
            print(f" {chofer} no trabaja en esta empresa. ")

def agregar_nuevo_auto():
    while True:
        listar()
        name_new_car=input("Ingrese el nuevo auto a añadir: ")
        if name_new_car not in taxis[0]:
            taxis.append(name_new_car)
            print(taxis)
            break            
        else:
            print("El auto ingresado ya se encuentra")
        


#listar()        
#recorrido_viaje()
#change_name()
#change_ruta()
agregar_nuevo_auto()
