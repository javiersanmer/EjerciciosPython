masLetras = ""
menosLetras = ""

palabrasCont = int(input("¿Cuántas palabras vas a insertar?: "))

for i in range(palabrasCont):
    palabra = (input("Inserta una palabras: "))   

    if i == 0:
        menosLetras = palabra
        masLetras = palabra
    if len(palabra) > len(masLetras):
        contadorLarga = palabra
    if len(palabra) < len(menosLetras):
        contadorCorta = palabra

    

        
print(f"La palabra con menos letras es {contadorCorta} y la que tiene más letras es {contadorLarga}")

    
