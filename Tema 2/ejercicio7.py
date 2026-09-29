ciclo = input("Introduce el ciclo en el que estás matriculado: ")
curso = int(input("Introduce el curso en el que estás: "))

if (ciclo == "DAW" or ciclo == "DAM") and curso == 1:
    print("Debes cursar programación")
else:
    print("No debes cursar progrmación")