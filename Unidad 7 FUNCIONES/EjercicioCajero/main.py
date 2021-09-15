"""
##**Ejercicio 4.5 (Cajero automatico)**
El programa debe:
*   Simular un cajero automatico y pedir usuario y contraseña (user, 1234) caso verdadero mostrar menu 
    y en caso falso seguir pidiendo.
*   En caso de mal ingreso de usuario o contraseña 3 veces el programa debe detenerse
*   El menu debe mostrar las funciones posteriores.
*   Contar con 4 funciones:
1.  Consultar el saldo (inicio de 50000)
2.  Ingresar dinero y actualizar saldo
3.  Retirar dinero y actualizar saldo
4.  Salir, y volver al menu de usuario y contraseña
*   Gestionar posibles errores
"""
import funciones_saldo as fs
import funcion_datos as fd
condicion=True
while condicion:
    condicion=fd.validar_usuario()

    while condicion:
        opcion=input(
    """ Por favor ingrese una opcion
        1. Consultar saldo
        2. Ingresar dinero
        3. Retirar dinero
        4. Salir
    Numero: """)
        if (opcion=="1"):
            fs.consultar_saldo()        
        elif (opcion=="2"):
            print(f"El dinero disponible sera: {fs.ingresar_y_actualizar()}")       
        elif (opcion=="3"):
            print(f"El dinero sera: {fs.retirar_y_actualizar()}")
        elif (opcion=="4"):
            condicion=fd.salir()
        else:
            print("No ingreso una opcion correcta")
    condicion=True
