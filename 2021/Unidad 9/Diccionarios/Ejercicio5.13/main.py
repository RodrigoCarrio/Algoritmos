"""
Crear una funcion que debe: (usar diccionario)

Guardar en un diccionario los precios de las frutas de la tabla.
Preguntar al usuario por una fruta, un número de kilos y 
 mostrar por pantalla el precio de ese número de kilos de fruta.
Si la fruta no está en el diccionario debe mostrar un mensaje informando ERROR.
"""
diccionario_frutas={
    "banana":50,
    "manzana":80,
    "pera":100,
    "naranja":30,
}

while True:
    frutas=input("Ingrese la fruta: ")
    if frutas in diccionario_frutas:
        try:
            kilos=int(input("Ingrese numero de kilos: "))
            #print(f"El precio de {frutas} es de {(diccionario_frutas.get(frutas)*kilos)} ")
            print(f"La cantidad de {kilos} kg de {frutas} es de ${(diccionario_frutas.get(frutas)*kilos)} ")
            break
        except:
            print("Error")
            
    else:
        print("Error")