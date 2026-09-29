import random
from pathlib import Path


def leer_configuracion(configuracion: str) -> dict[str, str | int | list]:
    config = {}

    with open(configuracion, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                clave, valor = linea.strip().split("=")
                config[clave] = valor

    return config


def jugar(config: dict):
    minimo = int(config["min"])
    maximo = int(config["max"])
    n_vidas = int(config["n_vidas"])
    config["operaciones"] = config["operaciones"].split(",")

    recordsJuga = []
    n_vidas_nuevas = n_vidas
    contador = 0
    while True:
        print("1. Jugar")
        print("2. Configuración")
        print("3. Ver ranking")
        print("4. Salir")

        opcionMenu = int(input("Elige una opción: "))

        n_vidas = n_vidas_nuevas

        if opcionMenu == 1:
            while n_vidas > 0:
                n1 = random.randint(minimo,maximo)
                n2 = random.randint(minimo,maximo)
                print(f"{n1} {operaciones} {n2}")

                if operaciones == "+":
                    resultado = n1 + n2
                elif operaciones == "-":
                    resultado = n1 - n2
                elif operaciones == "x":
                    resultado = n1 * n2

                resultadoUsuario = int(input("Tu respuesta: "))
                if resultado == resultadoUsuario:
                    print("Correcto")
                    contador += 1
                else:
                    print(f"Incorrecto. El resultado era: {resultado}")
                    n_vidas -= 1
                    print(f"Te quedan: {n_vidas} vidas.")

            if len(recordsJuga) <= 5:
                recordsJuga.append(contador)

        elif opcionMenu == 2:
            print(f"Configuración actual: num min = {minimo}, num max = {maximo}, operacion = {operaciones}, vidas = {n_vidas}")

            cambia_config = input("¿Quieres cambiar la configuración (S/N): ?")

            if cambia_config == "S":
                minimo = int(input("Introduce el mín: "))
                config["tipo_dado"] = minimo
                
                maximo = int(input("Introduce el max: "))
                config["tipo_dado"] = maximo

                operaciones = input("Introduce el símbolo de la operación: ")
                config["tipo_dado"] = operaciones

                n_vidas_nuevas = int(input("Introduce el número de vidas: "))
                config["tipo_dado"] = n_vidas_nuevas
        
        elif opcionMenu == 3:

            with open(records, "a", encoding="utf-8") as f:
                    
                for i, r in enumerate(recordsJuga):
                    if records[:5]:
                        f.write(
                            f"Jugador: {i}, {recordsJuga[i]} puntos\n"
                        )

if __name__ == "__main__":
    configuracion = Path(__file__).parent / "config.txt"
    records = Path(__file__).parent / "records.txt"
    config = leer_configuracion(configuracion)
    jugar(config)