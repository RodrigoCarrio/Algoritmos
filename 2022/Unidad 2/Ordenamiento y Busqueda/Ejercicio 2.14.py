"""
Ejercicio 2.14
Dada una lista de letrar, modificar el algoritmo de seleccion para que ordene por orden alfabetico.
"""
"""
def seleccion(lista):
  for i in range(0,len(lista)-1):
    minimo = i
    for j in range(i+1,len(lista)):
      if(lista[j] < lista[minimo]):
        minimo = j  
    lista[i],lista[minimo] = lista[minimo],lista[i]

#lista = [1,2,3,4,5,6,7,8]
lista = ["b","o","e","x","d","a"]
seleccion(lista)
print(lista)"""

"""
my_list = ['Jack', 'Sam', 'Jay', 'Mark','Baron']

def quicksort(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x <  lst[0]])
            + [lst[0]] +
            quicksort([x for x in lst[1:] if x >= lst[0]]))


print(quicksort(my_list))
"""

def seleccion(lista):
  cont = 0
  for i in range(0,len(lista)-1):
    minimo = i
    for j in range(i+1,len(lista)):
      if(lista[j] < lista[minimo]):
        minimo = j
        print(f"minimo: {lista[minimo]}")
      print(lista)
      cont+=1
    lista[i],lista[minimo] = lista[minimo],lista[i]

  print(f"Cantidad de operaciones: {cont}")

#lista = [1,2,3,4,5,6,7,8]
lista = ["b","o","e","x","d","a"]
seleccion(lista)
print(lista)