while True:
    print("¿Qué operación quieres hacer?: ")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicación")
    print("4.División")
    print("5.División entera")
    print("6.Resto")
    
    opcionMenu = (input("Introduce que quieres realizar: "))
    if opcionMenu == "fin":
        break

    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))

    match opcionMenu:
        case "1":
            print(f"{num1} + {num2} = {num1+num2}")
        case "2":
            print(f"{num1} - {num2} = {num1-num2}")
        case "3":
            print(f"{num1} * {num2} = {num1*num2}")
        case "4":
            print(f"{num1} / {num2} = {num1/num2}")
        case "5":
            print(f"{num1} // {num2} = {num1//num2}")
        case "6":
            print(f"{num1} % {num2} = {num1 % num2}")