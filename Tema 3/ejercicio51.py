alumnos = [
    ["Juanillo", 4, 1, 5],
    ["Marta", 9, 10, 9],
    ["Ramoncín", 1, 5, 1],
    ["Gerardo", 5, 5, 5],
    ["Einstein", 10, 10, 10]
]
#sin meterlo en la lista
'''
for alumno in alumnos:
    nombre = alumno[0]
    notas = alumno[1:]
    media = sum(notas)/ len(notas)
    print(f"{nombre} tiene un {round(media,2)} de media")

#metiendolo en la lista
'''
medias = []

for fila in alumnos:
    notas = fila[1:]
    medias.append(sum(notas)/ len(notas))

print(medias)