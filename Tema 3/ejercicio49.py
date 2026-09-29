matriz = [
    ["Perro", "Gato", "Hámster"],
    ["Loro", "Conejo", "Tortuga"],
    ["Pez", "Hurón", "Ardilla"],
    ["Iguana", "Serpiente", "Erizo"]
]
masLetras = matriz[0][0]
for fila in matriz:
    for e in fila:
        if len(masLetras) < len(e):
            masLetras = e
    
print(masLetras)