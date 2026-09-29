pesoCoche = float(input("Introduce el peso de tu coche: "))


if pesoCoche < 1:
    print("Tu coche es ligero")
elif pesoCoche>1 and pesoCoche<2:
    print("Tu coche es medio")
else:
    print("Tu coche es pesado")