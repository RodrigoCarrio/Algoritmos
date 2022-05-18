class Persona:
    def __init__(self,dni,nombre,apellido):
        self.dni=dni
        self.nombre=nombre
        self.apellido=apellido
    
    def get_dni(self):
        return self.dni

    def set_dni(self,dni_nuevo):
        self.dni=dni_nuevo
        
class Empleado(Persona):
    def __init__(self, dni, nombre, apellido,funcion,año_ingreso):
        super().__init__(dni, nombre, apellido)
        self.funcion=funcion
        self.año_ingreso=año_ingreso

    def get_funcion(self):
        return self.funcion

    def get_fecha(self):
        return self.año_ingreso

    
    def set_funcion(self,nueva_funcion):
        self.funcion=nueva_funcion
        
    def imprimir_info_empleados(self):        
        print(f" DNI: {self.dni} - Empleado: {self.nombre} {self.apellido} - Funcion: {self.funcion} - Año de ingreso {self.fecha_ingreso} ")