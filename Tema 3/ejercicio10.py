equipo = ["Novea", "Enrique", "Jose", "Iker", "Xavi", "Oao",]

for nombre in equipo:
    letras = len(nombre)
    if nombre[0].lower() == nombre[letras-1]:
        print(nombre)