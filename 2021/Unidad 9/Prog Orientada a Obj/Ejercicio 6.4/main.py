"""
###**Ejercicio 6.4**
Crear una clase padre Vehiculos:
*   Constructor debe incluir los atributos (patente,marca,año,origen)
*   Crear metodos para esta clase de:
    1.  Presentarse (patente,marca,año,origen)
    2.  Indicar tipos de vehiculo(Clases heredadas)
    3.  Metodos que luego modificarán las clases hijas. Acelerar, Retroceder, obtener_velocidad, setear_velocidad
 
Crear 3 clases que hereden de la clase padre Vehiculos, con un atributo en particular para cada una
1.   Particular
2.   PickUp
3.   Deportivo 
 
Crear clase GestorAutos que cuente con las siguientes funciones para un menu
1.   Crear auto, indicando tipo de auto y guardar en una lista
2.   Listar autos (presentandolos), indicando tipo de Vehiculo.
3.   Cambiar velocidad de un Vehiculo
4.   Calcular tiempo de viaje de un Vehiculo en una cant de Km pasados por parametro (tiempo = Km / Velocidad)
"""
import Vehiculos as vh
import GestorAutos as ga

gestor=ga.GestorAutos()

while True:
    opcion=input("""
-------MENU PRINCIPAL-------
    1. Crear autos.
    2. Imprimir lista de autos
    3. Cambiar velocidad de un Vehiculo
    4. Calcular tiempo de viaje de un Vehiculo
    5. Salir
    """)
    if opcion=="1":
        gestor.crear_vehiculos()
    elif opcion=="2":
        gestor.imprimir_lista()      
    elif opcion=="3":
        gestor.modificar_velocidad()
    elif opcion=="4":
        gestor.tiempo_viaje()
    elif opcion=="5":
        break
    else:
        print("Opcion incorrecta")
