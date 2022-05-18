"""
###**Ejercicio 6.4**
Crear una clase padre Vehiculos:
*   Constructor debe incluir los atributos (patente,marca,año,origen)
*   Crear metodos para esta clase de:
    1.  Presentarse (patente,marca,año,origen)
    2.  Indicar tipos de vehiculo(Clases heredadas)
    3.  Metodos que luego modificarán las clases hijas. Acelerar, 
     Retroceder, obtener_velocidad, setear_velocidad
    """
class Vehiculos:
    def __init__(self,patente,marca,año,origen):
        self.patente=patente
        self.marca=marca
        self.año=año
        self.origen=origen
    
    def presentarse(self):
        print(f"""Soy un vehiculo con patente {self.patente}, marca {self.marca},
         año {self.año} y de origen {self.origen} """)

    def tipo_vehiculo(self):
        print("Soy un vehiculo del tipo",type(self).__name__)

    def acelerar(self):
        pass

    def Retroceder(self):
        pass
    
    def obtener_velocidad_max(self):
        pass

    def setear_velocidad_max(self):
        pass

class Particular(Vehiculos):
    def __init__(self,patente,marca,año,origen,velocidad_max=130): #velocidad por defecto
        super().__init__(patente,marca,año,origen)
        self.velocidad_max=velocidad_max
        
    def acelerar(self):
        print("Estoy acelerando")

    def Retroceder(self):
        print("Estoy retrocediendo")
    
    def obtener_velocidad_max(self):
        print(f"La velocidad maxima es {self.velocidad_max} ")

    def setear_velocidad_max(self,velocidad_max_nueva):
        print(f"La velocidad maxima era {self.velocidad_max} y ahora es de {velocidad_max_nueva} ")
        self.velocidad_max=velocidad_max_nueva
        
class PickUp(Vehiculos):
    def __init__(self, patente,marca,año,origen,velocidad_max=180):
        super().__init__(patente,marca,año,origen)
        self.velocidad_max=velocidad_max
    
    def acelerar(self):
        print("Estoy acelerando VPU")
 
    def retroceder(self):
        print("Estoy retrocediendo VPU")
 
    def obtener_velocidad_max(self):
        print(f"La velocidad maxima es {self.velocidad_max}")
 
    def setear_velocidad_max(self, velocidad_max_nueva):
        print (f"La velocidad maxima era {self.velocidad_max} y ahora es {velocidad_max_nueva}")
        self.velocidad_max = velocidad_max_nueva

class Deportivo(Vehiculos):
    def __init__(self,patente,marca,año,origen,velocidad_max=240):
        super().__init__(patente,marca,año,origen)
        self.velocidad_max=velocidad_max

    def acelerar(self):
        print("Estoy acelerando VD")
 
    def retroceder(self):
        print("Estoy retrocediendo VD")
 
    def obtener_velocidad_max(self):
        print(f"La velocidad maxima es {self.velocidad_max}")
 
    def setear_velocidad_max(self, velocidad_max_nueva):
        print (f"La velocidad maxima era {self.velocidad_max} y ahora es {velocidad_max_nueva}")
        self.velocidad_max = velocidad_max_nueva