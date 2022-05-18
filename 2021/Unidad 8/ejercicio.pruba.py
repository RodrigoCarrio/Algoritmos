while True:
    condicion=input(""" Elija una opcion
    1. Agregar stock
    2. Checkear stock
    3. Eliminar stock
    4. Salir
    :""" )
    if condicion=="1":
        agregar_frutas_verduras()
    elif condicion=="2":
        check_stock()
    elif condicion=="3":
        delete_stock()
    elif condicion=="4":
        break
    else:
        print("No ingreso una opcion correcta")