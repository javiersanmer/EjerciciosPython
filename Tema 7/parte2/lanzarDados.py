import tkinter as tk
from tkinter import ttk, messagebox
import random

class DiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Dados")
        self.root.geometry("400x300")

        # Configuración por defecto
        self.dice_sides = 20
        self.language = "Español"

        self.main_menu()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # ---------------- MAIN MENU ----------------
    def main_menu(self):
        self.clear()

        title = tk.Label(self.root, text="Menú Principal", font=("Arial", 16))
        title.pack(pady=20)

        start_btn = tk.Button(self.root, text="Empezar", command=self.start_menu, width=20)
        start_btn.pack(pady=10)

        config_btn = tk.Button(self.root, text="Configurar", command=self.config_menu, width=20)
        config_btn.pack(pady=10)

    # ---------------- CONFIG MENU ----------------
    def config_menu(self):
        self.clear()

        tk.Label(self.root, text="Configuración", font=("Arial", 16)).pack(pady=10)

        # Dados (entrada personalizada)
        tk.Label(self.root, text="Número de caras del dado:").pack()
        self.dice_entry = tk.Entry(self.root)
        self.dice_entry.pack(pady=5)
        self.dice_entry.insert(0, str(self.dice_sides))

        # Idioma
        tk.Label(self.root, text="Idioma:").pack(pady=5)
        self.lang_var = tk.StringVar(value=self.language)
        lang_options = ["Español", "Inglés"]
        ttk.Combobox(self.root, values=lang_options, textvariable=self.lang_var).pack()

        # Botones
        save_btn = tk.Button(self.root, text="Guardar y volver", command=self.save_config)
        save_btn.pack(pady=10)

        back_btn = tk.Button(self.root, text="Volver", command=self.main_menu)
        back_btn.pack()

    def save_config(self):
        try:
            value = int(self.dice_entry.get())
            if value < 2:
                messagebox.showerror("Error", "El dado debe tener al menos 2 caras")
                return
            self.dice_sides = value
        except:
            messagebox.showerror("Error", "Introduce un número válido")
            return

        self.language = self.lang_var.get()
        self.main_menu()

    # ---------------- START MENU ----------------
    def start_menu(self):
        self.clear()

        tk.Label(self.root, text="Lanzador de Dados", font=("Arial", 16)).pack(pady=10)

        self.result_label = tk.Label(self.root, text="Resultado: -", font=("Arial", 14))
        self.result_label.pack(pady=10)

        roll_btn = tk.Button(self.root, text="Lanzar dado", command=self.roll_dice, width=20)
        roll_btn.pack(pady=10)

        back_btn = tk.Button(self.root, text="Volver", command=self.main_menu)
        back_btn.pack()

    def roll_dice(self):
        result = random.randint(1, self.dice_sides)
        self.result_label.config(text=f"Resultado: {result}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceApp(root)
    root.mainloop()