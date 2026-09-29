palabras_txt = input("Inserta palabras separadas por coma: ")

palabras = palabras_txt.split(",")

mayor = palabras[0]
menor = palabras[0]

for pal in palabras:
    if len(pal) > len(mayor):
        mayor = pal
    elif len(pal) < len(menor):
        menor = pal

print(mayor)
print(menor)