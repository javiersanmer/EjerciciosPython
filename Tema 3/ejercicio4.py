numeros = [1,4,5,11,2,0,6,12,3,10]
sumaTotal = 0
for n in numeros:
    sumaTotal += n

media = sumaTotal / len(numeros)
print(f"{media:-2f}")#Redondeo sin round