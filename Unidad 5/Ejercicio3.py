"""print("Ingrese 5 datos numericos")
try:
    numero1=int(input())
    numero2=int(input())
    numero3=int(input())
    numero4=int(input())
    numero5=int(input())
    print((numero1+numero2+numero3+numero4+numero5)/5)
except:
    print("Error")"""
n=int(input("Ingrese cantidad de numeros:"))
numero=[]
for i in range(n):
    numero.append(int(input()))
print(sum(numero)/5)

