nota =""
def convertirdorNotas(nota : str) -> str:
    conversion = "Nota erronea"
    match nota:
        case "DO":
            conversion = "C"
        case "RE":
            conversion = "D"
        case "MI":
            conversion ="E"
        case "FA":
            conversion = "F"
        case "SOL":
            conversion = "G"
        case "LA":
            conversion = "A"
        case "SI":
            conversion = "B" 
    return conversion
'''
    if nota == "DO":
        return "C"
    elif nota == "Re":
        return "D"
    elif nota == "MI":
        return "E"
    elif nota == "FA":
        return "F" 
    elif nota == "SOL":
        return"G"
    elif nota == "LA":
        return "A" 
    else:
        return "B"
'''
while True:
    nota = input("Inseta una nota: ")
    if nota == "fin":
        break
    resultado = convertirdorNotas(nota)
    print(resultado)
