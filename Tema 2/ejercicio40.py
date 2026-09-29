texto = input("Introduce un texto: ")
letra = input("Di que letra quieres contar: ")

sum = 0
for letraDentro in texto:
    if letraDentro == letra:
        sum = sum + 1
print(sum)