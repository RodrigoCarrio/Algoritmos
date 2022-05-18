"""
El programa debe:
*   Contar con una Clase Libro con los atributos (Id(unico), Nombre, Autor y estado (alquilado o no))
*   Contar con dos Clases Hijas que use el constructor de la clase padre pero que tenga un atributo mas:
        - LibroNiños (Atributo: edad_minima (por defecto = 11))
        - LibroIdiomas (Atributo: idioma_libro)

*   Se deben crear 4 metodos para la clase padre Libro (que heredaran las clases hijas):
        1. Presentarse: Que indique el Nombre, autor, año del libro y su estado 
        2. Indicar tipo de libro (tipo de clases heredadas o padre)
        3. Alquilar (Cambiaran el estado del libro a ALQUILADO)
        4. Devolver_alquiler (Cambiaran el estado del libro a No alquilado)
"""

class Libro:
    def __init__(self,id,nombre,autor,estado="No alquilado"):
        self.id=id
        self.nombre=nombre
        self.autor=autor
        self.estado=estado
    
    def presentarse(self):
        print(f"""Libro ID:{self.id},nombre: {self.nombre}, autor {self.autor} y su estado es {self.estado} """)

    def tipo_objeto(self):
        print(f"Soy un libro del tipo",type(self).__name__)

    def get_id(self):
        return self.id

    def alquilar(self):
        print(f"El estado del libro era: {self.estado}")
        self.estado = "Alquilado"
        print(f"El estado del libro ahora es: {self.estado}")

    def devolver_alquiler(self):
        self.estado = "No alquilado"
        print(f"El libro se devolvio y su estado se cambio a: {self.estado}")

    def get_estado(self):
        return self.estado

class LibroNiños(Libro):
    def __init__(self, id, nombre, autor,estado, edad_minima=11):
        super().__init__(id, nombre, autor, estado)
        self.edad_minima=edad_minima

class LibroIdiomas(Libro):
    def __init__(self, id, nombre, autor, idioma_libro, estado):
        super().__init__(id, nombre, autor, estado)
        self.idioma_libro=idioma_libro
