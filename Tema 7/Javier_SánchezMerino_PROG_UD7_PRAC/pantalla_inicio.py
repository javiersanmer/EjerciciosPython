import tkinter as tk


class PantallaInicio(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root, bg="#1e1e2f")
        self.app = app

        titulo = tk.Label(
            self,
            text="Continúa la secuencia",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#1e1e2f"
        )
        titulo.pack(pady=(80, 20))

        subtitulo = tk.Label(
            self,
            text="Adivina el siguiente número de cada serie",
            font=("Arial", 13),
            fg="#cbd5e1",
            bg="#1e1e2f"
        )
        subtitulo.pack(pady=(0, 40))

        boton_jugar = tk.Button(
            self,
            text="Jugar",
            command=lambda: self.app.mostrar(self.app.p_juego),
            bg="#22c55e",
            fg="white",
            width=20,
            relief="flat",
            font=("Arial", 11)
        )
        boton_jugar.pack(pady=8)

        boton_config = tk.Button(
            self,
            text="Configuración",
            command=lambda: self.app.mostrar(self.app.p_config),
            bg="#4f46e5",
            fg="white",
            width=20,
            relief="flat",
            font=("Arial", 11)
        )
        boton_config.pack(pady=8)

        boton_salir = tk.Button(
            self,
            text="Salir",
            command=self.app.root.destroy,
            bg="#ef4444",
            fg="white",
            width=20,
            relief="flat",
            font=("Arial", 11)
        )
        boton_salir.pack(pady=8)