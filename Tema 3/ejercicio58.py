texto = input("Introduce un texto: ")
textoPalabra = texto.split()
contador = {}

for palabra in textoPalabra:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

print("Frecuencia palabras: ")
for palabra, veces in contador.items():
    print(f"{palabra} : {veces}")
