import tkinter as tk
import math

def sin_deg(x): return math.sin(math.radians(x))
def cos_deg(x): return math.cos(math.radians(x))
def tan_deg(x): return math.tan(math.radians(x))

def asin_deg(x): return math.degrees(math.asin(x))
def acos_deg(x): return math.degrees(math.acos(x))
def atan_deg(x): return math.degrees(math.atan(x))

ALLOWED_NAMES = {
    'pi': math.pi, 'e': math.e,
    'sin': sin_deg, 'cos': cos_deg, 'tan': tan_deg,
    'asin': asin_deg, 'acos': acos_deg, 'atan': atan_deg,
    'ln': math.log, 'log': math.log, 'exp': math.exp,
    'sqrt': math.sqrt, 'pow': math.pow, 'abs': abs
}

OPERADORES = "+-*/^."

def sanitize_expression(expr: str) -> str:
    expr = expr.replace('^', '**').replace(',', '.')
    return expr

def safe_eval(expression: str):
    return eval(expression, {"__builtins__": None}, ALLOWED_NAMES)
