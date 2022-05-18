monedas={
    "Peso":"$",
    "Dolar":"USD",
    "Euro":"€"
}
def obtener_simbolos():
    moneda=input("Ingrese el tipo de moneda que desea saber el simbolo: ").capitalize()
    if moneda in monedas:
        print(f"El simbolo de {moneda} es {monedas[moneda]}")
    else:
        print("La moneda no existe en el diccionario")

def obtener_simbolos_2():
    moneda=input("Ingrese el tipo de moneda que desea saber el simbolo: ").capitalize()
    valor=monedas.get(moneda,"No existe")
    print(f"El simbolo de {moneda} es {valor} ")
    


#obtener_simbolos()
obtener_simbolos_2()

