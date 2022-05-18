"""
Crear clase GestorComputadora que cuente con las siguientes funciones para un menu
Crear Computadora, indicando tipo y guardar en una lista. Verificando marca y SO de una lista
Listar Computadoras (presentandolos), indicando tipo.
Cambiar SO de una Computadora, verificando una lista de SO disponibles
Listar perifericos
"""
import Computadoras as co
lista_computadoras=[]
lista_perifericos=[]

class GestorComputadoras:
    def __init__(self):
        pass

    def verificar_marca_so(self):
        pass

    def crear_computadora(self):
        id_modelo=input("Ingrese el modelo: ").upper()
        sistema_operativo=input("Indique el sistema operativo: ").capitalize()
        lista_perifericos=input("Ingrese un periferico si la computadora cuenta con uno: ")
        
        

        #menu para guardar los datos de cada computadora
        while True:
            opcion=input("""
            Ingrese una opcion para guardar los datos
            1.Escritorio
            2.Notebook
            Opcion:
            """)
            if opcion=="1":
                nombre_instancia=co.Escritorio(id_modelo,sistema_operativo,lista_perifericos)
                break
            elif opcion=="2":
                nombre_instancia=co.Notebook(id_modelo,sistema_operativo,lista_perifericos)
                break
            else:
                print("Opcion incorrecta")
    
        lista_computadoras.append(nombre_instancia)

    #Listar Computadoras (presentandolos), indicando tipo.
    def imprimir_lista(self):
        print(f"La longitud de la lista es de {len(lista_computadoras)} ")
        contador=1
        for compus in lista_computadoras:
            print(f" {contador}. ", end ="")
            compus.presentarse()
            compus.tipo_computadoras()
            contador+=1

    #Cambiar SO de una Computadora, verificando una lista de SO disponibles
    def cambio_so(self):
        while True:
            self.imprimir_lista()
            modelo=input("Ingrese el modelo de la computadora: ").upper()
            for compus in lista_computadoras:
                print(f"Modelo de la computadora en la lista {compus.id_modelo} vs {modelo}")
                if compus.id_modelo==modelo:
                    nuevo_so=input("Ingrese el nuevo sistema operativo: ")
                    compus.cambiar_so(nuevo_so)
                    return
                else:
                    print("No se encontro el modelo ingresado.")

    #Listar perifericos
    def listar_perifericos(self):
        print(f"Los perifericos son {self.listar_perifericos} ")
