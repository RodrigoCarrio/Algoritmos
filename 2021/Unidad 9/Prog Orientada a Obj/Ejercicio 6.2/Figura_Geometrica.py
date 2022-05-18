"""Se deben crear 3 metodos en la clase:
    1.  Presentar la figura: Un {tipo_de_figura} de color {color} y tamaño {tamaño}
    2.  Cambiar color de figura e indicar nuevo color
    3.  verificar si la figura es tamaño pequeño, agrandar a tamaño grande
    """
class FiguraGeometrica:
    def __init__(self,tipo_de_figura,color,tamaño="pequeño"):
        self.tipo_de_figura=tipo_de_figura
        self.color=color
        self.tamaño=tamaño
        
    def presentacion(self):
        print(f"""Un {self.tipo_de_figura} de color {self.color} y tamaño {self.tamaño}""")

    def cambiar_color(self,color_nuevo):
        print(f"Cambio de color {self.color} a {color_nuevo}")
        self.color=color_nuevo
    
    def verificar(self):
        if self.tamaño=="pequeño":
            self.tamaño="grande"
        print(f"El tamaño de la figura es {self.tamaño}")
      
       
figura_1=FiguraGeometrica("triangulo","blanco")
figura_1.presentacion()
figura_1.verificar()

nuevo_color = input("Indique el nuevo color: ")
if (figura_1.color == nuevo_color):
    print("ya tiene ese color, no es necesario cambiarlo")
else:
    figura_1.cambiar_color(nuevo_color)
    
    