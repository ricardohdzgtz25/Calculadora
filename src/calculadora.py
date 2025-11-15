import tkinter as tk
from tkinter import ttk

# FUNCIONES DE LA CALCULADORA
def click_boton(valor):
    entrada_actual = pantalla.get()
    pantalla.delete(0, tk.END)
    pantalla.insert(0, entrada_actual + str(valor))

def borrar_uno():
    entrada_actual = pantalla.get()
    pantalla.delete(0, tk.END)
    pantalla.insert(0, entrada_actual[:-1])

def borrar_todo():
    pantalla.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(pantalla.get())
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")

















