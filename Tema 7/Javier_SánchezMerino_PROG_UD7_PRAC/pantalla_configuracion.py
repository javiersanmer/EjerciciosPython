import tkinter as tk


class PantallaConfig(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root, bg="#1e1e2f")
        self.app = app

        self.label_titulo = tk.Label(
            self,
            text="Configuración",
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#1e1e2f"
        )
        self.label_titulo.pack(pady=(20, 10))

        self.label_dificultad = tk.Label(
            self,
            text="Dificultad",
            fg="#a6b1ff",
            bg="#1e1e2f",
            font=("Arial", 12)
        )
        self.label_dificultad.pack(pady=(10, 5))

        self.dificultad_var = tk.StringVar(value="facil")

        self.menu_dificultad = tk.OptionMenu(
            self,
            self.dificultad_var,
            "facil",
            "medio",
            "dificil"
        )
        self.menu_dificultad.config(
            bg="#2e2e4a",
            fg="white",
            activebackground="#4c5bdc",
            activeforeground="white",
            highlightthickness=0,
            width=12,
            relief="flat"
        )
        self.menu_dificultad.pack()

        self.label_vidas = tk.Label(
            self,
            text="Vidas",
            fg="#ff7b7b",
            bg="#1e1e2f",
            font=("Arial", 12)
        )
        self.label_vidas.pack(pady=(15, 5))

        self.entry_vidas = tk.Entry(
            self,
            justify="center",
            bg="#2e2e4a",
            fg="white",
            insertbackground="white",
            relief="flat",
            font=("Arial", 12)
        )
        self.entry_vidas.pack()

        self.label_mensaje = tk.Label(
            self,
            text="",
            fg="#fca5a5",
            bg="#1e1e2f",
            font=("Arial", 11)
        )
        self.label_mensaje.pack(pady=(6, 0))

        self.pista_var = tk.BooleanVar()

        self.check_pista = tk.Checkbutton(
            self,
            text="Modo pista",
            variable=self.pista_var,
            bg="#1e1e2f",
            fg="#cfcfcf",
            selectcolor="#2e2e4a",
            activebackground="#1e1e2f",
            activeforeground="white",
            font=("Arial", 11)
        )
        self.check_pista.pack(pady=12)

        self.boton_guardar = tk.Button(
            self,
            text="Guardar cambios",
            command=self.guardar,
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            activeforeground="white",
            width=18,
            font=("Arial", 11),
            relief="flat"
        )
        self.boton_guardar.pack(pady=15)

        self.boton_volver = tk.Button(
            self,
            text="Volver",
            command=lambda: self.app.mostrar(self.app.p_inicio),
            bg="#f44336",
            fg="white",
            activebackground="#d93636",
            activeforeground="white",
            width=18,
            font=("Arial", 11),
            relief="flat"
        )
        self.boton_volver.pack(pady=5)

    def cargar_valores(self):
        self.dificultad_var.set(self.app.config["dificultad"])
        self.entry_vidas.delete(0, tk.END)
        self.entry_vidas.insert(0, str(self.app.config["vidas"]))
        self.pista_var.set(self.app.config.get("pista", False))
        self.label_mensaje.config(text="")

    def guardar(self):
        try:
            vidas = int(self.entry_vidas.get())

            if vidas < 1 or vidas > 10:
                self.label_mensaje.config(text="Introduce un número entre 1 y 10")
                return

            self.app.config["dificultad"] = self.dificultad_var.get()
            self.app.config["vidas"] = vidas
            self.app.config["pista"] = self.pista_var.get()

            self.app.guardar_config()
            self.app.config = self.app.cargar_config()
            self.app.mostrar(self.app.p_inicio)

        except ValueError:
            self.label_mensaje.config(text="Introduce un número válido")