palabras = ["hola", "asi", "sioque", "desfasse"]
resultado = [p for p in palabras if p[0] == "a"]

#version para si empieza por a o A
palabras2 = [p for p in palabras if p[0].lower() == "a"]
print(resultado)