edad = int(input("Introduce tu edad: "))

if edad >= 0 and edad <= 2:
    print("Bebé")
elif edad >= 13 and edad <= 17:
    print("Adolescente")
elif edad >= 18 and edad <= 34:
    print("Adulto pero no")
elif edad == 35:
    print("La mejor edad posible")
elif edad >= 36 and edad <= 50:
    print("Adulto")
elif edad >= 51 and edad <= 67:
    print("Pre-anciano")
elif edad >= 68 and edad <= 99:
    print("Anciano")
elif edad > 100:
    print("Centenario")