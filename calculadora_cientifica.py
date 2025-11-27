import tkinter as tk
import math

ALLOWED_NAMES = {
    'pi': math.pi,
    'e': math.e,
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'asin': math.asin,
    'acos': math.acos,
    'atan': math.atan,
    'ln': math.log,
    'log': math.log,
    'exp': math.exp,
    'sqrt': math.sqrt,
    'pow': math.pow,
    'abs': abs
}

OPERADORES = "+-*/^."

def sanitize_expression(expr: str) -> str:
    expr = expr.replace('^', '**')
    expr = expr.replace(',', '.')
    return expr

def safe_eval(expression: str):
    try:
        return eval(expression, {"__builtins__": None}, ALLOWED_NAMES)
    except Exception:
        raise
