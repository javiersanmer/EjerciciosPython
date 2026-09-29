def calculaFactorial(factorial : int) -> int:
    resultado = 1
    for i in range(2,factorial+1):
        resultado = resultado * i
    return resultado

factorial = int(input("Introduce el factorial: "))
resultado = calculaFactorial(factorial)
print(f"El factorial de {factorial} es {resultado}")