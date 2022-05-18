"""
Requerimientos:
El programa debe:
*   Contar con una Clase Evento con los atributos (nombre_evento (único), fecha, hora, lugar)
*   Contar con dos Clases Hijas que use el constructor de la clase padre pero que tenga un atributo más:
        - EventoPersonal (Atributo: organizador (nombre de la persona que organiza))
        - EventoLaboral (Atributo: obligatorio "True o False" (por defecto = True))
        
*   Se deben crear 4 métodos para la clase padre Evento (que heredaran las clases hijas):
        1. Mostrar información: Que indique el nombre_evento, fecha y lugar del evento 
        2. Obtener tipo de evento (tipo de clases heredadas o padre)
        3. Setear Fecha y Hora (Setearán la Fecha y Hora en una misma función)
        4. Setear lugar (Setear el lugar)
"""

class Evento:
    def __init__(self,nombre_evento,fecha,hora,lugar):
        self.nombre_evento=nombre_evento
        self.fecha=fecha
        self.hora=hora
        self.lugar=lugar

    def presentarse(self):
        print(f"""Nombre evento:{self.nombre_evento},fecha: {self.fecha},lugar evento {self.lugar} """)

    def tipo_evento(self):
        print(f"Soy un evento del tipo",type(self).__name__)

    def set_fecha_hora(self,fecha_nueva,hora_nueva):
        print(f"Cambio de fecha {self.fecha} a {fecha_nueva} y se cambio la hora {self.hora} a {hora_nueva} ")
        self.fecha_nueva=fecha_nueva
        self.hora_nueva=hora_nueva

    def set_lugar(self,lugar_nuevo):
        print(f"Cambio de lugar {self.lugar} a {lugar_nuevo}")
        self.lugar=lugar_nuevo

    def get_lugar(self):
        return self.nombre_evento

class EventoPersonal(Evento):
    def __init__(self, nombre_evento, fecha, hora, lugar, organizador):
        super().__init__(nombre_evento, fecha, hora, lugar)
        self.organizador=organizador

class EventoLaboral(Evento):
    def __init__(self, nombre_evento, fecha, hora, lugar, obligatorio):
        super().__init__(nombre_evento, fecha, hora, lugar)
        self.obligatorio=obligatorio