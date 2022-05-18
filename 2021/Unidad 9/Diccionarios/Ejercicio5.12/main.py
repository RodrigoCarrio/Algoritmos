datos_personas={}
def añadir_datos():
    nombre=input("Ingrese su nombre: ").capitalize()
    datos_personas.update({"Nombre":nombre})
    while True:
        try:
            años=int(input("Ingrese su edad: "))
            datos_personas.setdefault("Edad",años)
            break
        except:
            print("Error")
    direccion=input("Ingrese su direccion: ").capitalize()
    datos_personas.setdefault("Direccion",direccion)
    while True:
        try:
            telefono=int(input("Ingrese su telefono: "))
            datos_personas.setdefault("Telefono",telefono)
            break
        except:
            print("Error")
    print(datos_personas) 
    print(f" {nombre} tiene {años}, vive en {direccion} y su telefono es {telefono} ")   
    
    
    


añadir_datos()