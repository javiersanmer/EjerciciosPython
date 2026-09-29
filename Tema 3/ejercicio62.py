mobs_hostiles = ["Zombie", "Skeleton", "Creeper", "Creeper", "Enderman", "Ghast", "Piglin"]
mobs_pacíficos = ["Cow", "Sheep", "Pig", "Villager", "Villager", "Enderman"]
mobs_del_Nether = ["Ghast", "Piglin", "Hoglin", "Blaze", "Piglin", "Enderman"]

set_hostiles = set(mobs_hostiles)
set_pacificos = set(mobs_pacíficos)
set_Nether = set(mobs_del_Nether)

print("a) Eliminar mobs repetidos de cada lista:",)
mobsHostilesSinRepetidos = list(set(mobs_hostiles))
mobsPacificosSinRepetidos = list(set(mobs_pacíficos))
mobsNetherSinRepetidos = list(set(mobs_pacíficos))
print(f"Mobs sin repetidos de {mobsHostilesSinRepetidos}, pacíficos {mobsPacificosSinRepetidos} y Nether{mobsNetherSinRepetidos}")

print("b) Mobs que aparecen en el Overworld y son hostiles:", list(set_hostiles - set_pacificos))
print("c) Mobs que son pacíficos y aparecen en el Nether :",list(set_pacificos & set_Nether))
print("d) Mobs presentes en las tres listas a la vez :",list(set_hostiles & set_Nether & set_pacificos))
print("e) Todos los mobs que existen en las tres categorías :", list(set_hostiles | set_Nether | set_pacificos))
print("f) Mobs del Nether que no son hostiles: ", list(set_Nether - set_hostiles))
print("g) ¿Alguna lista tiene mobs repetidos? :")
repetidosHostiles = len(set_hostiles) != len(set_hostiles)

if repetidosHostiles:
    print("Los hostiles tienen repetidos")
else:
    print("Los hostiles no tienen repetidos")
repetidosNether = len(set_Nether) != len(set_Nether)

if repetidosNether:
    print("Los del nether tienen repetidos")
else:
    print("Los del nether no tienen repetidos")
repetidosPacificos =  len(set_pacificos) != len(set_pacificos)

if repetidosPacificos:
    print("Los pacíficos tienen repetidos")
else:
    print("Los pacíficos no tienen repetidos")

print("h) Mobs que son hostiles o pacíficos, pero no del Nether: ", list((set_hostiles | set_pacificos )- set_Nether)) 