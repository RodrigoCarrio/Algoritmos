
import firebase_admin
import json
from firebase_admin import db
import GestorBaseDatos as gb

#conexion con base de datos
cred_obj = firebase_admin.credentials.Certificate('E:\\Analista en sistemas\\KEYS\\feria-virtual-1963d-firebase-adminsdk-uezr8-4cbe6f1ff4.json')
databasesURL="https://feria-virtual-1963d-default-rtdb.firebaseio.com/"
default_app = firebase_admin.initialize_app(cred_obj, {	'databaseURL':databasesURL})

#creacion objeto gestor base de datos
gestorbd=gb.GestorBD()

ref=db.reference("/")
"""
#convierto un diccionario en json
with open("alumnos.json","r") as f:
	file_contents=json.load(f)
"""
#print(f"json en python {type(file_contents)}")
#print(pythonDictionary.get('Book1').get("Title"))

book6={
	"Nombre": "book9",
	"Title": "Brida",
	"Author": "Paulo Coelho",
	"Genre": "Fiction",
	"Price": 100
}

gestorbd.insertar(ref,book6)
"""
#quiero actualizar la info del book 6
ref=db.reference("/")
books=ref.get()

for key, value in books.items():
	if(value.get("Nombre")=="book7"):
		ref.child(key).update({"Genre":"nuevo genero"})
		"""