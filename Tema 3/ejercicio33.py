palabras = []
while True:
    palabra = input("Inserta números: ")

    if palabra == "fin":
        break
    
    palabras.append(palabra)

palabras.sort()
print(f"Contenido de la lista {palabras}")