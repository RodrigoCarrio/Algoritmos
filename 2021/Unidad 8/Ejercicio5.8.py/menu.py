'''
##**Ejercicio 5.8 (Programa de ventas)**
El programa debe:
*   Simular un programa que venda 3 productos
Codigo      Nombre      PRecio stock
    1     & producto1  & 300   & 5
    2     & producto2  & 400   & 4
    3     & producto3  & 500   & 7

*   El menu debe mostrar los productos a comprar. ->LISTO
*   Luego se debe contar con un menu de si se pagara en efectivo o tarjeta credito o debito -> LISTO
*   Contar con 7 funciones disponibles en el menu:
  1. Ver menu de productos (Formato: codigo - producto) -> LISTO
  2.  Pagar con tarjeta credito (Se debe cobrar 10% mas y se debe descontar el stock) -> LISTO
  3.  Pagar con tarjeta debito (se debe descontar el stock) --> LISTO
  4.  Pagar con efectivo (Se debe cobrar 10% menos y se debe descontar el stock) --> LISTO
  5.  Consultar productos y stock --> LISTO
  6.  Agregar stock a los productos --> LISTO
  7.  Cambiar el precio a los productos
  
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''
import funciones as fun
import variables as vr

base_productos=[[1,2,3],["producto1","producto2","producto3"],[300,400,500],[5,4,7]]

def forma_de_pago():
    while True:
        condicion=input("""
        Ingrese
        1. Efectivo
        2. Tarjeta credito
        3. Tarjeta debito
        Opcion: """)
        if condicion=="1":
            return "Efectivo"
        elif condicion=="2":
            return "Tarjeta credito"
        elif condicion=="3":
            return "Tarjeta debito"
        else:
            print("No ingreso una opcion correcta")

fun.imprimir_matriz(vr.base_productos)
#fun.imprimir_codigo_producto(base_productos)
#forma_de_pago()
#fun.pago_con_credito()
#fun.pago_efectivo()
#fun.check_stock()
#fun.imprimir_matriz2(vr.base_productos)
#fun.agregar_stock_productos()
fun.cambio_precio_productos()


