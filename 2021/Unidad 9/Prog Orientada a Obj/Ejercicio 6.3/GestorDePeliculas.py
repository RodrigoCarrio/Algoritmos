"""
El programa debe:
*   Tener un menu con 7 opciones:
    1. Crear una pelicula y guardar su nombre en una lista de peliculas.
    2. Verificar si la pelicula deseada existe en la lista de peliculas.
    3. Pedir a la lista de peliculas, todas las de un año.
    4. Presentar una pelicula de la lista
    5. Cambiar el genero de una pelicula
    6. Verificar año pelicula
    7. Modificar puntuacion de la pelicula (entre 1 y 10)
"""
import Pelicula as pl
lista_peliculas=[] #EMPIEZA VACIA
lista_generos=["Comedia","Accion","Drama","Terror","Suspenso","Ciencia Ficcion","Infantil"]

class GestorDePeliculas:
    def __init__(self):#INSTANCIA PERO SIN ATRIBUTOS 
        pass

    

    def imprimir_lista(self):
        print(f"La longitud de la lista es de {len(lista_peliculas)} ")
        contador=1
        for peliculas in lista_peliculas:
            print(f" {contador}. ", end ="")
            peliculas.presentar_pelicula()
            contador+=1

    def virificar_pelicula(self,nombre_pelicula="null"):#dentro del metodo crear pelicula
        while True:
            if (nombre_pelicula=="null"):
                nombre_pelicula=input("Ingrese el nombre de la pelicula a verificar").capitalize()
            
            for peliculas in lista_peliculas:
                if nombre_pelicula==peliculas.nombre:
                    print("Esta pelicula ya existe")
                    return True
            
            print("Esta pelicula no existe")
            return False

        

    def crear_peliculas(self):
        #nombre
        while True:
            nombre=input("Ingrese el nombre de la pelicula: ").capitalize()
            if self.virificar_pelicula(nombre)== False: #True --> LA PELICULA EXISTE , FALSE LA PELICULA NO EXISTE
                break        

        #año
        while True:
            try:
                año=int(input("Ingrese el año: "))
                if año<=0:
                    print("El año no puede ser menor o igual a 0")
                else:
                    break
            except:
                print("Error en los argumentos")

        #genero
        while True:
            genero=input("Ingrese el genero: ")
            if genero in lista_generos:
                break
            else:
                print("Reintentar, el genero no se encuentra registrado en el sistema")
        
        #nacionalidad
        while True:
            nacionalidad=input("Ingrese la nacionalidad: ").capitalize()
            if nacionalidad.isalpha():
                break
            else:
                print("La nacionalidad no puede tener simbolos")
        
        #puntuacion
        while True:
            try:
                puntuacion=int(input("Ingrese la puntuacion: "))
                if puntuacion>0 and puntuacion<=10:
                    break   
                else:
                    print("La puntuacion debe estar entre 1 y 10")
            except:
                print("Error en los argumentos")
        
        nombre_instancia=pl.Peliculas(nombre,año,genero,nacionalidad,puntuacion)

        lista_peliculas.append(nombre_instancia)
    
    #Pedir a la lista de peliculas, todas las de un año.
    def año_pelicula(self):
        while True:
            try:
                año=int(input("Ingrese el año: "))
                break
            except:
                print("El año es numerico")

        flag=False
        for peliculas in lista_peliculas:
            if peliculas.año==año:
                print(peliculas.nombre)
                flag=True

        if flag==False:
            print("No existe ninguna pelicula en ese año")

    #Cambiar el genero de una pelicula                       
    def nuevo_genero(self):
        while True:
            self.imprimir_lista()
            nuevo_nombre = input("Por favor ingrese el NOMBRE de la pelicula o 0 para salir: ").capitalize()
            #si el usuario ingreso cero me voy del metodo
            if nuevo_nombre== "0":
                return
 
            for pelicula in lista_peliculas: #reocorro la lista de peliculas
                print(f"nombre pelicula en la lista {pelicula.nombre} vs {nuevo_nombre}")
                if pelicula.nombre == nuevo_nombre:
                    while True:
                        nuevo_genero = input("Ingrese el nuevo Genero de la Pelicula: ").capitalize()
                        if nuevo_genero in lista_generos: #verificamos que el genero este dentro de la lista
                            if pelicula.genero == nuevo_genero:
                                print("La pelicula ya posee ese genero")
                            else:
                                pelicula.cambio_genero(nuevo_genero)  
                            return
                        else:
                            print("Por favor ingrese un genero de la lista")
                            print(lista_generos)

    #Modificar puntuacion de la pelicula (entre 1 y 10)                
    def modificar_puntuacion(self):
        while True:
            self.imprimir_lista()
            nombre_pelicula=input("Por favor ingrese el NOMBRE de la pelicula o 0 para salir: ").capitalize()
            if nombre_pelicula== "0":
                return

            for pelicula in lista_peliculas:
                print(f"nombre pelicula en la lista {pelicula.nombre} vs {nombre_pelicula}")
                if pelicula.nombre==nombre_pelicula:
                    while True:
                        try:
                            nueva_puntuacion=int(input("Ingrese nueva puntuacion entre 1 y 10: "))
                            if nueva_puntuacion>0 and nueva_puntuacion<=10:
                                pelicula.cambio_puntuacion(nueva_puntuacion) #NO LLAME AL METODO CAMBIO_PUNTUACION DE LA CLASE PELICULA
                                print(f"Se modifico la puntuacion a {nueva_puntuacion} ")
                            else:
                                print("La puntuacion debe estar entre 1 y 10")
                            return
                        except:
                            print("La puntuacion debe ser numerica")

    #Verificar año pelicula
    def verificar_año_pelicula(self):
        self.imprimir_lista()
        nombre_pelicula=input("Por favor ingrese el NOMBRE de la pelicula: ").capitalize()
        for pelicula in lista_peliculas:
            if pelicula.nombre==nombre_pelicula:
                print(f"La pelicula ingresada es en el año {pelicula.año} ")