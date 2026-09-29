unidades = int(input("Inseta las unidades: "))
precio = 8.75

if unidades >= 1 and unidades <= 10:
    total = precio * unidades 

elif unidades>=11 and unidades<= 50:
    descuento = unidades * precio * 0.05
    total = unidades * precio - descuento
elif unidades>=51 and unidades<= 100:
    descuento = unidades * precio * 0.01
    total = unidades * precio - descuento
else:
    descuento = unidades * precio * 0.15
    total = unidades * precio - descuento
   
print(f"El precio sera {precio}")