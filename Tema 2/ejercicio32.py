terminos = int(input("Introduce los términos: "))
contador = 1

primerTerm = 0
segundoTerm = 1
while contador < terminos:
    if contador == 1:
        primerTerm = 0
        print(primerTerm)
    if contador == 2:
        segundoTerm = 1
        print(segundoTerm)
    if contador > 3:
        nuevoTerm = primerTerm+segundoTerm
        print(nuevoTerm)
        primerTerm=segundoTerm
        segundoTerm = nuevoTerm
    contador = contador + 1