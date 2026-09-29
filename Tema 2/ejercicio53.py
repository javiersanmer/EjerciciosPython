def vocalesPalabra(palabras: str) -> str:
    letra = 0
    for vocales in palabras:
        if vocales == "a" or vocales == "e" or vocales == "i" or vocales == "o" or vocales == "u" or\
            vocales == "A" or vocales == "E" or vocales == "I" or vocales == "O" or vocales == "U":
            letra = letra + 1
    return letra

palabras = input("Introduce tu texto: ")

letra = vocalesPalabra(palabras)

print(f"La palabra {palabras} tiene {letra} vocales")