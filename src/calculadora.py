import tkinter as tk
from tkinter import ttk

# FUNCIONES DE LA CALCULADORA
def click_boton(valor):
    entrada_actual = pantalla.get()
    pantalla.delete(0, tk.END)
    pantalla.insert(0, entrada_actual + str(valor))


















