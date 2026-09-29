import tkinter as tk
from tkinter import ttk, messagebox

class Pantalla3:
    def __init__(self, app):
        self.app = app

        tk.Label(
            app.root,
            text=app.t("Configuración", "Settings"),
            font=("Arial", 16)
        ).pack(pady=10)

        tk.Label(
            app.root,
            text=app.t("Número de caras del dado:", "Dice sides:")
        ).pack()

        self.entry = tk.Entry(app.root)
        self.entry.pack(pady=5)
        self.entry.insert(0, str(app.dice_sides))

        tk.Label(
            app.root,
            text=app.t("Idioma:", "Language:")
        ).pack(pady=5)

        self.lang_var = tk.StringVar(value=app.language)

        ttk.Combobox(
            app.root,
            values=["Español", "Inglés"],
            textvariable=self.lang_var
        ).pack()

        tk.Button(
            app.root,
            text=app.t("Guardar", "Save"),
            command=self.guardar
        ).pack(pady=10)

        tk.Button(
            app.root,
            text=app.t("Volver", "Back"),
            command=app.show_pantalla1
        ).pack()

    def guardar(self):
        try:
            value = int(self.entry.get())
            if value < 2:
                messagebox.showerror("Error", "Mínimo 2 caras")
                return
            self.app.dice_sides = value
        except:
            messagebox.showerror("Error", "Número inválido")
            return

        self.app.language = self.lang_var.get()
        self.app.show_pantalla1()