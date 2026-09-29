paises = ["Alemania", "Francia", "Italia", "España", "Países Bajos", "Polonia", "Suecia", "Bélgica", "Austria", "Portugal"]

poblaciones = [83, 68, 59, 47, 17, 38, 10, 11, 9, 10]  # En millones de habitantes

masBajo  = min(poblaciones)
media = sum(poblaciones) / len(poblaciones)

print(media)
print(paises[poblaciones.index(masBajo)])