"""
###**Ejercicio 3.5**
Crear una clase Persona unicamente con metodos estaticos.

Los metodos a crear son:

- calcular_edad, parametro (año_nacimiento)
- calcular_peso_promedio, parametro (estatura,genero) [Ayuda](https://www.zonadiet.com/tablas/pesoideal.cgi)
- calcular_IMC,  parametro (peso,estatura) [Ayuda](https://www.mundodeportivo.com/uncomo/deporte/articulo/como-calcular-el-indice-de-masa-corporal-7050.html)

Crear un menu para probar todos los requerimientos
"""
from datetime import date,time,datetime

class Persona:
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
        try:
            return peso/(estatura/100)**2
        except:
            print("Error")

"""try:
    peso=int(input("Ingrese el peso: "))
    estatura=int(input("Ingrese la estatura: "))
except:
            print("Error")

print(f"El IMC={Persona.calcular_IMC(peso,estatura)}")
"""
print(Persona.calcular_edad("24/02/1997"))
