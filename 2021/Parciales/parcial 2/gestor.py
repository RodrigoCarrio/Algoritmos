"""
*   Se debe crear una clase GestorEvento que cuente con las siguientes funciones para un menu:

    1.  Crear instancias de un evento y guárdalos en una lista de eventos. 
        1.1) Se debe verificar que tipo de instancia de evento a crear y los parámetros. IMPORTANTE!: clase hijas verificar y pedir parámetros
             - nombre_evento: debe ser único
             - Fecha: formato (dd/mm/yyyy) -> únicamente verificar la longitud del string = 10 
             - Hora: formato (hh:mm) -> no es necesario verificar
             - Lugar: sin formato especifico, no es necesario verificar
        1.2) Al crear un evento es necesario logearlo (Escribir en una línea nueva: nombre_evento-Fecha-Hora-Lugar-Tipo_de_evento(tipo de clase)) 
             en un archivo llamado lista_eventos.txt (Crear función en el mismo gestor). IMPORTANTE!: verificar permisos
        1.3) En caso que la instancia del evento sea EventoPersonal.
             - Para el organizador, el usuario debe elegir a través de una clave (mostradas por el programa) 
                desde un diccionario de organizadores.
             - En caso que no exista el organizador deseado debe ser "incognito" (AYUDA: Funcion get de diccionarios)
    2.   Listar eventos disponibles, leyendo la lista_evetos.txt. IMPORTANTE!: recorrer el archivo, no la lista. 
    3.   Cambiar el lugar de un evento, seleccionando su nombre. (Hacer check correspondientes)
    
*   Se deben crear los métodos correspondientes para las funciones del menú en las clases correspondientes
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
"""
import clase as cl

import os
path = os.path.abspath(os.path.dirname(__file__))

lista_eventos=[]

organizadores = {
    "FA":"familia", 
    "AM": "amigos",
    "PR": "propio"
    }

class GestorEvento:
    def __init__(self) -> None:
        pass

    def crear_evento(self):
        flag=True
        while True:
            nombre_evento=input("Ingrese el nombre del evento: ")
            for i in lista_eventos:
                if nombre_evento==i.get_lugar():
                    print("Nombre ya existente")
                    flag=False
                    break
            if flag:
                break

        while True:
            fecha=input("Ingrese la fecha (dd/mm/yyyy): ")
            if len(fecha)==10:
                    break
            else:
                print("La fecha tiene que ser numeros")

        hora=input("Ingrese la hora (hh:mm): ")
        lugar=input("Ingrese el lugar: ")

        #menu para guardar los datos del evento
        while True:
            opcion=input("""
            Ingrese una opcion para guardar los datos
            1. Evento
            2. Evento Personal
            3. Evento Laboral
            Opcion:
            """)
            if opcion=="1":
                nombre_instancia=cl.Evento(nombre_evento,fecha,hora,lugar)
                print("Evento agregado con exito!")
                self.loguear_evento(nombre_evento,fecha,hora,lugar)
                break
            elif opcion=="2":
                nombre_instancia=cl.EventoPersonal(nombre_evento,fecha,hora,lugar,self.organizador_evento())
                print("Evento agregado con exito!")
                self.loguear_evento(nombre_evento,fecha,hora,lugar)
                break
            elif opcion=="3":
                nombre_instancia=cl.Evento(nombre_evento,fecha,hora,lugar)
                print("Evento agregado con exito!!!")
                self.loguear_evento(nombre_evento,fecha,hora,lugar)
                break
            else:
                print("Opcion incorrecta")

        lista_eventos.append(nombre_instancia)
                    

    def loguear_evento(self,nombre_evento,fecha,hora,lugar,tipo_evento):
        try:
            fichero = open("lista_eventos.txt", "a")
            fichero.write(f"{nombre_evento}-{fecha}-{hora}-{lugar}- {tipo_evento} ")
            fichero.close()
        except:
            print("El archivo no existe.")

    def organizador_evento(self):
        print(organizadores.items())
        for i, j in organizadores.items():
            print(f"Key: {i} - Valor: {j}")
        organizador=input("Ingrese el simbolo: ")
        print(organizadores.get(organizador,"incognito"))


    def modificar_lugar_evento(self):
        #self.imprimir_lista_chofer()
        while True:
            nombre=input("Ingrese el nombre del evento: ")
            for i in lista_eventos:
                if nombre==i.get_lugar():
                    lugar_nuevo=input("Ingrese el nuevo lugar del evento: ")
                    i.set_lugar(lugar_nuevo)
                    return
                else:
                    print("El dni ingresado no es correcto.")

    def leer_archivo(self):
        try:
            fichero=open("lista_eventos.txt", "r")
            while True:
                linea=fichero.readline()
                if linea=="":
                    break
                print(linea,end="")
            fichero.close()
        except:
            print("Error")