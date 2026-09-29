import tkinter as tk


class PantallaJuego(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root, bg="#1e1e2f")
        self.app = app

        self.secuencia = []
        self.respuesta = 0
        self.vidas_actuales = 0
        self.ronda_actual = 1
        self.total_rondas = 0
        self.fallos = 0

        self.label_titulo = tk.Label(
            self,
            text="Secuencia",
            font=("Arial", 20, "bold"),
            fg="white",
            bg="#1e1e2f"
        )
        self.label_titulo.pack(pady=(20, 10))

        self.label_secuencia = tk.Label(
            self,
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#1e1e2f",
            padx=10,
            pady=10
        )
        self.label_secuencia.pack(pady=20)

        self.panel_info = tk.Frame(self, bg="#1e1e2f")
        self.panel_info.pack(pady=10)

        self.label_vidas = tk.Label(
            self.panel_info,
            font=("Arial", 14),
            fg="#fb7185",
            bg="#1e1e2f"
        )
        self.label_vidas.pack()

        self.label_progreso = tk.Label(
            self.panel_info,
            font=("Arial", 13),
            fg="#60a5fa",
            bg="#1e1e2f"
        )
        self.label_progreso.pack(pady=(5, 0))

        self.entry = tk.Entry(
            self,
            justify="center",
            font=("Arial", 16),
            bg="#2a2a3d",
            fg="white",
            insertbackground="white",
            disabledbackground="#1e1e2f",
            disabledforeground="#1e1e2f",
            relief="flat",
            bd=0
        )
        self.entry.pack(pady=10)

        self.label_info = tk.Label(
            self,
            font=("Arial", 13),
            fg="#e2e8f0",
            bg="#1e1e2f"
        )
        self.label_info.pack(pady=10)

        self.label_pista = tk.Label(
            self,
            font=("Arial", 13),
            fg="#facc15",
            bg="#1e1e2f"
        )
        self.label_pista.pack(pady=5)

        self.label_fallos_final = tk.Label(
            self,
            font=("Arial", 13, "bold"),
            fg="#e2e8f0",
            bg="#1e1e2f"
        )
        self.label_fallos_final.pack(pady=5)

        self.boton_comprobar = tk.Button(
            self,
            text="Comprobar",
            command=self.comprobar,
            bg="#22c55e",   
            fg="white",
            width=18,
            relief="flat"
        )
        self.boton_comprobar.pack(pady=10)

        self.boton_volver = tk.Button(
            self,
            text="Volver",
            command=lambda: self.app.mostrar(self.app.p_inicio),
            bg="#ef4444",
            fg="white",
            width=18,
            relief="flat"
        )
        self.boton_volver.pack(pady=10)

    def cargar_valores(self):
        self.app.secuencias_usadas = []
        self.vidas_actuales = self.app.config["vidas"]
        self.ronda_actual = 1
        self.total_rondas = self.app.total_secuencias()
        self.fallos = 0
        self.reset_ui()
        self.nueva_partida()

    def reset_ui(self):
        self.entry.config(
            state="normal",
            bg="#2a2a3d",
            fg="white",
            insertbackground="white"
        )
        self.boton_comprobar.config(state="normal")
        self.label_info.config(text="")
        self.label_pista.config(text="")
        self.label_fallos_final.config(text="")
        self.label_secuencia.config(text="", fg="white", bg="#1e1e2f")
        self.entry.delete(0, tk.END)
        self.actualizar_vidas()
        self.actualizar_progreso()

    def actualizar_vidas(self):
        self.label_vidas.config(text=f"Vidas: {self.vidas_actuales}")

    def actualizar_progreso(self):
        self.label_progreso.config(text=f"Progreso: {self.ronda_actual}/{self.total_rondas}")

    def obtener_tipo_pista(self):
        tipo = "general"
        difs = []

        for i in range(1, len(self.secuencia)):
            difs.append(self.secuencia[i] - self.secuencia[i - 1])

        if len(difs) > 0 and len(set(difs)) == 1:
            tipo = "suma"
        else:
            if len(self.secuencia) >= 2:
                ratios = []
                es_multiplicacion = True

                for i in range(1, len(self.secuencia)):
                    anterior = self.secuencia[i - 1]
                    actual = self.secuencia[i]

                    if anterior == 0 or actual % anterior != 0:
                        es_multiplicacion = False
                    else:
                        ratios.append(actual // anterior)

                if es_multiplicacion and len(ratios) > 0 and len(set(ratios)) == 1:
                    tipo = "multiplica"
                else:
                    if len(self.secuencia) >= 3:
                        if self.secuencia[-1] == self.secuencia[-2] + self.secuencia[-3]:
                            tipo = "fibonacci"

        return tipo

    def mostrar_pista(self):
        if self.app.config.get("pista", False):
            tipo = self.obtener_tipo_pista()

            if tipo == "suma":
                salto = self.secuencia[1] - self.secuencia[0]
                self.label_pista.config(text=f"La serie suma siempre {salto}.")
            else:
                if tipo == "multiplica":
                    factor = self.secuencia[1] // self.secuencia[0]
                    self.label_pista.config(text=f"La serie multiplica siempre por {factor}.")
                else:
                    if tipo == "fibonacci":
                        self.label_pista.config(text="Cada número se obtiene sumando los dos anteriores.")
                    else:
                        self.label_pista.config(text="Observa si la serie suma, resta o multiplica siempre lo mismo.")
        else:
            self.label_pista.config(text="")

    def mostrar_final(self, mensaje):
        self.label_info.config(text=mensaje)
        self.label_fallos_final.config(text=f"Fallos: {self.fallos}")
        self.entry.config(
            state="disabled",
            bg="#1e1e2f",
            disabledbackground="#1e1e2f",
            disabledforeground="#1e1e2f"
        )
        self.boton_comprobar.config(state="disabled")

    def mostrar_victoria(self):
        self.label_secuencia.config(
            text="Has ganado",
            fg="#22c55e",
            bg="#1e1e2f"
        )
        self.label_progreso.config(
            text=f"Progreso: {self.total_rondas}/{self.total_rondas}"
        )
        self.mostrar_final("Juego completado")

    def mostrar_derrota(self):
        self.mostrar_final(f"Has perdido. La respuesta era {self.respuesta}")

    def nueva_partida(self):
        if self.ronda_actual > self.total_rondas:
            self.mostrar_victoria()
        else:
            resultado = self.app.generar_secuencia()

            if resultado is None:
                self.mostrar_victoria()
            else:
                self.secuencia, self.respuesta = resultado
                self.app.secuencias_usadas.append(resultado)

                texto = " ".join(str(n) for n in self.secuencia)
                self.label_secuencia.config(text=f"{texto} ?")

                self.actualizar_vidas()
                self.actualizar_progreso()

    def comprobar(self):
        texto = self.entry.get().strip()

        if texto == "":
            self.label_info.config(text="")
        else:
            try:
                valor = int(texto)

                if valor == self.respuesta:
                    self.label_info.config(text="Correcto")
                    self.label_pista.config(text="")
                    self.entry.delete(0, tk.END)
                    self.ronda_actual += 1
                    self.nueva_partida()
                else:
                    self.fallos += 1
                    self.vidas_actuales -= 1
                    self.mostrar_pista()

                    if self.vidas_actuales <= 0:
                        self.actualizar_vidas()
                        self.mostrar_derrota()
                    else:
                        self.actualizar_vidas()
                        self.label_info.config(text="Incorrecto")
                        self.entry.delete(0, tk.END)

            except ValueError:
                self.label_info.config(text="Introduce un número válido")
                self.entry.delete(0, tk.END)