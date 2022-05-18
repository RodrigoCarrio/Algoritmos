"""
###**Ejercicio 3.6**
Crear una clase Persona con metodos estaticos, de clase y de instancia.
- Tiene que tener un atributo de clase: Nacionalidad

Los metodos a crear son:
- Conctructor con atributos DNI, nombre, apellido
-  **Metodos de clase:** set y get nacionalidad
-  **Metodos de intancia:** setters y getters, crear con @propierty
-  **Metodos estaticos:** ejercicio anterior

Crear un menu para probar todos los requerimientos
"""
from datetime import date,time,datetime


class Persona:
    nacionalidad= "Argentina"

    def __init__(self,dni,nombre,apellido):
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido

    #METODOS DE INSTANCIA
    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self,nuevo_dni):
        self.__dni=nuevo_dni

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,otro_nombre):
        self.__nombre=otro_nombre

    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self,otro_apellido):
        self.__apellido=otro_apellido

    #METODOS DE CLASE
    @classmethod
    def get_nacionalidad(cls):
        return cls.nacionalidad

    @classmethod
    def set_nacionalidad(cls,nueva_nacionalidad):
        cls.nacionalidad=nueva_nacionalidad

    #METODOS ESTATICOS
    @staticmethod
    def calcular_edad(fecha_nacimiento):
        now=datetime.now()
        fecha=datetime.strptime(fecha_nacimiento,"%d/%m/%Y")
        return (now-fecha)/365

    @staticmethod
    def calcular_peso_promedio(estatura,genero):
        pass

    @staticmethod
    def calcular_IMC(peso,estatura):
        return peso/(estatura/100)**2
        