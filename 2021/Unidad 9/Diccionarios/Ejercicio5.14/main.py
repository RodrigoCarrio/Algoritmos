"""
Crear una funcion que debe: (usar diccionario)
*    Crear un diccionario vacío y lo vaya llenado con información sobre
     una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
*    Pida al usuario el dato a agregar (key) y el valor
*    Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""

personas={}
def añadir_datos():
    while True:
        nombre=input("Ingrese su nombre: ")
        personas.setdefault("nombre",nombre)
        print(personas)
        try:
            años=int(input("Ingrese su edad: "))
            personas.setdefault("edad",años)
            print(personas)
        except:
            print("Error")
        sexo=input("Ingrese su sexo:")
        personas.setdefault("sexo",sexo)
        print(personas)
        try:
            telefono=int(input("Ingrese su telefono: "))
            personas.setdefault("telefono",telefono)
            print(personas)
        except:
            print("Error")
        correo=input("Ingrese su correo: ")
        personas.setdefault("correo electronico",correo)
        print(personas)
        break

def añadir_datos2():
    while True:
        key=input("""Ingrese la informacion a registrar como por ejemplo
        - Nombre
        - Edad
        - Direccion
        - Sexo
        - Telefono
        - Correo electronico
        O salir (para abandonar el programa)
        : """)
        if key=="salir":
            break
        if key in personas:
            print("Informacion ya registrada previamente, ingrese otros datos ! ")
        else:
            valor=input(f"Ingrese el valor del {key}: ")
            personas.setdefault(key,valor)
            print(personas)
 
def imprimir_diccionario(nombre,diccionario):
    print(f"-------{nombre}-------")
    print(f"--key\tValor--")
    for i in diccionario:
        print(f"{i}\t{diccionario.get(i)}")

def imprimir_diccionario2(nombre,diccionario):
    print(f"-------{nombre}-------")
    print(f"--key\tValor--")
    for i,j in diccionario.items():
        print(f" {i}\t{j}")
añadir_datos()
añadir_datos2()