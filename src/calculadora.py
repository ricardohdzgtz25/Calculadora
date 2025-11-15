import tkinter as tk
from tkinter import ttk

def aplicar_estilos(ventana):
    style = ttk.style(ventana)
    style.theme_use("default")

    # Fondo Suave Menta
    ventana.configure(bg="#E8F5F3")

    #Estilo para botones
    style.configure(
        "TButton",
        font=("Arial", 11, "bold"),
        padding=6,
        background="#2F5C63",
        foreground="white",
        borderwidth=0
    )

    style.map(
        "TButton",
        background=[("active", "#3F6E75")] 
    )

    # Pantalla de la calculadora
    style.configure(
        "Entrada.TEntry",
        foreground="black",
        fieldbackground="#D9EFEB", 
        borderwidth=3
    )


# FUNCIONES DE LA CALCULADORA
historial = []

def click_boton(valor):
    historial.append(pantalla.get())
    entrada_actual = pantalla.get()
    pantalla.delete(0, tk.END)
    pantalla.insert(0, entrada_actual + str(valor))

def borrar_uno():
    entrada_actual = pantalla.get()
    if entrada_actual:  
        historial.append(entrada_actual)
    pantalla.delete(0, tk.END)
    pantalla.insert(0, entrada_actual[:-1])

def borrar_todo():
    historial.append(pantalla.get())
    pantalla.delete(0, tk.END)

def calcular():
    try:
        historial.append(pantalla.get())  
        resultado = eval(pantalla.get())
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")

def deshacer():
    if historial:
        ultimo_valor = historial.pop()
        pantalla.delete(0, tk.END)
        pantalla.insert(0, ultimo_valor)

# VENTANA PRINCIPAL

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")
ventana.resizable(False, False)

pantalla = tk.Entry(ventana, font=("Arial", 24), justify="right")
pantalla.pack(fill="both", padx=10, pady=10)


# BOTONES
botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

frame_botones = tk.Frame(ventana)
frame_botones.pack()

for texto, fila, col in botones:
    if texto == "=":
        tk.Button(frame_botones, text=texto, width=5, height=2,
                  command=calcular).grid(row=fila, column=col, padx=5, pady=5)

    else:
        tk.Button(frame_botones, text=texto, width=5, height=2,
                  command=lambda t=texto: click_boton(t)).grid(row=fila, column=col, padx=5, pady=5)

#Botones especiales
btn_borrar = tk.Button(ventana, 
text="Borrar Uno", 
width=10, 
command=borrar_uno)
btn_borrar.pack(pady=5)

btn_borrar_todo = tk.Button(ventana, 
text="Borrar Todo",
width=10, command=borrar_todo)
btn_borrar_todo.pack(pady=5)
btn_deshacer = tk.Button(ventana, text="Deshacer",width=10, command=deshacer)
btn_deshacer.pack(pady=5)
ventana.mainloop()



