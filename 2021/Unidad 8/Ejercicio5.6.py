##**Ejercicio 5.6 (Programa de Inventario de verduleria)**
"""
Crear un prgrama que debe:
*    Contar con un stock de frutas y otro de verduras
(El stock indica si venden o no esa fruta o verdura, no la cantidad)
- dos listas que inician vacias
*    Contar con un menu y 3 funciones

      1. Agregar frutas o verduras al correspondiente stock
       (verificando que que sean nuevas)
      2. Consultar el stock de frutas o verduras
      3. Eliminar un elemento del stock"""
verduras=[]
frutas=[] 
def agregar_frutas_verduras():
    while True:
        stock=input("""Ingrese
        1. stock frutas
        2. stock verduras
        :""")
        if stock=="1":
            stock_fruta=input("Ingrese fruta: ")
            if stock_fruta not in frutas:
                frutas.append(stock_fruta)
                print(frutas)
            else:
                print("Fruta ya stockeada")
            break
        elif stock=="2":
            stock_verdura=input("Ingrese verdura:")
            if stock_verdura not in verduras:
                verduras.append(stock_verdura)
                print(verduras)                
            else:
                print("verdura ya stockeada:")
            break
        else:
            print("No ingreso una opcion correcta")

def check_stock():
    while True:
        stock=input("""Ingrese
        1. stock frutas
        2. stock verduras:
        """)
        if stock=="1":
            stock_to_check=input("Ingrese fruta a checkear en stock:")
            for fruta in frutas:
                if fruta==stock_to_check:
                    print(stock_to_check+"es una fruta en stock")
                else:
                    print(stock_to_check+"es una fruta sin stock")
            break
        elif stock=="2":
            stock_to_check=input("Ingrese verdura a checkear en stock:")
            for verdura in verduras:
                if verdura==stock_to_check:
                    print(stock_to_check + "es una verdura en stock")
                else:
                    print(stock_to_check + "es una verdura sin stock")
            break
        else:
            print("No ingreso una opcion correcta")

def delete_stock():
    while True:
        stock=input("""Ingrese
        1. stock frutas
        2. stock verduras:
        """)
        if stock=="1":
            stock_to_del=input("Ingrese fruta a eliminar:")
            for fruta in frutas:
                if fruta==stock_to_del:
                    frutas.remove(stock_to_del)
                    print(frutas)
                else:
                    print(stock_to_del + "no existe en stock")
            break
        elif stock=="2":
            stock_to_del=input("Ingrese una verdura a eliminar:")
            for verdura in verduras:
                if verdura==stock_to_del:
                    verduras.remove(stock_to_del)
                    
                else:
                    print(stock_to_del + "no existe en stock")
            break
        else:
            print("No ingreso una opcion correcta")

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


