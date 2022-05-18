"""El programa debe:

Simular una base de datos de peliculas y series con la capacidad de agregar, buscar, eliminar y filtrar peliculas y series.
Debe comenzar con las siguientes peliculas y series en un diccionario:
base = {
    "peliculas" : ["El hombre araña", "Los vengadores" , "Los vengadores 2"],
    "series" : ["prision break", "la casa de papel" , "los simpsons"]
        }
Contar con 5 funciones disponibles en el menu:
Mostrar por pantalla en formato vertical la lista de peliculas o series disponibles.
Agregar nuevas peliculas o series (que no esten) en la base.
Eliminar peliculas o series de la base.
Mostrar segun requiera el usuario la lista de peliculas desde un punto a otro (ej el usuario quiere ver de la 2° a la 4° una lista ).
Buscar peliculas o series que contengan una palabra requerida por el usuario. (ej. input("el"), se liste las peliculas que contengan la palabra "el")."""


base = {
    "peliculas" : ["El hombre araña", "Los vengadores" , "Los vengadores 2"],
    "series" : ["prision break", "la casa de papel" , "los simpsons"]
        }

def mostrar_bases():
    while True:
        base_mostrar = input(
        """
        Ingrese si requiere ver:
        1. la lista de peliculas
        2. la lista de series
        3. Salir
        opcion:
        """)
        if base_mostrar =="1":
            print(f"---------Peliculas---------")
            for i in range(len(base.get("peliculas"))):
                print(base.get("peliculas")[i])
        elif base_mostrar =="2":
            print(f"---------Series---------")
            for i in range(len(base.get("series"))):
                print(base.get("series")[i])
        elif base_mostrar=="3":
            break
        else:
            print("Opcion incorrecta")

def agregar_peliculas_series():
    while True:
        base_mostrar = input(
        """
        Ingrese si requiere agregar:
        1. Peliculas
        2. Series
        3. Salir
        opcion:
        """)
        if base_mostrar =="1":
            nombre_pelicula=input("Ingrese el nombre de la nueva pelicula: ")
            if nombre_pelicula not in base.get("peliculas"):
                base.get("peliculas").append(nombre_pelicula.capitalize())
            else:
                print("Ese nombre ya estaba")
        elif base_mostrar =="2":
            nombre_series=input("Ingrese el nombre de la nueva serie: ")
            if nombre_series not in base.get("series"):
                base.get("series").append(nombre_series.capitalize())
            else:
                print("Ese nombre ya estaba")
        elif base_mostrar=="3":
            break
        else:
            print("Opcion incorrecta")

def eliminar_peliculas_series():
    while True:
        base_mostrar = input(
        """
        Ingrese si requiere eliminar:
        1. Peliculas
        2. Series
        3. Salir
        opcion:
        """)
        if base_mostrar =="1":
            lista_peliculas=base.get("peliculas")
            print(lista_peliculas)
            nombre_pelicula=input("Ingrese el nombre de la pelicula a eliminar: ")
            if nombre_pelicula in lista_peliculas:
                base.get("peliculas").remove(nombre_pelicula)
            else:
                print("Ese nombre no existe")
        elif base_mostrar =="2":
            lista_series=base.get("series")
            print(lista_series)
            nombre_series=input("Ingrese el nombre de la serie a eliminar: ")
            if nombre_series in lista_series:
                base.get("series").remove(nombre_series)
            else:
                print("Ese nombre no existe")
        elif base_mostrar=="3":
            break
        else:
            print("Opcion incorrecta")

def mostrar_de_A_B():
    while True:
        base_mostrar = input(
        """
        Ingrese si requiere mostrar:
        1. la lista de peliculas
        2. la lista de series
        3. Salir
        opcion:
        """)
        if base_mostrar =="1":
            lista_peliculas=base.get("peliculas")
            print(lista_peliculas)            
            start=int(input("Ingrese un numero desde donde comenzar a mostrar peliculas: "))
            end=int(input("Ingrese un numero hasta donde quiere ver peliculas: "))
            for i in range(start,end+1):
                print(lista_peliculas[i],end="-")
            else:
                print("ese nombre no existe")
        elif base_mostrar =="2":
            lista_series=base.get("series")
            print(lista_series)
            start=int(input("Ingrese un numero desde donde comenzar a mostrar peliculas: "))
            end=int(input("Ingrese un numero hasta donde quiere ver peliculas: "))
            for i in lista_series[start-1,end-1]:
                print(i,end="-")
        elif base_mostrar=="3":
            break
        else:
            print("Opcion incorrecta")
    
    for i in lista_peliculas:
        

        print(i)

def buscar_pelicula_serie():
    while True:
        opcion=input("""Ingrese
        1. Peliculas
        2. Series
        3. Salir
        opcion: 
        """)
        if opcion=="1":
            lista_peliculas=base.get("peliculas")
            palabra=input("Ingrese palabra:")
            for pelicula in lista_peliculas:
                if palabra in pelicula:
                    print(f"La palabra {palabra} esta en {pelicula} ")
                    
        elif opcion=="2":
            lista_series=base.get("series")
            palabra=input("Ingrese palabra:")
            for serie in lista_series:
                if palabra in serie:
                    print(f"La palabra {palabra} esta en {serie} ")
        elif opcion=="3":
            break
        else:
            print("Pelicula o serie no encontrada")




while True:
    opcion=input(
    """
    Por favor ingrese una opcion
    1. Mostrar bases
    2. Agregar series o peliculas
    3. Eliminar series o peliculas
    4. Mostrar de A a B
    5. Busqueda por palabra
    6. Salir
    Opcion:
    """)
    if opcion=="1":
        mostrar_bases()
    elif opcion=="2":
        agregar_peliculas_series()
    elif opcion=="3":
        eliminar_peliculas_series()
    elif opcion=="4":
        mostrar_de_A_B()
    elif opcion=="5":
        buscar_pelicula_serie()
    else:
        print("Opcion incorrecta")
