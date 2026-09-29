from random import randint
from pathlib import Path

def leer_configuracion(nombre_archivo: str) -> dict:
    config = {}

    with open(nombre_archivo, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                clave, valor = linea.strip().split("=")
                config[clave] = valor
    return config

def jugar(config: dict):
    tablas = [int(x) for x in config["tablas"].split(",")]
    preguntas = int(config["preguntas"])

    if preguntas == -1:
        while True:            
            tabla = tablas[randint(0, len(tablas) - 1)] 
            numero = randint(0,10)
            resultadoCorrecto = tabla * numero
            print(f"{tabla} * {numero}")
            
            resultado = int(input("Introduce el resultado: "))
            if resultadoCorrecto == resultado:
                print("Correcto")
            else:
                print(f"Incorrecto. La respuesta era {resultadoCorrecto}")
    
    while preguntas > 0:
        tabla = tablas[randint(0, len(tablas) - 1)] 
        numero = randint(0,10)
        resultadoCorrecto = tabla * numero
        print(f"{tabla} * {numero}")
            
        resultado = int(input("Introduce el resultado: "))
        if resultadoCorrecto == resultado:
            print("Correcto")
        else:
            print(f"Incorrecto. La respuesta era {resultadoCorrecto}")
        preguntas -= 1

if __name__ == "__main__":
    nombre_archivo = Path(__file__).parent / "tablasMulti.txt"
    config = leer_configuracion(nombre_archivo)
    jugar(config)