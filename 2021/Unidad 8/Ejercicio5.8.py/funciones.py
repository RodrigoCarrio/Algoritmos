import variables as vr

def imprimir_matriz(matriz):
    print(f"Codigo - Producto - Precio - Stock")
    for i in range(len(matriz)-1):
        print(f"{matriz[0][i]} - {matriz[1][i]} - {matriz[2][i]} - {matriz[3][i]} ")


def agregar_stock_productos():
    print(f"-------------- AÑADIR STOCK -------------")
    while True:
        stock=input("""Ingrese
        1. stock producto 1
        2. stock producto 2
        3. stock producto 3
        :""")
        if stock=="1":
            if(vr.base_productos[3][0]>0):           
                stock_producto_1=int(input("Ingrese cantidad de stock: "))
                print(f"Se añadio {stock_producto_1} al stock")
                vr.base_productos[3][0]=(vr.base_productos[3][0])+(stock_producto_1)
                print(f"Stock actualizado, cantidad: {vr.base_productos[3][0]}")
                return
            else:
                stock_producto_1=int(input("Ingrese cantidad de stock: "))
                print(f"Se añadio {stock_producto_1} al stock")
                vr.base_productos[3][0]=(vr.base_productos[3][0])+(stock_producto_1)
                print(f"Stock actualizado, cantidad: {vr.base_productos[3][0]}")
                return
        elif stock=="2":
            if(vr.base_productos[3][1]>0):
                stock_producto_2=int(input("Ingrese cantidad de stock: "))
                print(f"Se añadio {stock_producto_2} al stock")
                vr.base_productos[3][1]=(vr.base_productos[3][1])+(stock_producto_2)
                print(f"Stock actualizado, cantidad: {vr.base_productos[3][1]}")
                return
            else:
                stock_producto_2=int(input("Ingrese cantidad de stock: "))
                print(f"Se añadio {stock_producto_2} al stock")
                vr.base_productos[3][1]=(vr.base_productos[3][1])+(stock_producto_2)
                print(f"Stock actualizado, cantidad: {vr.base_productos[3][1]}")
                return
        elif stock=="3":
            if(vr.base_productos[3][2]>0):
                stock_producto_3=int(input("Ingrese cantidad de stock: "))
                print(f"Se añadio {stock_producto_3} al stock")
                vr.base_productos[3][2]=(vr.base_productos[3][2])+(stock_producto_3)
                print(f"Stock actualizado, cantidad: {vr.base_productos[3][2]}")
                return
            else:
                stock_producto_3=int(input("Ingrese cantidad de stock: "))
                print(f"Se añadio {stock_producto_3} al stock")
                vr.base_productos[3][2]=(vr.base_productos[3][2])+(stock_producto_3)
                print(f"Stock actualizado, cantidad: {vr.base_productos[3][2]}")
                return
        else:
            print("No ingreso una opcion correcta")
  
def imprimir_matriz2(matriz):
  print(f"--------------PRODUCTOS--------------")
  print(f"C \t PRODUCTO \t Pr$ \tStock")
  for i in range(len(matriz)-1):
    if i !=0:
      print("")
    for j in range(len(matriz)):
      print(f"{matriz[j][i]}",end='\t')
  print("") 

def pago_con_credito():
    print(f"--------------PAGO CON CREDITO-------------")
    while True:
        print(f"Que producto desea vender:")
        for i in range(len(vr.base_productos[1])):
            print(f"{vr.base_productos[0][i]}  {vr.base_productos[1][i]}")
        opcion=input("--> ")        
        if opcion=="1":
            if(vr.base_productos[3][0]>0):
                vr.base_productos[3][0]=vr.base_productos[3][0]-1 #resto stock
                print(f"El comprador debe pagar:$ {vr.base_productos[2][0]*1.1}")
                return
            else:
                print("No hay stock")
        elif opcion=="2":
            if(vr.base_productos[3][1]>0):
                vr.base_productos[3][1]=vr.base_productos[3][1]-1 #resto stock
                print(f"El comprador debe pagar:$ {vr.base_productos[2][1]*1.1}")
                return
            else:
                print("No hay stock")
        elif opcion=="3":
            if(vr.base_productos[3][2]>0):
                vr.base_productos[3][2]=vr.base_productos[3][2]-1 #resto stock
                print(f"El comprador debe pagar:$ {vr.base_productos[2][2]*1.1}")
                return
            else:
                print("No hay stock")
        else:
            print("No ingreso una opcion correcta")

def imprimir_codigo_producto(matriz):
    print(f"------------PRODUCTO------------")
    print(f"C \t PRODUCTO")
    for i in range(len(matriz)-1):
        if i!=0:
            print("")
        for j in range(2):
            print(f"{matriz[j][i]}",end="\t")
    print("")

