def multiplosTotales(n: int, inicio : int, final: int): #no devuelve nada pq pone muestre por pantalla
    multiplos = 0
    for i in range(inicio, final+1):
        if i % n == 0:
            multiplos = i
            print(multiplos)
    return multiplos

n = int(input("Introduce el n: "))
inicio = int(input("Introduce el incio: "))
final = int(input("Introduce el final: "))

print(f"Entre {inicio} y {final} el número {n} tiene los siguientes múltiplos: ")
multiplos = multiplosTotales(n, inicio, final)
