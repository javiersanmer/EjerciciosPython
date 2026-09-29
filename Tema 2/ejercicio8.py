ciclo = input("Introduce el ciclo en el que estás matriculado: ")
curso = int(input("Introduce el curso en el que estás: "))

if (ciclo == "ASIR" and curso == 1) or (ciclo == "DAW" and curso == 2):
    print("Debes cursar despliegue de páginass web.")
else:
    print("No debes cursar despliegue de páginas web.")
