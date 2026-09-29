animales_mitologicos = [
   "Yeti",
   "Monstruo del lago Ness",
   "Mokele-mbembe",
   "Chupacabras",
   "Aberroncho",
   "Hombre polilla",
   "Demonio de Dover",
   "Mapinguarí",
   "Nahuelito",
   "Kraken",
   "Wendigo",
   "Ahool",
   "Jersey Devil",
   "Skinwalker",
   "Ogopogo",
   "Borja profe de programación"
]
print("Listado de animales mitológicos con nombre compuesto: ")
for nombre in animales_mitologicos:
    if len(nombre.split())>1:
        print(f"\t {nombre}")
