import json
import tkinter as tk
from pathlib import Path

from pantalla_inicio import PantallaInicio
from pantalla_juego import PantallaJuego
from pantalla_config import PantallaConfig


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.textos = self.cargar_textos()
        self.config = self.cargar_config()

        self.p_inicio = PantallaInicio(self)
        self.p_juego = PantallaJuego(self)
        self.p_config = PantallaConfig(self)

        self.pantalla_actual = None
        self.mostrar(self.p_inicio)

    def cargar_textos(self):
        ruta = Path(__file__).parent / "textos.json"
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)

    def cargar_config(self):
        try:
            ruta = Path(__file__).parent / "config.json"
            with open(ruta, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {"dificultad": "facil", "dinero_inicial": 500, "idioma": "ES"}

    def guardar_config(self):
        ruta = Path(__file__).parent / "config.json"
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(self.config, f, ensure_ascii=False, indent=4)

    def t(self, clave):
        return self.textos[self.config["idioma"]][clave]

    def mostrar(self, pantalla):
        if self.pantalla_actual:
            self.pantalla_actual.pack_forget()

        if hasattr(pantalla, "actualizar"):
            pantalla.actualizar()
        if hasattr(pantalla, "cargar_valores"):
            pantalla.cargar_valores()

        self.pantalla_actual = pantalla
        self.pantalla_actual.pack(fill="both", expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()