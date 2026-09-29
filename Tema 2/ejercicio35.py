altura = int(input("Inserta la altura: "))
base = int(input("Inserta la base: "))
caracter = (input("Inserta el caracter: "))

contadorA = 1
contadorB = 0

cantidad = caracter
while contadorA < base:
    cantidad = cantidad + caracter
    contadorA = contadorA + 1

while contadorB < altura:
        print(cantidad)
        contadorB = contadorB + 1