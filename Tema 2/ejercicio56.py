def fraseDevuelve(texto : str) -> int:
    sum = 1
    for palabra in texto:
        if palabra == " ":
            sum = sum + 1
    return sum

texto = input("Introduce tu texto: ")
resultado = fraseDevuelve(texto)

print(sum)