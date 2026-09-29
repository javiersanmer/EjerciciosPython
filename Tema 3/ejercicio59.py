diccionarioIngles = {
    'dog' : 'perro',
    'cat' : 'gato'
}

while True:
    palabraIngles = input("Palabra en inglés?")
    traduccion = diccionarioIngles.get(palabraIngles)

    if traduccion != None:
        print(f"Traducción al español: {traduccion}")
    else:
        print("No se encuentra en el diccionario")
        aniadePalabra = input("Añade una palabra: ")
        descripcionPalabra = input("Añade su descripción: ")
        diccionarioIngles[aniadePalabra] = descripcionPalabra
    