import tkinter as tk


class PantallaConfig(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app

        self.label_dinero = tk.Label(self)
        self.label_dinero.pack(pady=10)

        self.entry_dinero = tk.Entry(self, justify="center")
        self.entry_dinero.pack()

        self.label_dificultad = tk.Label(self)
        self.label_dificultad.pack(pady=10)

        self.dificultad_var = tk.StringVar()
        self.menu = tk.OptionMenu(self, self.dificultad_var, "facil", "dificil")
        self.menu.pack()

        self.btn_guardar = tk.Button(self, command=self.guardar)
        self.btn_guardar.pack(pady=10)

        self.btn_volver = tk.Button(
            self,
            command=lambda: self.app.mostrar(self.app.p_inicio)
        )
        self.btn_volver.pack()

    def cargar_valores(self):
        self.entry_dinero.delete(0, tk.END)
        self.entry_dinero.insert(0, str(self.app.config["dinero_inicial"]))
        self.dificultad_var.set(self.app.config["dificultad"])
        self.actualizar()

    def actualizar(self):
        self.label_dinero.config(text=self.app.t("config_titulo_dinero"))
        self.label_dificultad.config(text=self.app.t("config_titulo_dificultad"))
        self.btn_guardar.config(text=self.app.t("config_guardar"))
        self.btn_volver.config(text=self.app.t("config_volver"))

    def guardar(self):
        try:
            self.app.config["dinero_inicial"] = int(self.entry_dinero.get())
        except:
            pass

        self.app.config["dificultad"] = self.dificultad_var.get()
        self.app.guardar_config()
        self.app.mostrar(self.app.p_inicio)