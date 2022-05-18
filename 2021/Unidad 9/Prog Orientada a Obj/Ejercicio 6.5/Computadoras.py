"""
Crear una clase padre Computadoras:
*   Constructor debe incluir los atributos (id_modelo,listaPerifericos,SO)
*   Crear metodos para esta clase de:
    1.  Presentarse (id_modelo,listaPerifericos,SO)
    2.  Indicar tipo de Computadora (Clases heredadas)
    3.  Metodos que luego modificarán las clases hijas. agregar_perifericos,CambiarSO
"""
class Computadoras:
    def __init__(self,id_modelo,sistema_operativo,lista_perifericos):
        self.id_modelo=id_modelo
        self.sistema_operativo=sistema_operativo
        self.lista_perifericos=lista_perifericos

    def presentarse(self):
        print(f"""Soy una computadora de modelo {self.id_modelo} de la lista {self.lista_perifericos} 
         y con el sistema operativo {self.sistema_operativo} """)
    
    def tipo_computadoras(self):
        print("Soy una computadora del tipo",type(self).__name__)
    
    def agregar_perifericos(self):
        pass

    def cambiar_so(self):
        pass

class Escritorio(Computadoras):
    def __init__(self,id_modelo,sistema_operativo,lista_perifericos,marca="Samsung"):
        super().__init__(id_modelo,sistema_operativo,lista_perifericos=lista_perifericos)
        self.marca=marca

    def agregar_perifericos(self,nuevo_periferico):
        print(f"Los periféricos que tiene la Computadora de Escritorio son {self.lista_perifericos}")
        self.lista_perifericos.append(nuevo_periferico)

    def cambiar_so(self,nuevo_so):
        print (f"El SO de la computadora Escritorio era {self.sistema_operativo} y ahora es {nuevo_so}")
        self.sistema_operativo=nuevo_so
        

class Notebook(Computadoras):
    def __init__(self, id_modelo,sistema_operativo,lista_perifericos,marca="Asus"):
        super().__init__(id_modelo,sistema_operativo,lista_perifericos=lista_perifericos)
        self.marca=marca

    def agregar_perifericos(self,nuevo_periferico):
        print(f"Los perifericos que tiene la Notebook son {self.lista_perifericos} ")
        self.lista_perifericos.append(nuevo_periferico)

    def cambiar_so(self,nuevo_so):
        print (f"El SO de la computadora Notebook era {self.sistema_operativo} y ahora es {nuevo_so}")
        self.sistema_operativo=nuevo_so