while True:
    try:
        num1 = int(input("Introduce un número: "))
    except Exception as error:
        print("Número no válido")
    else:
        break
while True:
    try:
        num2 = int(input("Introduce otro número: "))
    except Exception as error:
        print("Número no válido")
    else:
        break
resultado = num1 + num2 
print(f"El resultado es {resultado}")