"""*   Contar con 6 funciones disponibles en el menu **(estas funciones deben estar incluidas en una clase llamada GestorTaxis)*
    1. Crear instancias de choferes y guardarlos en una lista de choferes
    2. Crear instancias de Autos (verificando que haya choferes para ese auto) y guardarlos en una lista de autos
    3. Modificar el chofer de un auto
    4. Modificar el lugar de residencia del chofer indicando su nombre/dni?
    5. imprmiir lista de choferes (con toda su informacion)
    6. imprimir lista de autos (con toda su informacions)
    """
import Taxis as ta 
lista_choferes=[]
lista_autos=[]

class GestordeTaxis:
    def __init__(self):
        pass
    
    #Crear instancias de choferes(nombre,apellido,dni,fecha_nacimiento,residencia)
    def crear_choferes(self):
        #nombre
        while True:
            nombre=input("Ingrese el nombre del chofer: ").capitalize()
            if nombre.isalpha():
                break
            else:
                print("El nombre debe contener letras unicamente.")


        #apellido
        while True:
            apellido=input("Ingrese el apellido del chofer: ").capitalize()
            if apellido.isalpha():
                break
            else:
                print("El apellido debe contener letras unicamente.")

        #DNI:
        while True:
            flag=True   
            dni=input("Ingrese el DNI: ")
            for chofer in lista_choferes:
                if dni==chofer.get_dni(): #DUDA CON EL GET_DNI (PARA QUE SE CREA Y SE LLAMA ESTA FUNCION)
                    flag=False

            if (dni.isdigit() and len(dni)==8 and flag):
                break
            else:
                print("El dni son solo numeros y tienen que ser 8 numeros o ya existe")
                

        #Fecha de nacimiento
        fecha_nacimiento=input("Ingrese fecha de nacimiento DD/MM/AAAA: ")

        #residencia
        while True:
            residencia=input("Ingrese lugar de residencia: ").capitalize()
            if residencia.isalpha():
                break
            else:
                print("La residencia no debe contener simbolos o numeros")

        lista_choferes.append(ta.Chofer(nombre,apellido,dni,fecha_nacimiento,residencia))

    #Crear instancias de Autos (patente,modelo,año,marca,dni_chofer)
    def crear_autos(self):
        if len(lista_choferes)==0:
            print("Es necesario tener choferes")
            return

        while True:
            patente=input("Ingrese la patente, 3 letras o mas y 3 numeros: ").upper()
            # A continuacion, verificacion de si la patente contiene numeros y letras
            cont_letras=0
            cont_num=0
            for i in patente:
                if i.isdigit():
                    cont_num+=1
                elif i.isalpha():
                    cont_letras+=1
            if cont_letras>=3 and cont_num==3:
                break
            else:
                print("Vuelva a ingresar la patente correctamente")

        #modelo
        modelo=input("Ingrese el modelo del auto: ")

        #año
        año=input("Ingrese el año del auto: ")
        """if año.isnumeric():
            return
        else:
            print("El año debe contener numeros unicamente")"""

        #marca
        marca=input("Ingrese la marca del auto: ")
        """if marca.isalpha():
            return
        else:
            print("La marca del auto debe contener letras unicamente.")"""

        #A traves del dni que valido aca ? 
        self.imprimir_lista_chofer()

        while True:
            dni_chofer=input("Ingrese el dni del chofer: ")
            for chofer in lista_choferes:
                if dni_chofer==chofer.get_dni():
                    lista_autos.append(ta.Autos(patente,modelo,año,marca,dni_chofer))
                    return

    """def imprimir_info_choferes(self):
        for i in lista_choferes:
            i.imprimir_choferes()

    def imprimir_info_autos(self):
        for i in lista_autos:
            i.imprimir_autos()"""

    def imprimir_lista_autos(self):
        print(f"La longitud de la lista es de {len(lista_autos)} ")
        contador=1
        for autos in lista_autos:
            print(f" {contador}. ", end ="")
            autos.imprimir_autos()
            contador+=1

    def imprimir_lista_chofer(self):
        print(f"La longitud de la lista es de {len(lista_choferes)} ")
        contador=1
        for chofer in lista_choferes:
            print(f" {contador}. ", end ="")
            chofer.imprimir_choferes()
            contador+=1

    #Modificar el chofer de un auto
    def modificar_chofer_auto(self):
        self.imprimir_lista_autos()
        flag=True
        while flag:   
            patente=input("Ingrese la patente del auto: ")
            for autos in lista_autos:
                if patente==autos.get_patente():
                    flag=False

        flag=True
        self.imprimir_lista_chofer()
        while flag: 
            chofer=input("Ingrese el dni del chofer: ")
            if self.verificar_dni(chofer):
                for i in lista_choferes:
                    if chofer == i.get_dni():
                        flag=False
            else:
                print("Error en el formato de dni")

        for i in lista_autos:
            if patente== i.get_patente():
                i.set_chofer(chofer)

    #Modificar el lugar de residencia del chofer indicando su nombre/dni?               
    def modificar_residencia_chofer(self):
        self.imprimir_lista_chofer()
        while True:
            dni=input("Ingrese el dni del chofer: ")
            for chofer in lista_choferes:
                if dni==chofer.get_dni():
                    nueva_residencia=input("Ingrese la nueva residencia del chofer: ").capitalize()
                    chofer.modificar_residencia(nueva_residencia)
                    return
                else:
                    print("El dni ingresado no es correcto.")

    def verificar_dni(self,dni):
        if dni.isdigit() and len(dni)==8:
            return True