from firebase_admin import db

class GestorBD:
    def insertar(self,ref,data):
        #insertar datos en la base de datos
        try:
            ref.push().set(data)
        except Exception as e:
            print(e)

    def obtener(self):
        pass
    
    def actualizar(self,ref):
       #quiero actulizar la info del book7
        ref = db.reference("/")
        books = ref.get()

        for key, value in books.items():
            if(value.get("Nombre") == 'book1'):
                ref.child(key).update({"Genre":'nuevo genero'})