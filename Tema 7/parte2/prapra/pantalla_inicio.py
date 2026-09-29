import tkinter as tk


class PantallaInicio(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app

        tk.Label(self, text="BLACKJACK", font=("Arial", 24)).pack(pady=30)

        self.btn_jugar = tk.Button(
            self,
            command=lambda: self.app.mostrar(self.app.p_juego),
            width=18
        )
        self.btn_jugar.pack(pady=10)

        self.btn_config = tk.Button(
            self,
            command=lambda: self.app.mostrar(self.app.p_config),
            width=18
        )
        self.btn_config.pack(pady=10)

    def actualizar(self):
        self.btn_jugar.config(text=self.app.t("inicio_empezar"))
        self.btn_config.config(text=self.app.t("inicio_configurar"))