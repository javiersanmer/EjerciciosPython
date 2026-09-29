planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

masas = [3.30e23, 4.87e24, 5.97e24, 6.42e23, 1.90e27, 5.68e26, 8.68e25, 1.02e26]

radios = [2439.7, 6051.8, 6371.0, 3389.5, 69911, 58232, 25362, 24622]

while True:
    planeta = input("Inserta un planeta: ")

    if planetas.count(planeta) > 0:
        n = planetas.index(planeta)
        print(f"La posicion en el sistema solar de {planeta} es {planetas.index(planeta)+1}, masa {masas[n]} y radio {radios[n]}")
    else:
        print("No valido")