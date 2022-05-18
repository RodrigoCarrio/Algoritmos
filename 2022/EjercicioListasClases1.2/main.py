"""
El programa debe:

Contar con:

Contar con una Clase Persona con los atributos (dni (int - único), nombre (string), apellido (string))
Contar con una Clase Hija Empleado que use el constructor de la clase padre con los atributos:
funcion (string)
año_ingreso (string 'yyyy')
Se deben crear los siguientes métodos para la clase padre Persona (que heredará la clase hija):
Set y Get dni.
Se deben crear los siguientes métodos para la clase hija.

*  Set y Get funcion.
Se debe contar y crear funciones para un menu que tenga las siguiente opciones,

Crear un empleado y guardarlo en una lista_empleados
Recorrer la lista de empleados segun DNI, mayor a menor o menor a mayor
Recorrer la lista de empleados segun fecha_ingreso, mayor a menor o menor a mayor
Eliminar el ultimo empleado agregado
IMPORTANTE:

Se deben crear metodos y clases a criterio
Gestionar posibles errores
Estructurar el programa a criterio propio
"""
import Persona as pe
import Gestor as ge
gestor=ge.GestorPersonas()

while True:
    opcion=input("""
-------MENU PRINCIPAL-------
    1. Crear empleado
    2. Recorrer la lista de empleados segun DNI, mayor a menor o menor a mayor
    3. Recorrer la lista de empleados segun fecha_ingreso, mayor a menor o menor a mayor
    4. Eliminar el ultimo empleado agregado
    5. Salir
    """)
    if opcion=="1":
        gestor.crear_empleados()
    elif opcion=="2":
        pass       
    elif opcion=="3":
        gestor.ordenar_por_fecha_me_a_mayor()
    elif opcion=="4":
        gestor.eliminar_ultimo_empleado()  
    elif opcion=="5":
        break
    else:
        print("Opcion incorrecta")


