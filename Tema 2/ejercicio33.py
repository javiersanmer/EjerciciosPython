factorial = int(input("Introduce un numero: "))
contador = 2
resultado = 1
while contador <= factorial:
    resultado = resultado * contador
    contador = contador + 1

print(f"El factorial de {factorial} es {resultado}")