from ZODB import DB  
from ZODB.FileStorage import FileStorage
import transaction 
from datetime import datetime
from persistent import Persistent
from persistent.list import PersistentList
import os

os.makedirs("./ejercicio1", exist_ok=True)

class Item(Persistent):
    def __init__(self, nombre):
        self.nombre = nombre
        self.fecha_creacion = datetime.now()
        self.fecha_modificacion = self.fecha_creacion
    
    def modificar(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        self.fecha_modificacion = datetime.now()
    
    def __str__(self):
        return f"{self.nombre} (creado el {self.fecha_creacion.strftime('%d/%m/%Y %H:%M:%S')} | modificado el {self.fecha_modificacion.strftime('%d/%m/%Y %H:%M:%S')})"

storage = FileStorage("./ejercicio1/checklist.fs")
db = DB(storage) 
connection = db.open() 
root = connection.root()


if "items" not in root:
    root["items"] = PersistentList()


items = root["items"] 

while True:
    print("\n--- CHECKLIST ---")

    if items:
        for i, item in enumerate(items, start=1):
            print(f"{i}. {item}")
    else:
        print("No hay items aún.")

    print("\n1) Nuevo item")
    print("0) Salir")
    print("-x para borrar, m-x para modificar")

    opcion = input("Elige opción: ")

    if opcion == "1":
        nombre = input("Nombre del item: ")
        nuevo_item = Item(nombre)
        root["items"].append(nuevo_item) 
        transaction.commit() 
        print("Item añadido")
    
    elif opcion[0] == "-":
        indice = int(opcion[1:]) -1
        if indice >= 0 and indice < len(items):
            eliminado = items.pop(indice)
            transaction.commit()
            print("Item borrado")

    elif opcion[:2] == "m-":
        indice = int(opcion[2:]) -1
        if indice >= 0 and indice < len(items):
            nuevo_nombre = input("Nuevo nombre: ")
            items[indice].modificar(nuevo_nombre)
            transaction.commit()
            print("Item modificado")

    elif opcion == "0":
        print("Saliendo...")
        break

    else:
        print("Opción no válida")


connection.close()
db.close()
storage.close()