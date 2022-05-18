class Lapiz:
    #todos los lapices seran de la misma marca
    marca = "Faber-Castell"

    def __init__(self, color, longitud):
        print(f"Creando un lapiz de color {color}, que mide {longitud} cm")
        # Atributos de instancia
        self.color = color
        self.longitud = longitud

lapiz_1 = Lapiz("rojo",25)
lapiz_2 = Lapiz("rojo",25)
lapiz_1.marca = "bic"
lapiz_2.marca = "bic"
print(lapiz_1.marca)
print(lapiz_2.marca)