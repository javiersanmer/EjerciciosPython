numeros = []

while True:
    n = int(input("Introduce números: "))

    if n == 0:
        break
    numeros.append(n)

while len(numeros) > 0:
    print(numeros.pop())