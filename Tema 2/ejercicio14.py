temperatura = float(input("Introduce la temperatura: "))
escala = input("Introuduce la escala: ")

if escala == "Celsius":
    solucion = (temperatura * 1.8) + 32
    print(f"{temperatura} grados Celsius es {solucion} grados Fahrenheit")
elif escala == "Fahrenheit":
    solucion = (temperatura -32) *1.8
    print(f"{temperatura} grados Fahrenheit es {solucion} grados Celsius")
