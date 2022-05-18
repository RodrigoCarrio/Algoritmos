"""
*   La Clase Animales tiene los atributos (nombre, tipo_animal, fecha_nacimiento,
         encargado_cuidar (Legajo de objeto empleado))
    *   Crear 3 clases que hereden de animal segun su sector del zoologico)
        1. AnimalesEnjaulados.
        2. AnimalesSueltos.
        3. AnimalesAcuaticos
"""
class Animales:
    def __init__(self,nombre,tipo_animal,fecha_nacimiento,encargado_cuidar):
        self.nombre=nombre
        self.tipo_animal=tipo_animal
        self.fecha_nacimiento=fecha_nacimiento
        self.encargado_cuidar=encargado_cuidar

    def tipo_objeto(self):
        print(f"Soy un animal del tipo",type(self).__name__)

    def set_empleado(self,encargado_cuidar):
        self.encargado_cuidar = encargado_cuidar

    def presentarse(self):
        print(f"Clase: {type(self).__name__} - Nombre: {self.nombre} - Nacimiento {self.fecha_nacimiento}")

class AnimalesEnjaulados(Animales):
    pass

class AnimalesSueltos(Animales):
    pass

class AnimalesAcuaticos(Animales):
    pass

class Empleados:
    def __init__(self,legajo,nombre,apellido,lista_animales_a_cuidar=[]):
        self.legajo=legajo
        self.nombre=nombre
        self.apellido=apellido
        self.lista_animales_a_cuidar=lista_animales_a_cuidar

    def asignar_animales(self,nuevo_animal):
        self.lista_animales_a_cuidar.append(nuevo_animal)
    
    def presentarse(self):
        print(f"{self.legajo} - {self.nombre} {self.apellido}")
        print("Cuida los siguientes animales")
        for i in self.lista_animales_a_cuidar:
            i.presentarse()

    def get_legajo(self):
        return self.legajo
        
"""
animal=Animales("rodri","felino","1/1/2020","pedro")
animal_marino=AnimalesAcuaticos("rodri2","felino","12/1/2020","pedro")
animal_jaula=AnimalesEnjaulados("rodri3","felino","15/1/2020","pedro")
animal_suelto=AnimalesSueltos("rodri4","felino","10/1/2020","pedro")

print(animal.nombre)
animal.tipo_objeto()
animal_marino.tipo_objeto()
animal_jaula.tipo_objeto()
animal_suelto.tipo_objeto()
"""