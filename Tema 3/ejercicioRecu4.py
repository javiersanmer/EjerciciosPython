lista = []

while True:
    numeros = int(input("Introduce números: "))
    if numeros == 0:
        break    
    lista.append(numeros)
    print(lista)

media = sum(lista) / len(lista)

mayoresMedia = [n for n in lista if n>media]
menoresMedia = [n for n in lista if n<media]

lista.sort()
tam = len(lista)



if not len(lista) % 2== 0:
    pass
else:
    mediana = lista[tam // 2]

print(media)
print(f"Los números mayores a la media {mayoresMedia}")
print(f"Los números menores a la media {menoresMedia}")
print(max(lista))
print(min(lista))
