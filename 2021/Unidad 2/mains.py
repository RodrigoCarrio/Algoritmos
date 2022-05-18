#polideportivo
futbol=True
basket=False
voley=True
#condiciones de los amigos
amigo1=futbol
amigo2=basket or voley
amigo3=not voley
amigos=(amigo1) and (amigo2) and (amigo3)
print(f"Los amigos van a ir? {amigos}")
a="2"
b="3"
a_int=int(a)
b_int=int(b)
c=a_int+b_int

print(f"la suma de {a} y {b} es {c}")

print("ingrese un dato")
dato_1=input()
print("ingrese otro dato")
dato_2=input()
print(f"los datos son: {dato_1} y {dato_2}")

Var1=True
Var2=False
Var3=True
condicion_final=Var1 and Var2 and Var3
print(condicion_final)

try:
    dinero_actual=float(input("Ingrese su dinero actual(pesos):"))
    precio_insumo=float(input("Ingrese el precio del insumo que desea comprar(USD):"))
    dinero_actual_usd= dinero_actual/170
    print(dinero_actual_usd>=precio_insumo)
except:
    print("Error de escritura")

try:
    dato1=int(input("Ingrese un dato:"))
    dato2=int(input("Ingrese otro dato:"))
    print(dato1+dato2)
except:
    print("Error")

try:
    nombre=input("Ingrese su nombre:")
    apellido=input("Ingrese su apellido:")
    edad=int(input("Ingrese su edad:"))
    calzado=float(input("ingrese su numero de calzado:"))
    print(nombre)
    print(apellido)
    print(edad)
    print(calzado)
except:
    print("Error")