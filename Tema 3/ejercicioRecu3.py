pokemones = [
   ["Pikachu", ["Eléctrico"]],
   ["Charmander", ["Fuego"]],
   ["Bulbasaur", ["Planta", "Veneno"]],
   ["Squirtle", ["Agua"]],
   ["Gengar", ["Fantasma", "Veneno"]],
   ["Onix", ["Roca", "Tierra"]],
   ["Machamp", ["Lucha"]],
   ["Zapdos", ["Eléctrico", "Volador"]],
   ["Dragonite", ["Dragón", "Volador"]],
   ["Eevee", ["Normal"]]
]

#Con list Comprenhension
electrico = [p[0] for p in pokemones if "Eléctrico" in p[1]]
print(electrico)

electricoYotro = [p[0] for p in pokemones if "Eléctrico" in p[1] and len(p[1]) > 1]
print(electricoYotro)


for pokemon in pokemones:
    if "Eléctrico" in pokemon[1]:
        print(pokemon[0])

for pokemon in pokemones:
    tipos = pokemon[1]
    if "Eléctrico" in tipos and len(tipos) > 1:
        print(pokemon[0])