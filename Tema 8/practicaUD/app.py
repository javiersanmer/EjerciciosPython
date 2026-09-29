from random import choice
from ZODB import DB  
from ZODB.FileStorage import FileStorage
import transaction 
from persistent import Persistent
from persistent.list import PersistentList
import os

os.makedirs("./Practica", exist_ok=True)

class FrasesMotivacionales(Persistent):
    def __init__(self, frase, autor):
        self.frase = frase
        self.autor = autor
    
    def __str__(self):
        return f"{self.frase} - {self.autor}"

storage = FileStorage("./Practica/checklist.fs")
db = DB(storage) 
connection = db.open() 
root = connection.root()

if "frases" not in root:
    root["frases"] = PersistentList()

frases = root["frases"] 

if frases:
    frase_actual = choice(frases)
else:
    frase_actual = None

while True:
    if frases:
        print(frase_actual)
        
    else: 
        print("No hay ninguna frase")
    print()
    
    print("[S]iguiente - [M]odificar - [B]orrar - [N]ueva frase")
    print()
    opcionMenu = input("Opción:").upper().strip()
    print()

    if opcionMenu == "S":
        if frases:
            frase_actual = choice(frases)
    
    elif opcionMenu == "M":
        if frase_actual:
            print("Deja en blanco para mantener el valor actual.")
           
            textoMod = input(f"Nuevo texto [{frase_actual.frase}]: ")
            autorMod = input(f"Nuevo Autor [{frase_actual.autor}]: ")
            print()

            if textoMod:
                frase_actual.frase = textoMod
            if autorMod:
                frase_actual.autor = autorMod

            transaction.commit()
        else:
            print("No hay frases para modificar")

    elif opcionMenu == "B":
        if frase_actual:
            frases.remove(frase_actual)
            transaction.commit() 
          
            print("Frase eliminada")
            print()
            
            if frases:
                frase_actual = choice(frases)
            else:
                frase_actual = None

        else: 
            print("No hay frases para borrar")
            print()

    elif opcionMenu == "N":
        while True:
            frase = input("Frase: ").strip()
            if frase:
                break
            print("No se permiten campos vacíos")

        while True:
            autor = input("Autor: ").strip()
            if autor:
                break
            print("No se permiten campos vacíos")
            
        nueva_frase = FrasesMotivacionales(frase,autor)
        frases.append(nueva_frase) 
        transaction.commit() 
            
        frase_actual = nueva_frase

        print("Frase añadida")
        print()

    elif opcionMenu == "Q":
        break
    
    else:
        print("Opción no válida")

connection.close()
db.close()
storage.close()