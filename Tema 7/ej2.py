from pathlib import Path

nombre_archivo = Path(__file__).parent / "quijote.txt"

# Versión 1 (sin usar readlines)
contador = 0
with open(nombre_archivo, "r", encoding="utf-8") as f:
    for linea in f:
        if linea[:4] == "Don ":
            contador += 1

print("Número de líneas que empiezan por 'Don':", contador)

# Versión 2 (usando readlines)
with open(nombre_archivo, "r", encoding="utf-8") as f:
    lineas = f.readlines()
    contador = len([linea for linea in lineas if linea.startswith("Don ")])
    print("Número de líneas que empiezan por 'Don':", contador)


# Versión 3 esta es si tiene mera
contador2 = 0

with open(nombre_archivo, "r", encoding="utf-8") as f:
    for linea in f:
        palabras = linea.split()
        for palabra in palabras:
            if "mera" in palabra.lower():
                contador2 += 1

print("Número de palabras que contienen 'me':", contador2)