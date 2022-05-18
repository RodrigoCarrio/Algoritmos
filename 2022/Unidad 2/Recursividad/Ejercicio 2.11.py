"""
Ejercicio

Realizar una funcion simple (sin recursion) para obtener los numeros n de la susecion de Fibonnacci
Realizar una funcion recursiva para obtener los numeros n de la susecion de Fibonnacci
"""
# 0,1,1,2,3,5,8,13,21,34,55,89,144,
# fibonacci[n]=fibonacci[n-1] + fibonacci[n-2]
"""
def fibonacci(n):
    n0=0
    print(n0,end=", ")
    n1=1
    print(n0,end=", ")
    suma= n0+n1

    while suma <= n:
        suma= n0+n1
        print(suma,end=", ")
        n0=n1
        n1=suma

fibonacci(90)"""


def fibonacci_recursivo(n):
    if n<=1:
        return n
    else:
        return (fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2))
         
n=7
for i in range(n):  
    print(fibonacci_recursivo(i))