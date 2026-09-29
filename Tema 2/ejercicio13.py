numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce un número: "))
operacion = input("Operación: ")

if operacion == "suma":
    solucion = numero1 + numero2
    print(f"El resultado {numero1} + {numero2} es {solucion}")

elif operacion == "resta":
    solucion = numero1 - numero2
    print(f"El resultado {numero1} - {numero2} es {solucion}")

elif operacion == "multiplicación":
    solucion = numero1 * numero2
    print(f"El resultado {numero1} * {numero2} es {solucion}")

elif operacion == "división":
    solucion = numero1 / numero2
    print(f"El resultado {numero1} / {numero2} es {solucion}")
    