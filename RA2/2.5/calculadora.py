# Autor: Cristian Jorda Matei
# Data: 8/11/2025
# Mòdul calculadora.py - Funcions de suma, resta, multiplicació i divisió.

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacio(a, b):
    return a * b

def divisio(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No es pot dividir per zero"