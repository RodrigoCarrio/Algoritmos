from datetime import datetime, time, date
import Persona as pe
lista_empleados=[]

class GestorPersonas:
    def __init__(self) -> None:
        pass

    def crear_empleados(self):
        #dni
        while True:
            flag=True   
            dni=input("Ingrese el DNI: ")
            for i in lista_empleados:
                if dni==i.get_dni(): 
                    flag=False

            if (dni.isdigit() and len(dni)==8 and flag):
                break
            else:
                print("El dni son solo 8 numeros o ya puede existir en el sistema")
        
        #nombre
        try:
            nombre=str(input("Ingrese el nombre: "))
        except:
            print("El nombre debe contener letras")

        #apellido           
        while True:
            apellido=input("Ingrese el apellido: ")
            if apellido.isalpha():
                break
            else:
                print("El apellido debe contener letras unicamente.")
        
        #funcion
        try:
            funcion=str(input("Ingrese la funcion: "))
        except:
            print("Error")

        #año de ingreso
        while True:
            try:
                año_ingreso=datetime.strptime(input("Ingrese el año de ingreso del empleado dd/mm/yyyy : "),
                                                    '%d/%m/%Y')
    
                break
            except:
                print("Error")
        
        lista_empleados.append(pe.Empleado(dni,nombre,apellido,funcion,año_ingreso))

    def eliminar_ultimo_empleado(self):
        print(f"La longitud de la lista es de {len(lista_empleados)} ")
        lista_empleados.pop()
        print(f"Ahora la longitud de la lista es de {len(lista_empleados)} ")

    def info_empleados(self):
        for i in lista_empleados:
            i.imprimir_info_empleados()

    def ordenar_por_fecha_me_a_mayor(self):
        lista_aux_ordenada = []
        global lista_empleados #habia que declarar la lista como global para obtener elementos
        while( len(lista_empleados)>0):
            objeto_menor = lista_empleados[0]
            for empleado in lista_empleados:
                if (empleado.get_fecha() < objeto_menor.get_fecha()):
                    objeto_menor = empleado
            
            lista_aux_ordenada.append(objeto_menor)#agrego el menor a la lista
            lista_empleados.remove(objeto_menor)
        
        lista_empleados = lista_aux_ordenada
        self.imprimir_info_empleados()

        """ #codigo que se intento hacer en clase
        lista_aux_ordenada=[]
        objeto_menor=lista_empleados[0]

        while(len(lista_empleados)>0):
            for empleado in lista_empleados:
                if (empleado.get_fecha()< objeto_menor.get_fecha()):
                    objeto_menor=empleado
                    
            
            lista_aux_ordenada.append(objeto_menor)#agrego el menor a la lista
            lista_empleados.remove(objeto_menor)
        
        lista_empleados=lista_aux_ordenada
        self.imprimir_info_empleados()
        """

