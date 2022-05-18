"""
Ejercicio 2.1
Implementar una función para calcular el producto (sin utilizar el operador por) de dos números enteros dados.(SIN RECURSION)
Implementar una función para calcular el producto (sin utilizar el operador por) de dos números enteros dados.(CON RECURSION)
"""
def producto(a,b):
    try:
        int_a = int(a)
        int_b = int(b)
    except:
        print("Error, numeros no son enteros")
        return
    i=0
    product=0
    for i in range(int_b):
        product+=int_a
        i+=1
    
    return product

print(producto(7,5))

def multiplicacion_recursivo(numero_1,numero_2):
    if(numero_2 == 0):
        return 0
    else:
        return numero_1 + multiplicacion_recursivo(numero_1,numero_2-1)

  
multiplicacion_recursivo(5,6)