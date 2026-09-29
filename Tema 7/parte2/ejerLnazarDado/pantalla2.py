import tkinter as tk
import random

class Pantalla2:
    def __init__(self, app):
        self.app = app

        tk.Label(
            app.root,
            text=app.t("Lanzar Dado", "Roll Dice"),
            font=("Arial", 16)
        ).pack(pady=20)

        self.resultado = tk.Label(
            app.root,
            text=app.t("Resultado", "Result") + ": -",
            font=("Arial", 14)
        )
        self.resultado.pack(pady=10)

        tk.Button(
            app.root,
            text=app.t("Lanzar dado", "Roll dice"),
            width=25,
            command=self.lanzar
        ).pack(pady=10)

        tk.Button(
            app.root,
            text=app.t("Volver", "Back"),
            width=25,
            command=app.show_pantalla1
        ).pack(pady=10)

    def lanzar(self):
        resultado = random.randint(1, self.app.dice_sides)
        self.resultado.config(
            text=f"{self.app.t('Resultado', 'Result')}: {resultado}"
        )