nums = []
while True:
    n = int(input("Inserta números: "))

    if n == 0:
        break
    
    nums.append(n)

nums.sort()
print(f"Contenido de la lista {nums}")