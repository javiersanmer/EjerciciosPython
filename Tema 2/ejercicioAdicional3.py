nBilletes50 = nBilletes20 = nBilletes10 = nBilletes5 = 0
dinero = int(input("Introduce una cantidad de dinero: "))

if dinero >= 50:
    billete = dinero // 50
    nBilletes50 = billete
    dinero -= 50
elif dinero < 50:
    billete = dinero // 20
    nBilletes20 = billete
    dinero -= 20
elif dinero <= 20:
    billete = dinero // 10
    nBilletes10 = billete
    dinero -= 10
elif dinero <= 10:
    billete = dinero // 5
    nBilletes5 = billete
    dinero -= 5

print(f"{nBilletes50} billetes de 50, {nBilletes20} billetes de 20, {nBilletes10} billetes de 10, {nBilletes5} billetes de 5.")