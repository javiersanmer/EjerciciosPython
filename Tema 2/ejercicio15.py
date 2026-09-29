figura = (input("Introduce una figura: "))

if figura == "triángulo":
    base = float(input("Introduce la base: "))
    altura = float(input("Introduce la altura: "))
    area = (base * altura)/2

elif figura == "rectágulo":
    base = float(input("Introduce el lado: "))
    altura = float(input("Introduce el lado: "))
    area = base * altura

elif figura == "circunferencia":
    radio = float(input("Introduce el radio: "))
    area = 3.1416 * radio^2

print(area)