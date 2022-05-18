"""
*   Contar con 6 funciones disponibles en el menu **(estas funciones deben estar incluidas en una clase llamada GestorZoologico)**:
    1. Crear instancias de animales (se puede elegir entre los tres sectores)  y guardarlos en una lista
    2. Crear instancia de Empleados y guardarlos en una lista
        * Los empleados se les pueden asignar animales luego, los animales al crearlos en el sistema tienen q contar siosi con un encargado
    3. Asignar a un empleado un animal a cuidar
    4. Cambiar de encargado un animal
    5. imprmiir lista de animales (con toda su informacions)
    6. imprimir lista de Empleados (con toda su informacions)
"""
import Zoologico as zo
lista_empleados=[]

class GestorDelZoologico:

    #Crear instancia de Empleados
    def crear_empleado(self):
        #legajo
        flag=True
        while flag:
            legajo=input("Ingrese un legajo: ")
            for i in lista_empleados:
                if legajo==i.get_legajo() :
                    print("El legajo debe ser unico")
                return

        
        #nombre
        nombre=input("Ingrese el nombre: ")

        #apellido
        apellido=input("Ingrese el apellido: ")

        lista_empleados.append(zo.Empleados(legajo,nombre,apellido))

    def imprimir_empleado(self):
        for i in lista_empleados:
            i.presentarse()