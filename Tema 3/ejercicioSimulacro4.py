def sin_repetidos(l : list[int]) -> list[int]:
    l2 = []
    for e in l:
        if l2.count(e) == 0:
            l2.append(e)

    return l2

l = [1,1,2,2,3,4,5,5]
print(sin_repetidos(l))