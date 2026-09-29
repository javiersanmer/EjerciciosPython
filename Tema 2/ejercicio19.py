anio = int(input("Inserta año: "))

if anio % 100 == 0:
    siglo = anio // 100
else:
    siglo = anio // 100 + 1

print(siglo)


