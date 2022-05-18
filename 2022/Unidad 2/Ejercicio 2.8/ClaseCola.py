from re import X


class Cola:
    """ Representa a una cola, con operaciones de encolar y desencolar.
        El primero en ser encolado es también el primero en ser desencolado.
    """

    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa por una lista vacía
        self.items=[]

    def encolar(self, x):
        """ Agrega el elemento x como último de la cola. """
        self.items.append(x)

    def desencolar(self):
        """Elimina el primer elemento de la cola y devuelve su
            valor. Si la cola está vacía, levanta ValueError."""
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía")
    
    def es_vacia(self):
        """ Devuelve True si la cola esta vacía, False si no."""
        return self.items == []
    
    def ver_cola(self):         
        for i in range(len(self.items)-1, -1, -1):
            if i == len(self.items)-1:
                print("Final", end =" ")
            print(self.items[i], end =" ")
            if i == 0:
                print("Frente", end =" ")
        
        print("")
        
    def get_tamaño(self):
        return len(self.items)
    
    def get_cima_cabecera(self):
        return self.items[0]
    
    def get_cima_final(self):
        return self.items[-1]
    
    def mover_al_final(self):
        try:
            elemento=self.desencolar() 
            self.encolar(elemento)
            self.ver_cola()
        except:
            print("Error")

    #Crear metodo de cola que permita agregar un elemento con cierta prioridad.

    #P = 0, se agrega al frente de la cola
    #P = 1, se agrega segundo en la cola
    #P = 2, se agrega a la mitad de la cola
    
    def agregar_con_prioridad(self,x,prioridad):
        if prioridad==0:
            self.items.insert(0,x)
        elif prioridad==1:
            self.items.insert(1,x)
        elif prioridad==2:
            self.items.insert(int(len(self.items)/2)-1,x)
        else:
            print("Prioridad incorrecta")
