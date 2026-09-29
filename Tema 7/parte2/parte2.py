import tkinter as tk
import math
import random

# Ventana
ancho, alto = 800, 400
ventana = tk.Tk()
ventana.title("Mini Angry Birds Pro")
canvas = tk.Canvas(ventana, width=ancho, height=alto, bg="skyblue")
canvas.pack()

# Suelo
canvas.create_rectangle(0, alto-20, ancho, alto, fill="sienna")

# Variables
radio = 15
gravedad = 0.5
vel_x = 0
vel_y = 0
arrastrando = False
linea = None
pos_x, pos_y = 100, alto-50

# Pájaro inicial
pajaros_disponibles = [
    canvas.create_oval(pos_x-radio, pos_y-radio, pos_x+radio, pos_y+radio, fill="red"),
    canvas.create_oval(pos_x-radio, pos_y-radio, pos_x+radio, pos_y+radio, fill="orange"),
    canvas.create_oval(pos_x-radio, pos_y-radio, pos_x+radio, pos_y+radio, fill="yellow")
]
pajaros_disponibles.reverse()  # Para sacar primero el rojo
pajaro = pajaros_disponibles.pop()

# Bloques
obstaculos = []
for i in range(3):
    rect = canvas.create_rectangle(500+i*40, alto-60-(i*40), 530+i*40, alto-20-(i*40), fill="brown")
    obstaculos.append(rect)

# Cerdos
cerdos = []
for i in range(2):
    c = canvas.create_oval(510+i*60, alto-80, 530+i*60, alto-60, fill="green")
    cerdos.append(c)

# Funciones
def start_drag(event):
    global arrastrando
    if math.hypot(event.x - pos_x, event.y - pos_y) <= radio:
        arrastrando = True

def drag(event):
    global linea
    if arrastrando:
        global pos_x, pos_y
        # Dibujar línea del tirachinas
        if linea:
            canvas.delete(linea)
        linea = canvas.create_line(pos_x, pos_y, event.x, event.y, fill="black", width=2)
        canvas.coords(pajaro, event.x-radio, event.y-radio, event.x+radio, event.y+radio)

def stop_drag(event):
    global arrastrando, vel_x, vel_y, linea
    if arrastrando:
        dx = pos_x - event.x
        dy = pos_y - event.y
        vel_x = dx / 5
        vel_y = dy / 5
        arrastrando = False
        if linea:
            canvas.delete(linea)

def reiniciar_pajaro():
    global pajaro, pos_x, pos_y, vel_x, vel_y
    if pajaros_disponibles:
        pajaro = pajaros_disponibles.pop()
        pos_x, pos_y = 100, alto-50
        vel_x = 0
        vel_y = 0
        canvas.coords(pajaro, pos_x-radio, pos_y-radio, pos_x+radio, pos_y+radio)
    else:
        canvas.create_text(ancho//2, alto//2, text="¡Juego terminado!", font=("Arial", 24), fill="red")

def mover_pajaro():
    global pos_x, pos_y, vel_x, vel_y
    if not arrastrando:
        vel_y += gravedad
        pos_x += vel_x
        pos_y += vel_y

        # Rebote con suelo y paredes
        if pos_y + radio >= alto-20:
            pos_y = alto-20 - radio
            vel_y *= -0.5
            vel_x *= 0.9
        if pos_x - radio <= 0 or pos_x + radio >= ancho:
            vel_x *= -0.5

        # Colisión con bloques
        for obs in obstaculos[:]:
            ox1, oy1, ox2, oy2 = canvas.coords(obs)
            if ox1 < pos_x < ox2 and oy1 < pos_y < oy2:
                canvas.delete(obs)
                obstaculos.remove(obs)
                vel_x *= 0.7
                vel_y *= -0.7

        # Colisión con cerdos
        for cerdo in cerdos[:]:
            cx1, cy1, cx2, cy2 = canvas.coords(cerdo)
            if cx1 < pos_x < cx2 and cy1 < pos_y < cy2:
                canvas.delete(cerdo)
                cerdos.remove(cerdo)
                vel_x *= 0.7
                vel_y *= -0.7

        # Actualizar posición
        canvas.coords(pajaro, pos_x-radio, pos_y-radio, pos_x+radio, pos_y+radio)

        # Si el pájaro se detiene o sale del canvas, lanzar siguiente
        if (abs(vel_x) < 0.5 and abs(vel_y) < 0.5) or pos_y > alto:
            if cerdos:
                reiniciar_pajaro()
            else:
                canvas.create_text(ancho//2, alto//2, text="¡Victoria!", font=("Arial", 36), fill="gold")

    ventana.after(20, mover_pajaro)

# Eventos
canvas.bind("<Button-1>", start_drag)
canvas.bind("<B1-Motion>", drag)
canvas.bind("<ButtonRelease-1>", stop_drag)

# Iniciar juego
mover_pajaro()
ventana.mainloop()