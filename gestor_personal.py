"""
SISTEMA PYTHON SIMPLIFICADO
Proyecto educativo con conceptos básicos de Python
"""

#VARIABLES
nombre_sistema = "Mi Sistema Python"
version = 1.0
activo = True
contador = 0

# ESTRUCTURAS DE DATOS
contactos = {}
historial = []

# FUNCIONES

def convertir_temperatura(valor, de_tipo, a_tipo):
    """Convierte entre Celcius, Fahrenheit y Kelvin"""
    if de_tipo == 'C':
        celsius = valor
    elif de_tipo == 'F':
        celcius = (valor - 32) * 5/9
    else:
        celsius = valor - 273.15

    if a_tipo == 'C':
        return celsius
    elif a_tipo == 'F':
        return celsius * 9/5 + 32
    else:
        return celcius + 273.15

def calcular_factorial(n):
    """Calcula el factorial usando bucle"""
    if n < 0:
        return None
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado



