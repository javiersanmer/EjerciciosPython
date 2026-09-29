import tkinter as tk
import json
import os
from pantalla1 import Pantalla1
from pantalla2 import Pantalla2
from pantalla3 import Pantalla3

CONFIG_FILE = "config.json"

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Dados")
        self.root.geometry("400x300")

        self.dice_sides = 20
        self.language = "Español"

        self.load_config()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.show_pantalla1()

    # ---------- IDIOMA ----------
    def t(self, es, en):
        return es if self.language == "Español" else en

    # ---------- CONFIG ----------
    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r") as f:
                    data = json.load(f)
                    self.dice_sides = int(data.get("dice_sides", 20))
                    self.language = data.get("language", "Español")
            except:
                pass

    def save_config(self):
        with open(CONFIG_FILE, "w") as f:
            json.dump({
                "dice_sides": self.dice_sides,
                "language": self.language
            }, f)

    def on_close(self):
        self.save_config()
        self.root.destroy()

    # ---------- NAV ----------
    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

    def show_pantalla1(self):
        self.clear()
        Pantalla1(self)

    def show_pantalla2(self):
        self.clear()
        Pantalla2(self)

    def show_pantalla3(self):
        self.clear()
        Pantalla3(self)


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()