hora = int(input("Introduce una hora entr 1 y 12: "))
minutos = int(input("Introduce los minutos entre 0 y 59: "))
tipo = input("Di si es AM/PM: ")

if tipo == "AM":
    if hora > 12:
        hora = hora % 12

minutos = str(minutos)
hora = str(hora)

if len(minutos) == 1 and len(hora) == 1:
    print(f"0{hora}:0{minutos}")
elif len(minutos) == 1 and len(hora) == 2:
    print(f"{hora}:0{minutos}")
else:
    print(f"{hora}:{minutos}")




