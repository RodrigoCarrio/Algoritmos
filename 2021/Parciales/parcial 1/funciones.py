usuarios=["alumno_1","alumno_2","alumno_3"]
edad=[12,15,17]
email=["alumno_1@gmail.com","alumno_2@gmail.com","alumno_3@gmail.com"]
materias=["matematicas"]
alumnos_gral=[usuarios,edad,email]

def listar_alumnos():
    print(f"USUARIO - EDAD - EMAIL ")
    for i in range(len(alumnos_gral[0])):
        print(f"{alumnos_gral[0][i]} - {alumnos_gral[1][i]} - {alumnos_gral[2][i]}")

def editar_edad():
    print(f"EDITAR EDAD")
    while True:
        nombre=input("Ingrese el nombre del alumno:")
        if nombre in alumnos_gral[0]:
            edad_nueva=int(input("Ingrese nueva edad: "))
            #taxis[1][taxis[0].index(opcion)]=input("Nuevo nombre del chofer: ")
            break 
            
        else:
            print("No ingreso un nombre correcto")

def agregar_alumno():
    while True:
        nombre=input("Ingrese nombre del alumno:")
        if nombre not in usuarios:
            usuarios.append(nombre)
            print(usuarios)
        else:
            print("Nombre ya registrado")
        edad_nueva=int(input("Ingrese edad del nuevo alumno:"))
        if edad_nueva<=18:
            edad.append(edad_nueva)
            print(edad)
        elif edad_nueva>=10:
            edad.append(edad_nueva)
            print(edad)
        else:
            print("Edad no apta")
        email_nuevo=input("Ingrese el mail: ") 
        i="@"
        if i in email_nuevo:
            email.append(email_nuevo)
            print(email)
        else:
            print("No ingreso un mail con @")       
        break

def listar_materias():
    print(f"MATERIAS")
    print(materias)

def agregar_materias():
    while True:
        add_materia=input("Ingrese materia a añadir: ")
        if add_materia in materias:
            print("Materia ya asignada")
        else:
            materias.append(add_materia)
            print(materias)
            break
        

    



