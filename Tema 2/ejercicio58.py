import random

def operacionAleatoria() -> str:
    operacion = random.randint(1,3)
    
    if operacion == 1:
        simb = "+"
    elif operacion == 2:
        simb = "-"
    else:
        simb = "*"
    
    return simb

def cuentaAleatoria(inicial : int, final : int): 
    num1 = random.randint(inicial, final)
    num2 = random.randint(inicial, final)
    simb = operacionAleatoria()

    if simb == "+":
        cuenta = num1 + num2
    elif simb == "-":
        cuenta = num1 - num2
    elif simb == "*":
        cuenta = num1 * num2
    
    print(f"Resuelve {num1} {simb} {num2}")
    return cuenta

for i in range(10):
    resultado = cuentaAleatoria(1,10)
    respuesta = int(input("Introuce el resultado: "))

    if respuesta == resultado:
        print("Correcto")
    else:
        print("Incorrecto")
