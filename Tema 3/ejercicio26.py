nums = []

while True:
    n = int(input("Inserta un número: "))
    
    if nums.count(n) == 0:
        nums.append(n)
    else:
        print("El número ya se encuentra en la lista.")

    print(f"Contenido de la lista {nums}")
    