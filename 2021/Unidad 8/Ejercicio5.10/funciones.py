alfabeto_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alfabeto_b = ['.-' ,'-...' , '-.-.' ,'-..' ,'.', '..-.','--.', '....','..' ,'.---' , '-.-', '.-..','--' ,'-.' ,'---' ,'.--.','--.-' , '.-.' ,'...' ,'-','..-' ,'...-','.--','-..-' , '-.--' , '--..' ]

def listar_alfabeto_a():
    print(alfabeto_a)

def listar_alfabeto_b():
    print(alfabeto_b)

def modificar_alfabeto():
    while True:
        letra=input("Ingrese letra a modificar: ")           
        if (letra in alfabeto_a):   
            nueva_letra=input("Ingrese nueva letra: ")
            i=alfabeto_a.index(letra)
            alfabeto_a[i]=nueva_letra
            alfabeto_b[i]=nueva_letra
            #alfabeto_a[alfabeto_a.index(letra)]=nueva_letra
            #alfabeto_b[alfabeto_a.index(letra)]=nueva_letra                       
            print(alfabeto_a)
            print(alfabeto_b)
            break
        else:
            print("Letra no esta en alfabeto. Ingrese nuevamente una letra.")

def verificacion_de_letra():
    while True:
        opcion=input("""
        Ingrese 
        1. alfabeto_a
        2. alfabeto_b
        :    
        """)
        if opcion=="1":
            check_letra=input("Ingrese letra a verificar: ")
            for letra in alfabeto_a:
                if letra==check_letra:
                    print(f"La letra:{check_letra} esta en el alfabeto_a")
                else:
                    print("Letra no existente")
            break
        elif opcion=="2":
            check_letra=input("Ingrese letra a verificar: ")
            for letra in alfabeto_b:
                if letra==check_letra:
                    print(f"La letra:{check_letra} esta en el alfabeto_b")
                else:
                    print("Letra no existente")
            break
        else:
            print("No ingreso una opcion correcta")

def conver_a_to_b():
    while True:
        letra=input("Ingrese letra a convertir: ")
        if letra in alfabeto_a:
            i=alfabeto_a.index(letra)
            print(f"La letra: {letra} fue convertida a: {alfabeto_b[i]} ")
            break
        else:
            print("Letra no disponible")

def conver_b_to_a():
    while True:
        letra=input("Ingrese letra del alfabeto_b a convertir: ")
        if letra in alfabeto_b:
            i=alfabeto_b.index(letra)
            print(f"La letra: {letra} fue convertida a: {alfabeto_a[i]} ")
            break
        else:
            print("Ingrese correctamente las letras del alfabeto_b")

verificacion_de_letra()













