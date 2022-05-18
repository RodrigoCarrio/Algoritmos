"""
Crear una funcion que debe:

*    Pedir al usuario 5 materias
(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
*    Verficiar que sea un nombre correcto
*    Almacenar los nombres en una lista
*    Mostrar las materias en orden alfabetico
*    No deben aparecer y se deben tener en cuenta todos los posibles errores
"""
def ordenamiento_palabras():
    lista_materias=[]
    for i in range(5):
        while True:
            materias=input(F"Ingrese la materia {i+1} : ")
            if materias.isalpha():
                lista_materias.append(materias)
                lista_materias.sort()
                print(lista_materias)
                break                        
            else:
                print("No ingreso una materia")              

ordenamiento_palabras()

