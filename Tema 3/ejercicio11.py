liga = ["Real Madrid", "Atlético de Madrid", "FC Barcelona", "Athletic Club",  "Villarreal CF", "RCD Mallorca", "Rayo Vallecano", "Girona FC", "Real Sociedad", "Real Betis", "CA Osasuna", "Sevilla FC", "RC Celta", "Getafe CF", "UD Las Palmas", "CD Leganés", "Deportivo Alavés", "RCD Espanyol", "Valencia CF", "Real Valladolid"]

print("La posción del Real Betis es: ")
for i, equipo in enumerate(liga):
    if equipo == "Real Betis":
        print(f"{i+1}. {equipo}")