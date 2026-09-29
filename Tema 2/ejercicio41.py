texto = input("Introduce un texto: ")

sum = 1
for palabra in texto:
    if palabra == " ":
        sum = sum + 1
print(sum)
