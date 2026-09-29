liga = ["Real Madrid", "Atlético de Madrid", "FC Barcelona", "Athletic Club",  "Villarreal CF", "RCD Mallorca", "Rayo Vallecano", "Girona FC", "Real Sociedad", "Real Betis", "CA Osasuna", "Sevilla FC", "RC Celta", "Getafe CF", "UD Las Palmas", "CD Leganés", "Deportivo Alavés", "RCD Espanyol", "Valencia CF", "Real Valladolid"]

equipo = input("Introduce un equipo: ")


if liga.count(equipo) > 0:
    print(f"La posción del {equipo} es: { liga.index(equipo)+1}")
else:
    print("No se ha encontrado el equipo")


