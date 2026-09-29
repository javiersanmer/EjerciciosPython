km = int(input("Introduce los km: "))
hora = float(input("Introduce la hora: "))
dia = input("Introduce el dia: ")

base = 3.5

if (dia == "Domingo"):
    precio = base + km * 1.5

elif (dia == "Sábado"):
    if(hora >= 8 and hora <= 18):
        precio = base + km * 1.2
    else:
        precio = base + km *1.5
else:  
    if(hora >= 8 and hora <= 18):
        precio = km + base
    elif(hora>= 19 and hora<=23):
        precio = base + km * 1.2
    else:
        precio = base + km * 1.5

print(f"El precio sera {precio}")

'''Examen'''
'''la tikitiki'''