contador = 0
suma = 0

nMax = 0
nMin = 0

while True:
    num = int(input("Introduce un numero: "))
    contador = contador + 1

    if num == 0:
        break

    suma = suma + num
    media = suma/contador

    if num > nMax:
        num = nMax 
    
    if num < nMin:
       num = nMin 
    
   

print(f"La media es: {media}, el min es {nMin} y el máximo es {nMax}")