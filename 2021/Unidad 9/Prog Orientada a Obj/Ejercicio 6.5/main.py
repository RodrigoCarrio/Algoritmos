"""
Ejercicio 6.5
Crear una clase padre Computadoras:
Constructor debe incluir los atributos (id_modelo,listaPerifericos,SO)
Crear metodos para esta clase de:
Presentarse (modelo,marca,precio)
Indicar tipo de Computadora (Clases heredadas)
Metodos que luego modificarán las clases hijas. agregar_perifericos,CambiarSO
Crear 2 clases que hereden de la clase padre Computadoras, con un atributo en particular para cada una
Escritorio
Notebbok
Crear clase GestorComputadora que cuente con las siguientes funciones para un menu
Crear Computadora, indicando tipo y guardar en una lista. Verificando marca y SO de una lista
Listar Computadoras (presentandolos), indicando tipo.
Cambiar SO de una Computadora, verificando una lista de SO disponibles
Listar perifericos
"""
import Computadoras as co
import GestorComputadoras as gc

gestor=gc.GestorComputadoras()

while True:
    opcion=input("""
-------MENU PRINCIPAL-------
    1. Crear Computadora
    2. Listar Computadoras
    3. Cambiar SO de una Computadora
    4. Listar perifericos
    5. Salir
    """)
    if opcion=="1":
        gestor.crear_computadora()
    elif opcion=="2":
        gestor.imprimir_lista()      
    elif opcion=="3":
        gestor.cambio_so()
    elif opcion=="4":
        gestor.listar_perifericos()
    elif opcion=="5":
        break
    else:
        print("Opcion incorrecta")
