i = 1
mayor =""
menor=""
while True:
    palabra = input("Introduce una palabra: ")

    if palabra == "fin":
        break    
    if i == 1:
        contadorCorta = palabra
        contadorLarga = palabra
    else: 
    
        if len(palabra) > len(mayor):
            contadorLarga = palabra
        if len(palabra) < len(menor):
            contadorCorta = palabra
    i = i +1
if contadorLarga != "" and contadorCorta != "":
    print(f"La mas larga es {contadorLarga} y la mas corta {contadorCorta}")
else:
    print(f"No has introducido nada")
print(f"La palabra con menos caracteres es: {contadorCorta} y la mayor es: {contadorLarga}")
