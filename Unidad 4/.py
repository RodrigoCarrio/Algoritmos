variable_string="1234"
if variable_string.isdigit():
    print("el string son solo numeros")
else:
    print("el string no son numeros")

try:
    usuario=str(input("Ingrese un string:"))
    if usuario.islower():
        print("El string que ingreso esta en minuscula:",usuario)
    else:
        print("Ingreso el string en mayusculas")
except:
    print("Error")

try:
    contraseña="auto123"
    usuario=input("Ingrese la contraseña:")
    if usuario.lower()==contraseña:
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")
except:
    print("Invalid Date")
