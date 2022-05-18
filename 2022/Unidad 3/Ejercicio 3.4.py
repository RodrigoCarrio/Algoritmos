"""
Crear una clase Persona con atributos DNI, nombre, apellido encapsulados, 
    de tal forma de poder acceder y modificar los atributos unicamente 
        con metodos get y set utilizando el decorador property
"""
class Persona:
    def __init__(self,dni,nombre,apellido):
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido

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

persona_1=Persona(40030222,"rodri","carrio")
print(persona_1.apellido)
persona_1.apellido="suarez"
print(persona_1.apellido)