def pago_con_debito():
    print(f"--------------PAGO CON DEBITO-------------")
    while True:
        print(f"Que producto desea vender:")
        for i in range(len(vr.base_productos[1])):
            print(f"{vr.base_productos[0][i]}  {vr.base_productos[1][i]}")
        opcion=input("-->: ")
        if opcion=="1":
            if(vr.base_productos[3][0]>0):
                vr.base_productos[3][0]=vr.base_productos[3][0]-1
                print(f"El comprador debe pagar:$ {vr.base_productos[2][0]}")
                return
            else:
                print("No hay stock")
        elif opcion=="2":
            if(vr.base_productos[3][1]>0):
                vr.base_productos[3][1]=vr.base_productos[3][1]-1
                print(f"El comprador debe pagar:$ {vr.base_productos[2][1]}")
                return
            else:
                print("No hay stock")
        elif opcion=="3":
            if(vr.base_productos[3][2]>0):
                vr.base_productos[3][2]=vr.base_productos[3][2]-1
                print(f"El comprador debe pagar:$ {vr.base_productos[2][2]}")
                return
            else:
                print("No hay stock")
        else:
            print("No ingreso opcion correcta")

def pago_efectivo():
    print(f"-------------- PAGO CON EFECTIVO -------------")
    while True:
        print(f"Que producto desea vender:")
        for i in range(len(vr.base_productos[1])):
            print(f"{vr.base_productos[0][i]}  {vr.base_productos[1][i]}")
        opcion=input("-->: ")
        if opcion=="1":
            if(vr.base_productos[3][0]>0):
                vr.base_productos[3][0]=vr.base_productos[3][0]-1
                print(f"El comprador debe pagar:$ {round(vr.base_productos[2][0]/1.1111)}")
                return
            else:
                print("No hay stock")
        elif opcion=="2":
            if(vr.base_productos[3][1]>0):
                vr.base_productos[3][1]=vr.base_productos[3][1]-1
                print(f"El comprador debe pagar:$ {round(vr.base_productos[2][1]/1.1111)}")
                return
            else:
                print("No hay stock")
        elif opcion=="3":
            if(vr.base_productos[3][2]>0):
                vr.base_productos[3][2]=vr.base_productos[3][2]-1
                print(f"El comprador debe pagar:$ {round(vr.base_productos[2][2]/1.1111)}")
                return
            else:
                print("No hay stock")
        else:
            print("No ingreso opcion correcta")

def check_stock():
    print(f"-------------- CHECK STOCK -------------")
    while True:
        print(f"Que producto desear chequear:")
        for i in range(len(vr.base_productos[1])):
            print(f"{vr.base_productos[0][i]}  {vr.base_productos[1][i]}")
        opcion=input("--> ")
        if opcion=="1":
            if(vr.base_productos[3][0]>0):
                print(f"Cantidad de stock:{vr.base_productos[3][0]}")
                return
            else:
                print("No hay stock")
        elif opcion=="2":
            if(vr.base_productos[3][1]>0):
                print(f"Cantidad de stock:{vr.base_productos[3][1]}")
                return
            else:
                print("No hay stock")
        elif opcion=="3":
            if(vr.base_productos[3][2]>0):
                print(f"Cantidad de stock:{vr.base_productos[3][2]}")
                return
            else:
                print("No hay stock")
        else:
            print("Opcion incorrecta")

def cambio_precio_productos():
    print(f"-------------- CAMBIO DE PRECIOS -------------")
    while True:
        print(f"Que producto desear cambiar el precio:")
        for i in range(len(vr.base_productos[1])):
            print(f"{vr.base_productos[0][i]}  {vr.base_productos[1][i]}")        
        opcion=input("--> ")
        if opcion=="1":
            try:
                precio_nuevo=int(input("Ingrese el monto nuevo: $ "))
                print(vr.base_productos[2][0])             
                vr.base_productos.pop([2][0])                
                vr.base_productos[2][0]=precio_nuevo                
                print(f"El precio actualizado es de ${vr.base_productos[2][0]}.-")
                break
            except:
                print("Error")
        elif opcion=="2":
            try:
                precio_nuevo=int(input("Ingrese el monto nuevo: $ "))
                print(vr.base_productos[2][1])
                vr.base_productos.pop([2][1])
                vr.base_productos[2][1]=precio_nuevo
                print(f"El precio actualizado es de ${vr.base_productos[2][1]}.-")
                break
            except:
                print("Error")
        elif opcion=="3":
            try:
                precio_nuevo=int(input("Ingrese el monto nuevo: $ "))
                vr.base_productos.pop([2][2])
                vr.base_productos[2][2]=precio_nuevo
                print(f"El precio actualizado es de ${vr.base_productos[2][2]}.-")
                break
            except:
                print("Error")

        else:
            print("No ingreso una opcion correcta")


        