
class Pila:
    def __init__(self) :
        print("Cree una pila vaia")
        self.items=[]
        
    def apilar(self,x):
        self.items.append(x)
        print(f"agregar el elemento {x} a la pila ")

    def desapilar(self):
        print(" Devuelve el elemento tope y lo elimina de la pila.Si la pila está vacía levanta una excepción. ")
        try:
            return self.items.pop()
        except:
            print("La pila está vacía")

    def pila_vacia(self):
        if(len(self.items)==0):
            return True
        else:
            return False
    
    def get_tamaño(self):
        return len(self.items)
    
    def get_cima(self):
        return self.items[-1]
    
    def ver_pila(self): #ver la lista de atras para adelante
        #for i in range(len(x)-1, -1, -1):
        for i in reversed(self.items):
            print(i)
    
    def ver_pila_2(self):
        print(self.items)