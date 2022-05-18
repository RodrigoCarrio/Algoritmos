"""Crear una funcion que debe:

*    Pedir al usuario una palabra o una frase
*    Indicar si esta se trata de un palindromo (reconocer, neuquen, amor a roma)
*    No deben aparecer y se deben tener en cuenta todos los posibles errores
"""
def usuario():
    while True:
        try:
            palabra=input("Ingrese una palabra o frase:")
            if palabra.isalpha():
                palabra_lista=list(palabra)
                palabra_reversa=palabra_lista.copy()
                palabra_reversa.reverse()
                if palabra_lista==palabra_reversa:
                    print("Es una palabra capicua")
                    break
                else:
                    print("No es una palabra capicua")
                    break
            else:
                print("No ingreso una palabra o frase")
        except:
            print("Error")

usuario()
