def divisionesNumero(n: int):
    for i in range(1, n+1):
        if n % i == 0:
            print(i)

n = int(input("Introduce un n'umero: "))
divisionesNumero(n)
