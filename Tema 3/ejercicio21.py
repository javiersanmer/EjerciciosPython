ordenados = []

while True:
    num = int(input("Inserta un número: "))
    if num == 0:
        break
    else:
        if len(ordenados) == 0:
            ordenados.append(num)
        else:
            insertado = False
        
            for i in range(len(ordenados)):
                if num < ordenados[i]:
                    ordenados.insert(i, num)
                    insertado = True
                    break
            if not insertado:
                ordenados.append(num)
print(ordenados)