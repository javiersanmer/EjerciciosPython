import tkinter as tk

class Pantalla1:
    def __init__(self, app):
        self.app = app

        tk.Label(
            app.root,
            text=app.t("Menú Principal", "Main Menu"),
            font=("Arial", 16)
        ).pack(pady=20)

        tk.Button(
            app.root,
            text=app.t("Empezar", "Start"),
            width=25,
            command=app.show_pantalla2
        ).pack(pady=10)

        tk.Button(
            app.root,
            text=app.t("Configurar", "Settings"),
            width=25,
            command=app.show_pantalla3
        ).pack(pady=10)