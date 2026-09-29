import json
import tkinter as tk
from pathlib import Path
import random

from pantalla_inicio import PantallaInicio
from pantalla_adivina_secuencia import PantallaJuego
from pantalla_configuracion import PantallaConfig


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Continúa la secuencia")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2f")

        self.config = self.cargar_config()
        self.secuencias_usadas = []

        self.p_inicio = PantallaInicio(self)
        self.p_juego = PantallaJuego(self)
        self.p_config = PantallaConfig(self)

        self.pantalla_actual = None
        self.mostrar(self.p_inicio)

    def config_defecto(self):
        return {
            "dificultad": "facil",
            "vidas": 3,
            "pista": False,
        }

    def cargar_config(self):
        ruta = Path(__file__).with_name("config.json")
        config = self.config_defecto()

        try:
            if ruta.exists():
                with open(ruta, "r", encoding="utf-8") as f:
                    datos = json.load(f)

                if isinstance(datos, dict):
                    config.update(datos)
        except Exception:
            pass

        if config["dificultad"] not in ("facil", "medio", "dificil"):
            config["dificultad"] = "facil"

        try:
            config["vidas"] = int(config["vidas"])
        except (TypeError, ValueError):
            config["vidas"] = 3

        config["vidas"] = max(1, min(10, config["vidas"]))
        config["pista"] = bool(config.get("pista", False))

        return config

    def guardar_config(self):
        ruta = Path(__file__).with_name("config.json")
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(self.config, f, ensure_ascii=False, indent=4)

    def total_secuencias(self):
        if self.config["dificultad"] == "dificil":
            return 15
        return 10

    def generar_secuencia(self):
        dificultad = self.config["dificultad"]

        facil = [
            ([2, 4, 6, 8], 10),
            ([1, 2, 3, 4], 5),
            ([5, 10, 15, 20], 25),
            ([3, 6, 9, 12], 15),
            ([10, 20, 30, 40], 50),
            ([4, 8, 12, 16], 20),
            ([7, 14, 21, 28], 35),
            ([1, 3, 5, 7], 9),
            ([6, 12, 18, 24], 30),
            ([9, 18, 27, 36], 45),
        ]

        medio = [
            ([2, 4, 8, 16], 32),
            ([3, 6, 12, 24], 48),
            ([5, 10, 20, 40], 80),
            ([1, 4, 9, 16], 25),
            ([2, 5, 10, 17], 26),
            ([7, 10, 16, 25], 37),
            ([3, 9, 27, 81], 243),
            ([8, 16, 32, 64], 128),
            ([11, 22, 44, 88], 176),
            ([1, 2, 4, 7, 11], 16),
        ]

        dificil = [
            ([1, 1, 2, 3, 5], 8),
            ([2, 3, 5, 8, 13], 21),
            ([1, 4, 9, 16, 25], 36),
            ([1, 8, 27, 64, 125], 216),
            ([2, 6, 12, 20, 30], 42),
            ([10, 9, 7, 4, 0], -5),
            ([3, 6, 12, 24, 48], 96),
            ([5, 15, 45, 135], 405),
            ([1, 2, 4, 7, 11, 16], 22),
            ([2, 4, 7, 11, 16], 22),
            ([1, 3, 6, 10, 15], 21),
            ([4, 9, 16, 25, 36], 49),
            ([2, 5, 11, 23, 47], 95),
            ([1, 2, 6, 24, 120], 720),
            ([7, 14, 28, 56, 112], 224),
        ]

        if dificultad == "facil":
            lista = facil
        elif dificultad == "medio":
            lista = medio
        else:
            lista = dificil

        disponibles = [s for s in lista if s not in self.secuencias_usadas]

        if not disponibles:
            return None

        return random.choice(disponibles)

    def mostrar(self, pantalla):
        if self.pantalla_actual is not None:
            self.pantalla_actual.pack_forget()

        self.pantalla_actual = pantalla

        if hasattr(pantalla, "cargar_valores"):
            pantalla.cargar_valores()

        self.pantalla_actual.pack(fill="both", expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()