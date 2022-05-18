"""
##**Ejercicio 5.10 (Conversión de alfabeto)**
El programa debe:
*   Simular la conversion de un alfabeto a otro: Por ejemplo el moorse 
    (NO ES ESTRICTAMENTE NECESARIO USAR ESTE ALFABETO, PUEDE SER INVENTADO)
*   Contar con 6 funciones disponibles en el menu:
    1. Mostrar el alfabeto A
    2. Mostrar el alfabeto B
    3. Modificar una letra del Alfabeto A y el alfabeto B (debe ser la misma)
    4. Conversion de alfabeto A a alfabeto B: ejemplo **abc --> .--...-.-.**
    5. Conversion de alfabeto B a alfabeto A: ejemplo **.--...-.-. --> abc**
    6. Verificacion de existencia de una letra del alfabeto (debe seleccionar A o B)

*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
    """
alfabeto_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alfabeto_b = ['.-' ,'-...' , '-.-.' ,'-..' ,'.', '..-.','--.', '....','..' ,'.---' , '-.-', '.-..','--' ,'-.' ,'---' ,'.--.','--.-' , '.-.' ,'...' ,'-','..-' ,'...-','.--','-..-' , '-.--' , '--..' ]
import funciones as fun
print(f"-----------PROGRAMA DE CONVERSION-----------")
while True:
    opcion=input("""
    MENU
    1.Mostrar el alfabeto A
    2.Mostrar el alfabeto B
    3.Modificar una letra del Alfabeto A y el alfabeto B
    4.Conversion de alfabeto A a alfabeto B
    5.Conversion de alfabeto B a alfabeto A
    6.Verificacion de existencia de una letra del alfabeto
    7.Salir

    Ingreso: """)
    if opcion=="1":
        fun.listar_alfabeto_a()
    elif opcion=="2":
        fun.listar_alfabeto_b()
    elif opcion=="3":
        fun.modificar_alfabeto()
    elif opcion=="4":
        fun.conver_a_to_b()
    elif opcion=="5":
        fun.conver_b_to_a()
    elif opcion=="6":
        fun.verificacion_de_letra()
    elif opcion=="7":
        break
    else:
        print("No ingreso una opcion correcta")
