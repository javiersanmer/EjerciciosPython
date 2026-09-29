def mayorIgual(lista : list[int], n: int)-> bool:
    return n <= min(lista)

lista = [5,2,6,2,8]
n = 5

print(mayorIgual(lista,n))