via = (input("Introduce el tipo de vía: "))
vehiculo = (input("Introduce tu vehiculo: "))

if(via == "Nacional"):
    if (vehiculo == "Coche") or (vehiculo == "Autobus"):
        print("La velocidad permitida es 100km/h")
    elif (vehiculo == "Camión"):
        print("La velocidad permitada es 90km/h")
    else: 
        print("Vehiculo no reconocido")
else:
    if (vehiculo == "Coche"):
        print("La velocidad permitida es 120km/h")
    elif (vehiculo == "Camión"):
        print("La velocidad permitida es 100km/h")
    elif (vehiculo == "Autobus"):
        print("La velocidad permitida es 110km/h")
    else: 
        print("Vehiculo no reconocido")
