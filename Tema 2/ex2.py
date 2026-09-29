libraCon = 0.453592
cifra = 1
def convertidorLibras(cifra: float) -> float:
    convertidor = cifra / libraCon
    print(f"{cifra} kilos son {convertidor} libras")


while cifra > 0:
    cifra = float(input("Introduce un peso en kilogramos: "))
    convertidorLibras(cifra)

'''def convertidorLibras(cifra: float) -> float:
    return cifra / 0.5435


while True:
    cifra = float(input("Introduce un peso en kilogramos: "))
    noseve'''