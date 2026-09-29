import tkinter as tk

# Funciones
def click(valor):
    pantalla.insert(tk.END, valor)

def borrar():
    pantalla.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(pantalla.get())
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")

# Ventana
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")

# Pantalla
pantalla = tk.Entry(
    ventana,
    font=("Arial", 24),
    justify="right"
)
pantalla.grid(row=0, column=0, columnspan=4, sticky="nsew", ipady=20)

# Configurar grid adaptable
for i in range(5):
    ventana.rowconfigure(i, weight=1)
for i in range(4):
    ventana.columnconfigure(i, weight=1)

# Botones
botones = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

# Crear botones con for
for fila, fila_botones in enumerate(botones):
    for col, texto in enumerate(fila_botones):

        if texto == "C":
            comando = borrar
        elif texto == "=":
            comando = calcular
        else:
            comando = lambda t=texto: click(t)

        boton = tk.Button(
            ventana,
            text=texto,
            font=("Arial", 16),
            command=comando
        )
        boton.grid(row=fila+1, column=col, sticky="nsew")
        
ventana.mainloop()