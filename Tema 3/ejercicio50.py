matriz = [
    ["Perro", "Gato", "Hámster"],
    ["Loro", "Conejo", "Tortuga"],
    ["Pez", "Hurón", "Ardilla"],
    ["Iguana", "Serpiente", "Erizo"]
]

contador = 0
for fila in matriz:
    for animal in fila:
        if animal[0].lower() in ["a", "e", "i" ,"o", "u"]:
            contador +=1
print(contador)