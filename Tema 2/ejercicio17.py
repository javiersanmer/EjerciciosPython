renta = float(input("Introudce tu renta: "))

if renta <= 10000:
    impuesto = 0
elif renta > 10000 and renta <= 20000:
    exceso = renta - 10000
    impuesto = exceso * 0.1
elif renta > 20000 and renta <= 40000:
    exceso = renta - 20000
    impuesto = exceso * 0.1 + 0.2 * exceso 
else:
    exceso = renta - 40000
    impuesto = 1000 + 2000 + exceso * 0.3

print(f"Bueno bueno, hacienda se lleva {impuesto} euros")