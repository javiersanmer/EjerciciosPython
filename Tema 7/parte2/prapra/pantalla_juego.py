import tkinter as tk
import random


class PantallaJuego(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app

        self.label = tk.Label(self, font=("Arial", 16))
        self.label.pack(pady=20)

        self.btn_pedir = tk.Button(self, command=self.pedir)
        self.btn_pedir.pack(pady=5)

        self.btn_plantarse = tk.Button(self, command=self.plantarse)
        self.btn_plantarse.pack(pady=5)

        self.btn_volver = tk.Button(
            self,
            command=lambda: self.app.mostrar(self.app.p_inicio)
        )
        self.btn_volver.pack(pady=10)

        self.iniciar()

    def actualizar(self):
        self.btn_pedir.config(text=self.app.t("juego_pedir"))
        self.btn_plantarse.config(text=self.app.t("juego_plantarse"))
        self.btn_volver.config(text=self.app.t("juego_volver"))
        self.iniciar()

    def iniciar(self):
        self.jugador = [self.carta(), self.carta()]
        self.banca = [self.carta(), self.carta()]
        self.mostrar()

    def carta(self):
        return random.randint(1, 11)

    def total(self, mano):
        return sum(mano)

    def mostrar(self, final=""):
        self.label.config(
            text=f"Jugador: {self.jugador} = {self.total(self.jugador)}\n"
                 f"Banca: [{self.banca[0]}, ?]\n{final}"
        )

    def pedir(self):
        self.jugador.append(self.carta())

        if self.total(self.jugador) > 21:
            self.mostrar(self.app.t("juego_perder"))
        else:
            self.mostrar()

    def plantarse(self):
        limite = 16 if self.app.config["dificultad"] == "facil" else 18

        while self.total(self.banca) < limite:
            self.banca.append(self.carta())

        self.final()

    def final(self):
        j = self.total(self.jugador)
        b = self.total(self.banca)

        if b > 21 or j > b:
            res = self.app.t("juego_ganar")
        elif j == b:
            res = self.app.t("juego_empate")
        else:
            res = self.app.t("juego_perder")

        self.label.config(
            text=f"Jugador: {self.jugador} = {j}\n"
                 f"Banca: {self.banca} = {b}\n{res}"
        )