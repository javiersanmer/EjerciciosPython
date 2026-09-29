from pathlib import Path

nombre_archivo = Path(__file__).parent / "quijote.txt"

# Versión 1 (sin usar readlines)
contador = 0

with open(nombre_archivo, "r", encoding="utf-8") as f:
    for linea in f:
        linea = linea.lower()
        contador += linea.count("caballero")

print(f"Número de veces que aparece 'caballero': {contador}")

# Versión 2 (usasando readlines)

with open(nombre_archivo, "r", encoding="utf-8") as f:
    lineas = f.readlines()
    contador = sum([linea.lower().count("caballero") for linea in lineas])
print(f"Número de veces que aparece 'caballero': {contador}")
