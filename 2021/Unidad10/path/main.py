import os
#path actual
#path = os.path.abspath(os.path.dirname(__file__))#probar este 1°
#path = os.path.abspath(os.path.dirname('auto'))#probar este 2°
path = os.path.dirname(os.path.abspath("auto"))#probar este 3°
path_archivo = path+"\\auto.txt"
print(path+"\\auto.txt")##\\ por caracteres especiales