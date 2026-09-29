i = 0
while True:
    palabra = input("Introduce una palabra: ")
    
    if palabra == "fin":
        break

    if len(palabra) <= 5:
        i = i + 1

print(i)
#EXAMEN CAE