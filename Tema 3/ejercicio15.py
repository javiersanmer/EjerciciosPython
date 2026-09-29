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
masaTotal = 0
mayor = masas_sistema_solar[0]

for masa in (masas_sistema_solar):
   masaTotal += masa

media = masaTotal / len(masas_sistema_solar)

for i, planeta in enumerate(planetas_sistema_solar):
   if masas_sistema_solar[i] > media:
      print(planeta)

for i, masa in enumerate(masas_sistema_solar):
   if masa > mayor:
      mayor = masa
      mayorTotal = i

resultado = planetas_sistema_solar[i]

print(f"{i} pesa mas que {masa}") #mal