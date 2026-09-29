try:
    num1 = int(input("Introduce un número: "))
    num2 = int(input("Introduce otro número: "))
except Exception as error:
    print(f"Se ha producido un error del tipo: {error}")
else:
    resultado = num1 + num2
    print(f"El resultado es {resultado}")
