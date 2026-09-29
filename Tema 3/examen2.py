pedrolos = [
    ["Cuarzo",     2.65, False],
    ["Pirita",     5.02, False],
    ["Hematita",   5.26, False],
    ["Galena",     7.6,  False],
    ["Fluorita",   3.18, False],
    ["Calcita",    2.71, False],
    ["Magnetita",  5.17, True ],
    ["Malaquita",  3.9,  False],
    ["Obsid<iana",  2.4,  False],
    ["Apatito",    3.2,  False]
]

apartadoA = [p[0] for p in pedrolos if len(p[0]) <= 7 and p[0][-1] != "a"]
print(apartadoA)

media = 0
for pedrolo in pedrolos:
    media += pedrolo[1]
media /= len(pedrolos) 

# O mejor
mediaPedrolo = [pedrolo[1] for pedrolo in pedrolos]
mediaPedrolosTotal = sum(mediaPedrolo)/len(mediaPedrolo)

apartadoB = [p[0] for p in pedrolos if not p[2] and p[1] > media]
print(apartadoB)

apartadoC = [p[0] for p in pedrolos if ('p' in p[0].lower() or 't' in p[0].lower()) and not ('p' in p[0].lower() and 't' in p[0].lower())] 
print(apartadoC)

apartadoD = [p[0] for p in pedrolos if p[2] and len(p[0]) % 2 == 1]
print(apartadoD)
