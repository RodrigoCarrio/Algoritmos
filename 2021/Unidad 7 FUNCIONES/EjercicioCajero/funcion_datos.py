"""
*   Simular un cajero automatico y pedir usuario y contraseña (user, 1234) caso verdadero mostrar menu 
    y en caso falso seguir pidiendo.
*   En caso de mal ingreso de usuario o contraseña 3 veces el programa debe detenerse
"""
def validar_usuario():
    for i in range(3):
        usuario=input("Usuario: ")
        contraseña=input("Contraseña: ")
        if usuario=="user" and contraseña=="1234":
            return True
        else:
            print(f"Datos incorrectos, {2-i} ")
    return False

def salir():
    return False