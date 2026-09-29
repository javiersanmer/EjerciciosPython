def cantidadRecibida(n:int,medida1: str, medida2: str) -> float:
    if medida1 == "gramos":
        if medida2 == "tonelada":
            n = n *1000000
        elif medida2 == "kilos":
            n = n * 1000
    elif medida1 == "tonelada":
        if medida2 == "gramos":
            n = n /10000000
        elif medida2 == "kilos":
            n = n /1000
    elif medida1 == "kilos":
        if medida1 == "tonelada":
            n = n * 1000
        elif medida2 == "gramos":
            n = n / 1000
    else: 
        print("No valido")
    return n

n = int(input("Introduce un número:" ))
medida1 = (input("Introduce una medida:" ))
medida2 = (input("Introduce una medida:" ))

resultado = cantidadRecibida(n, medida1, medida2)
print(resultado)
