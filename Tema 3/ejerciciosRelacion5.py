planetas = [
    ["Mercurio", True, 2439.7],
    ["Venus", True, 6051.8],
    ["Tierra", True, 6371.0],
    ["Marte", True, 3389.5],
    ["Júpiter", False, 69911],
    ["Saturno", False, 58232],
    ["Urano", False, 25362],
    ["Neptuno", False, 24622],
    ["Plutón", True, 1188.3]  # Incluyendo a Plutón
]

gaseosos_radio = [planeta[2] for planeta in planetas if not planeta[1]]
gaseosos_radio_medio = sum(gaseosos_radio) / len(gaseosos_radio) 
print(f"El radio medio de los planetas gaseosos es: {gaseosos_radio_medio:.2f}")

menorGaseso = min(gaseosos_radio)
rocosoMasGrande = [planeta[0] for planeta in planetas if planeta[1] and planeta[2] > menorGaseso]
print(rocosoMasGrande)

nombrePlaneta = [planeta[0] for planeta in planetas if planeta[0][-2:] == "no"]
print(nombrePlaneta)