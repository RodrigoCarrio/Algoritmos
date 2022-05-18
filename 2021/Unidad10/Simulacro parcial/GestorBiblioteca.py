"""
*   Se debe crear una clase GestorBiblioteca que cuente con las siguientes funciones para un menu:

    1.  Crear instancias de libros y guardalos en una lista de libros. 
        1.1) Se debe verificar que tipo de instancia de libro crear y los parametros
             - Id debe ser unico, se comienza del 1                                                                                             --->
             - Nombre y autor no es necesario                                                                                                   ---> 
             - estado debe comenzar "No alquilado"                                                                                              --->
        1.2) Al crear un libro es necesario logearlo (Escribir en una linea nueva: id-nombre-autor)                                             --->                         
             en un archivo llamado libros.txt (Crear funcion en el mismo gestor)                                                                --->
        1.3) En caso que la instancia del libro sea LibroIdiomas.                                                                               
             - El usuario  debe elegir a travez de una clave (mostradas por el programa) desde un diccionario de idiomas.                       --->
             - En caso que no exista el idioma deseado debe ser en idioma "español" (AYUDA: Funcion get de diccionarios)                        --->
    2.   Listar libros disponibles (recorrer la lista, no el archivo)                                                                           ---> 
    3.   Cambiar el estado (Alquilar o devolver) de un libro, seleccionando su id. (Hacer check correspondientes)                               --->
"""

import libro as lb
lista_libros=[]
idiomas = {
    "IN":"ingles", 
    "AL": "aleman",
    "CH":  "chino"
    }

class GestorBiblioteca:
    def __init__(self):
        pass

    def crear_libros(self):
        #id
        
        #while True:
            #flag=True  
            #id=input("Ingrese el id: ")
        tamaño_lista_libro=len(lista_libros)
        id=int(tamaño_lista_libro+1)

        """for i in lista_libros:
                if id==i.get_id():
                    flag=False

            if (id.isdigit() and len(id)==8 and flag):
                break
            else:
                print("El id son solo numeros y tienen que ser 8 numeros o ya existe")"""

        #nombre
        while True:
            nombre=input("Ingrese el nombre del libro: ").capitalize()
            if nombre.isalpha():
                break
            else:
                print("El nombre debe contener letras unicamente.")

        #Autor
        while True:
            autor=input("Ingrese el nombre del autor: ").capitalize()
            if autor.isalpha():
                break
            else:
                print("El nombre debe contener letras unicamente.")


        #menu para guardar los datos de cada libro
        while True:
            opcion=input("""
            Ingrese una opcion para guardar los datos
            1.Libro
            2.Libro Niños
            3.LibroIdiomas
            Opcion:
            """)
            if opcion=="1":
                nombre_instancia=lb.Libro(id,nombre,autor,estado="No alquilado")
                print("Libro agregado con exito!!!")
                self.loguear_libro(nombre)
                break
            elif opcion=="2":
                nombre_instancia=lb.LibroNiños(id,nombre,autor,estado="No alquilado")
                print("Libro agregado con exito!!!")
                self.loguear_libro(nombre)
                break
            elif opcion=="3":
                nombre_instancia=lb.LibroIdiomas(id,nombre,autor,self.idioma_libro(),estado="No alquilado")
                print("Libro agregado con exito!!!")
                self.loguear_libro(nombre)
                break
            else:
                print("Opcion incorrecta")
        
        lista_libros.append(nombre_instancia)

    #Listar libros (presentandolos), indicando tipo de libro.
    def imprimir_lista(self):
        print(f"La longitud de la lista es de {len(lista_libros)} ")
        contador=1
        for libros in lista_libros:
            print(f" {contador}. ", end ="")
            libros.presentarse()
            libros.tipo_objeto()
            contador+=1

    def idioma_libro(self):
        print(idiomas.items())
        for i, j in idiomas.items():
            print(f"Key: {i} - Valor: {j}")
        idioma=input("Ingrese el simbolo: ")
        print(idiomas.get(idioma,"español"))

    def loguear_libro(self, nombre):
        try:
            fichero=open("libros.txt", "a")
            fichero.write(f"{nombre}\n")
            fichero.close
        except:
            print("Error con el archivo")

    def cambiar_estado(self):
        if len(lista_libros) == 0:
            print("No hay libros en el sistema.")
            return
        while True:
            opcion = input("""
            Ingrese
            1. Para alquilar un libro.
            2. Para devolver un libro.
            Opcion: """)
            if opcion == "1":
                id_a_verificar =int(input("Ingrese el ID del libro que desea alquilar: "))
                for i in lista_libros:
                    if id_a_verificar == i.get_id() and i.get_estado() == "No alquilado":
                        i.alquilar()
                        return
                    else:
                        print("El libro ya se encuentra alquilado o no se encuentra registado.")
                        return
            elif opcion == "2":
                id_a_verificar =int(input("Ingrese el ID del libro que desea devolver: "))
                for i in lista_libros:
                    if id_a_verificar == i.get_id() and i.get_estado() == "Alquilado":
                        i.devolver_alquiler()
                        return
                    else:
                        print("El libro ya se encuentra alquilado o no se encuentra registado.")
                        return    
            else:
                print("Reintentar, pcion ingresada incorrecta.")