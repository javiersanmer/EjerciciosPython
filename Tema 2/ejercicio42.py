texto = input("Introduce un texto: ")

sum = 0

for vocales in texto:
    if vocales == "a" or vocales == "e" or vocales == "i" or vocales == "o" or vocales == "u" or\
        vocales == "A" or vocales == "E" or vocales == "I" or vocales == "O" or vocales == "U":
        sum = sum + 1
    
print(sum)