while True:
    real = float(input("Introduce un número real: "))
    if real == 0:
        break
    entero = int(input("Introduce un número entero: "))
    rendondeo = round(real, entero)
    print(f"El número {real} redondeado a {entero} es {rendondeo}")
    