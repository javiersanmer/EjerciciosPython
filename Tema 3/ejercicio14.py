precipitaciones_granada_2023 = [
   40.2,  # Enero
   35.6,  # Febrero
   45.8,  # Marzo
   50.1,  # Abril
   30.3,  # Mayo
   10.4,  # Junio
   1.2,   # Julio
   5.6,   # Agosto
   20.8,  # Septiembre
   60.5,  # Octubre
   55.3,  # Noviembre
   42.7   # Diciembre
]

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
contador = 0
for i, llueve in enumerate(precipitaciones_granada_2023):
    if i > 0:
        llueveAntes = precipitaciones_granada_2023[i-1]
        if llueve > llueveAntes:
            print(f"En {meses[i]} llovió más {llueve} que en el mes de {meses[i-1]} que llovió {llueveAntes}")