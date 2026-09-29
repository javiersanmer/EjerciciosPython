nota = int(input("Introduce una nota del 1 al 10 "))

if nota >= 1 and nota < 5:
    print("Insuficiente")
elif nota == 5:
    print("Suficiente")
elif nota == 6:
    print("Bien")
elif nota ==7 or nota == 8:
    print("Notable")
elif nota == 9 or nota == 10:
    print("Sobresaliente")