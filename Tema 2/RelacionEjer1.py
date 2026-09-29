sumaTotal = 0
num = 0
numMayor = 0 #None
numMenor = 0 #None
contador = 0

while sumaTotal <= 100: #hasta que, mientras
    num = int(input("Introduce números: "))

    contador += 1

    sumaTotal = num + sumaTotal

    if contador == 1:
        numMayor= num
        numMenor = num
    'Con none'
    ' if minimo is None and maximo is None:'
    '   numMaoyor = num'
    '   numMenor = num'
    'else'
    '   if num > numMayor'
    '       numMayor = num'
    '   else:'
    '       numMenor = num'
    if num > numMayor:
        numMayor = num
    elif num < numMenor:
        numMenor = num

media = sumaTotal / contador


print(f"La cantidad de números introducidos es: {contador}")
print(f"La suma total es {sumaTotal}")
print(f"La media es {media}")
print(f"El número mayor es {numMayor}")
print(f"El número menor es {numMenor}")