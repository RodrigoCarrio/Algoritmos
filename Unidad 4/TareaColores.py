"""El programa siguiente muestra el color obtenido al mezclar dos colores en la pantalla, siendo los 3 posibles:
Azul
Rojo
Verde
Y los posibles resultados son"""
print("Programa para mezclar 2 colores")
print("rojo\nazul\nverde")
print("A continuacion, ingrese los colores a combinar")
primer_color=input()    
if primer_color=="rojo":
    segundo_color=input()
    if segundo_color=="azul":
        print("Morado.")
    else:  
        print("Amarillo.")  
else:
    segundo_color=input()
    if segundo_color=="verde":
        print("Cyan.")
    else:
        print("Morado.")
    
