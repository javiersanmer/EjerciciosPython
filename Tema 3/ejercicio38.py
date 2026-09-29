planetas_sistema_solar = [
   "Mercurio", "Venus", "Tierra", "Marte",
   "Júpiter", "Saturno", "Urano", "Neptuno"
]

# Lista con las masas de los planetas en kilogramos (valores aproximados)
masas_sistema_solar = [
   3.3011e23,  # Mercurio
   4.8675e24,  # Venus
   5.97237e24, # Tierra
   6.4171e23,  # Marte
   1.8982e27,  # Júpiter
   5.6834e26,  # Saturno
   8.6810e25,  # Urano
   1.02413e26  # Neptuno
]

masaTotal = sum(masas_sistema_solar)
media = masaTotal / len(masas_sistema_solar)

print(media)

for i, planeta in enumerate(planetas_sistema_solar):
    if masas_sistema_solar[i] > media:
        print(planeta)

mayor = max(masas_sistema_solar)
resultado = planetas_sistema_solar[masas_sistema_solar.index(mayor)]
print(resultado)