planetas = [
    ["Mercurio", True, 2439.7],
    ["Venus", True, 6051.8],
    ["Tierra", True, 6371.0],
    ["Marte", True, 3389.5],
    ["Júpiter", False, 69911],
    ["Saturno", False, 58232],
    ["Urano", False, 25362],
    ["Neptuno", False, 24622],
    ["Plutón", True, 1188.3]
]

radioGaseoso = [planeta[2] for planeta in planetas if not planeta[1]]
radioGaseosoMedio = sum(radioGaseoso)/ len(radioGaseoso)
print(radioGaseosoMedio)

radioRocoso = [planeta[2] for planeta in planetas if planeta[1]]
radioRocosoMedio = sum(radioRocoso)/ len(radioRocoso)
print(radioRocosoMedio)

masGrande =  [planeta[2] for planeta in planetas if not planeta[1] > planeta[1]]
masGrande = sum(masGrande)/ len(radioRocoso)

terminaNo = [planeta[0] for planeta in planetas if planeta[0][-2:] == "no"]
print(terminaNo)