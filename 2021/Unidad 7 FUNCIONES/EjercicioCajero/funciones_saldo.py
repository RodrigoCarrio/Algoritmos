dinero_disponible=50000.0
lista=[1,2,3]
"""Consultar saldo"""
def consultar_saldo():
    global dinero_disponible
    print(f"El saldo disponible es:{dinero_disponible}")

"""Funcion ingresar dinero y actualizar saldo"""

def ingresar_y_actualizar():
    global dinero_disponible
    while True:
        try:
            dinero_ingresar=float(input("Ingrese el dinero a depositar:"))
            if dinero_ingresar>0:
                 break
            else:
                print("Por favor ingrese una suma positiva")
        except:
            print("Error")

    dinero_disponible+=dinero_ingresar
    return dinero_disponible

"""Funcion retirar dinero y actualizar saldo"""
def retirar_y_actualizar():
    global dinero_disponible
    while True:
        try:
            dinero_retirar=float(input("Ingrese el monto a retirar:"))
            if dinero_retirar>0 and dinero_retirar<=dinero_disponible:
                break
            else:
                print("Por favor ingrese una suma positiva o menor al dinero disponible")
        except:
            print("Error en los parametros")
        if dinero_retirar>0:
            break
        else:
            print("Por favor ingrese una suma positiva")
    dinero_disponible-=dinero_retirar
    return dinero_disponible



