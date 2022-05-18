"""
*   Cuyo constructor debe inicializar los atributos nombre, apellido, edad, ciudad_de_recidencia
*   Se deben crear dos metodos en la clase:
    1.  Presentarse que la persona indique: Soy {nombre} {apellido}, tengo {edad} años y vivo en 
        {ciudad de recidencia}
    2.  Indique segun la edad de la persona si esta es: Niño (0 a 14), Adolecente (14 a 22),
         Joven (22 a 30), mayor(30 a 50), mas mayor(50 a 120)"""

class Persona:
    nacionalidad="argentina"
    #constructor
    def __init__(self,nombre,apellido,edad,residencia,DNI):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.residencia = residencia
        self.dni=DNI #unico

    def presentacion(self):
        print(f"""Soy {self.nombre} {self.apellido}, tengo {self.edad} años,
         vivo en {self.residencia} y mi nacionalidad es {self.nacionalidad} """)

    def indicar_edad(self):
        if(self.edad > 0 and self.edad < 14):
            print(f"{self.nombre} es un niño")
        elif(self.edad >= 14 and self.edad <= 22):
            print(f"{self.nombre} es un adolescente")
        elif(self.edad > 22 and self.edad < 30):
            print(f"{self.nombre} es un joven")
        elif(self.edad >= 30 and self.edad <= 50):
            print(f"{self.nombre} es un mayor")
        else:
            print(f"{self.nombre} es muy mayor")
        