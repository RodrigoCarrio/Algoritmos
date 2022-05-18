"""
Ejercicio 3.2
Crear una clase abstracta (formal) Animal con 4 metodos. (Hablar, Mover, Dormir, Comer) y dos clases Gato y Perro que hereden la clase Animal.

Luego crear un menu para crear animales y guardarlos en una lista.
"""
from abc import ABC
from abc import abstractmethod

class Animal(ABC):
    @abstractmethod
    def hablar(self):
        pass

    @abstractmethod    
    def mover(self):
        pass

    @abstractmethod
    def dormir(self):
        pass

    @abstractmethod
    def comer(self):
        pass

class Gato(Animal):
    def hablar(self):
        print("Miauuuu")

    def mover(self):
        print("Estoy trepando un arbol")

    def dormir(self):
        print("ZZzzzzz (gato)")

    def comer(self):
        print("Rico pescado")

    def crear_animal():
        #nombre
        nombre=input("Ingrese el nombre del animal: ")
        lista_animales.append(nombre)

class Perro(Animal):
    def hablar(self):
        print("Guauuuu")

    def mover(self):
        print("Estoy corriendoooo")

    def dormir(self):
        print("ZZzzzzz (perro)")

    def comer(self):
        print("Rico huesoooo")

    def crear_animal():
        #nombre
        nombre=input("Ingrese el nombre del animal: ")
        lista_animales.append(nombre)

lista_animales=[]

def imprimir_lista():
    for i in lista_animales:
        print(i)

while True:
    opcion=input("""
-------MENU PRINCIPAL-------
    1. Crear Perro
    2. Crear Gato
    3. Imprimir lista
    4. Salir
    """)
    if opcion=="1":
        Perro.crear_animal()
    elif opcion=="2":
        Gato.crear_animal()  
    elif opcion=="3":
        imprimir_lista()
    elif opcion=="4":
        break

    else:
        print("Opcion incorrecta")