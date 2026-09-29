def cuentaPalabras(txt : str) -> list[tuple[str, int]]:
    textoDividido = txt.split()
    palabraYveces = []
    for palabra in textoDividido:
        if palabra not in [p for p,_ in palabraYveces]:
            veces = textoDividido.count(palabra)
            palabraYveces.append((palabra,veces))
    return palabraYveces

def imprimeReporte(palabraYveces):
    for palabra in palabraYveces:
        print(f"Palabra: {palabra[0]} | nº veces: {palabra[1]}")
texto_quijote = 'En un lugar de la Mancha de cuyo nombre no quiero acordarme no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero adarga antigua rocín flaco y galgo corredor'
print(imprimeReporte(cuentaPalabras(texto_quijote)))
