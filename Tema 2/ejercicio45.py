while True:
    precio = float(input("Inserta precio base: "))

    if precio < 0:
        break
    iva = float("Inserta el iva: ")
    sobrecoste = precio * iva / 100
    solucion = round(precio + sobrecoste,2)

    print(f"El precio final es: {solucion}")