with open("f.txt", "w", encoding="utf-8") as f:
    f.write("a\nb\nc\n")
    print(f.read())

with open("f.txt", "r", encoding="utf-8") as f:
    contador = 0
    for linea in f:
        if linea == "a":
            contador += 1

    