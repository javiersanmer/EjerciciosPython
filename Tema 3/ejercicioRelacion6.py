def sumaMatrices(m1 : list[list[float]], m2: list[list[float]]) -> list[list[float]]:
    m3 = m1.copy()

    for i, fila in enumerate(m1):
        for j,_ in enumerate(fila):
            m3[i][j] = m1[i][j] + m2[i][j]
    
    return m3