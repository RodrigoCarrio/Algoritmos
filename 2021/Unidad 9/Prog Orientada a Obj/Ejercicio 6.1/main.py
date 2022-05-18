"""
###**Ejercicio 6.1**
Crear una clase de Persona:
*   Cuyo constructutor debe inicializar los atributos nombre, apellido, edad, ciudad_de_recidencia
*   Se deben crear dos metodos en la clase:
    1.  Presentarse que la persona indique: Soy {nombre} {apellido}, tengo {edad} años y vivo en 
        {ciudad de recidencia}
    2.  Indique segun la edad de la persona si esta es: Niño (0 a 14), Adolecente (14 a 22),
         Joven (22 a 30), mayor(30 a 50), mas mayor(50 a 120)
*
    Menu:
    1. p
    Menu:
    1. para crear personas
    2. Segun el nombre de persona indicar edad"""
import funciones as fu
lista_personas=[]
def crear_personas():
    #dni
    while True:        
        dni=input("Ingrese el DNI: ")
        if dni.isdigit():
            flag_agregar=True
            for personas in lista_personas:
                if dni==personas.dni:
                    print("Ese dni ya existe")
                    flag_agregar=False
                    break
            if(flag_agregar):
                break
        else:
            print("El dni es numerico")
    #nombre
    while True:
        nombre=input("Ingrese el nombre: ").capitalize()
        if not nombre.isalpha():
            print("Un nombre no puede tener simbolos")
        else:
            break
    #apellido
    while True:
        apellido=input("Ingrese el apellido: ").capitalize()
        if not apellido.isalpha():
            print("Un apellido no puede tener simbolos")
        else:
            break
    #edad
    while True:
        try:
            edad=int(input("Ingrese su edad: "))
            if edad<=0:
                print("La edad no puede ser menor o igual a 0")
            else:
                break
        except:
            print("Error en los argumentos")
    #residencia
        residencia=input("Ingrese la residencia: ").capitalize()
        nombre_instancia=dni+nombre
        #instanciando o creando un objeto de persona
        nombre_instancia=fu.Persona(dni,nombre,apellido,edad,residencia)
        lista_personas.append(nombre_instancia)

def listar_personas():
    for persona in lista_personas:
        persona.presentacion()
    
while True:
    opcion=input("""
    1. Crear personas
    2. Verificar rango edad
    3. Listar personas
    4. Salir
    """)
    if opcion=="1":
        crear_personas()
    elif opcion=="2":
        fu.indicar_edad()        
    elif opcion=="3":
        listar_personas()
    elif opcion=="4":
        break
    else:
        print("Opcion incorrecta")
    
    