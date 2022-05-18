"""
Crear clase GestorAutos que cuente con las siguientes funciones para un menu
1.   Crear auto, indicando tipo de auto y guardar en una lista
2.   Listar autos (presentandolos), indicando tipo de Vehiculo.
3.   Cambiar velocidad de un Vehiculo
4.   Calcular tiempo de viaje de un Vehiculo en una cant de Km pasados por parametro (tiempo = Km / Velocidad)
"""
import Vehiculos as vh
lista_vehiculos=[]

class GestorAutos:
    def __init__(self):#INSTANCIA PERO SIN ATRIBUTOS 
        pass

    def crear_vehiculos(self):
        #patente
        while True:
            patente=str(input("Ingrese la patente del vehiculo: ")).upper()
            break
        
        #marca
        while True:
            marca=input("Ingrese la marca del vehiculo: ").capitalize()
            if marca.isalpha():
                break
            else:
                print("Los datos no pueden contener simbolos")
            break

        #año
        while True:
            try:
                año=int(input("Ingrese el año: "))
                if año<=0:
                    print("El año no puede ser inferior o igual a 0")
                else:
                    break
            except:
                print("El año debe ser numerico")
        
        #origen
        while True:
            origen=input("Ingrese el origen: ").capitalize()
            if origen.isalpha():
                break
            else:
                print("Los datos no pueden contener simbolos")

        #menu para guardar los datos de cada vehiculo
        while True:
            opcion=input("""
            Ingrese una opcion para guardar los datos
            1.Particular
            2.PickUp
            3.Deportivo
            Opcion:
            """)
            if opcion=="1":
                nombre_instancia=vh.Particular(patente,marca,año,origen)
                break
            elif opcion=="2":
                nombre_instancia=vh.PickUp(patente,marca,año,origen)
                break
            elif opcion=="3":
                nombre_instancia=vh.Deportivo(patente,marca,año,origen)
                break
            else:
                print("Opcion incorrecta")
        
        lista_vehiculos.append(nombre_instancia)

    #Listar autos (presentandolos), indicando tipo de Vehiculo.
    def imprimir_lista(self):
        print(f"La longitud de la lista es de {len(lista_vehiculos)} ")
        contador=1
        for autos in lista_vehiculos:
            print(f" {contador}. ", end ="")
            autos.presentarse()
            autos.tipo_vehiculo()
            autos.obtener_velocidad_max()
            contador+=1

    #Cambiar velocidad de un vehiculo
    def modificar_velocidad(self):
        while True:
            self.imprimir_lista()
            patente_auto=str(input("Ingrese la patente del auto: ")).upper()
            for autos in lista_vehiculos:
                print(f"Patente vehiculo en la lista {autos.patente} vs {patente_auto}")
                if autos.patente==patente_auto:
                    #if(type(autos).__name__=!Vehiculos) PARA COMPARAR CON VEHICULO GENERICO 
                    while True:
                        try:
                            nueva_velocidad=int(input("Ingrese la nueva velocidad: "))
                            if nueva_velocidad>0:
                                autos.setear_velocidad_max(nueva_velocidad)
                            else:
                                print("La velocidad debe ser mayor a 0")
                            return
                        except:
                            print("No ingreso un valor numerico")
                else:
                    print("Patente no encontrada")

    #Calcular tiempo de viaje de un Vehiculo en una cant de Km pasados por parametro (tiempo = Km / Velocidad)
    def tiempo_viaje(self):
        while True:
            self.imprimir_lista()
            patente_auto=str(input("Ingrese la patente del auto: ")).upper()
            for autos in lista_vehiculos:
                print(f"Ingreso la patente {patente_auto} ")
                if autos.patente==patente_auto:
                    while True:
                        try:
                            km=int(input("Ingrese la cantidad de Kilometros: "))
                            print(f"""El vehiculo {autos.marca} con una velocidad de {autos.velocidad_max}
                             recorrera {km} km en un tiempo de {km/(autos.velocidad_max)}""")
                            return
                        except:
                            print("Ingrese datos numericos")
                else:
                    print("Patente no encontrada. Ingrese nuevamente la patente")


        
