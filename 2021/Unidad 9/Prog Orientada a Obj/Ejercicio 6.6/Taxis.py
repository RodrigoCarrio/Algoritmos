"""
*   La Clase auto tiene los atributos (patente, modelo, año, marca, nombre_Chofer (objeto clase Choferes))
*   La Clase Chofer tiene los atributos (nombre, apellido, dni, fecha nacimiento, Residencia)
"""
class Chofer:
    def __init__(self,nombre,apellido,dni,fecha_nacimiento,residencia):
        
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.fecha_nacimiento=fecha_nacimiento
        self.residencia=residencia

    def imprimir_choferes(self):
        print(f"Nombre/apellido: {self.get_nombre()}/{self.apellido}, dni:{self.get_dni()}, fecha de nacimiento:{self.fecha_nacimiento}, residencia:{self.residencia}")

    def modificar_residencia(self,nueva_residencia):
        print(f"Se cambio de residencia: {self.residencia} a {nueva_residencia} ")
        self.residencia=nueva_residencia

    def get_nombre(self):
        return self.nombre

    def get_dni(self):
        return self.dni

    def set_nombre(self,nuevo_nombre):
        self.nombre=nuevo_nombre

class Autos:
    def __init__(self,patente,modelo,año,marca,dni_chofer):
        self.patente=patente
        self.modelo=modelo
        self.año=año
        self.marca=marca
        self.dni_chofer=dni_chofer

    def get_patente(self):
        return self.patente

    def get_chofer(self):
        return self.dni_chofer

    def set_chofer(self,dni_chofer):
        self.dni_chofer= dni_chofer

    def imprimir_autos(self):
        print(f"Patente: {self.patente}, año {self.año}, marca/modelo: {self.marca}/{self.modelo}, chofer: {self.get_chofer()} ")