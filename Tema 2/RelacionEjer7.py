contador = 0
letra = input("Introduce una letra: ")
while True:
    palabra = input("Inserta una palabra: ")

    if palabra == "fin":
        break
       
    for letra in palabra:
        if palabra == letra:
            contador += 1
print(contador)