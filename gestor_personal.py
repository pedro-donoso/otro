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

    celcius = 0

    if de_tipo == 'C':
        celsius = valor
    elif de_tipo == 'F':
        celsius = (valor - 32) * 5/9
    elif de_tipo == 'K':
        celsius = valor - 273.15

    if a_tipo == 'C':
        return celsius
    elif a_tipo == 'F':
        return celsius * 9/5 + 32
    elif a_tipo == 'K':
        return celsius + 273.15
    
    return celsius

def calcular_factorial(n):
    """Calcula el factorial usando bucle"""
    if n < 0:
        return None
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def tabla_multiplicar(numero):
    """Genera tabla de multiplicar"""
    print(f"\nTabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def analizar_numero(num):
    """Analiza un número con condicionales"""
    print(f"\nAnálisis de {num}:")

    if num > 0:
        print("Es POSITIVO")
    elif num < 0:
        print("Es NEGATIVO")
    else:
        print("Es CERO")

    if num % 2 == 0:
        print("Es PAR")
    else:
        print("Es IMPAR")

def menu_conversor():
    """Conversor de temperatura"""
    print("\n=== CONVERSOR DE TEMPERATURA ===")
    valor = float(input("Valor: "))
    de = input("De (C/F/K): ").upper()
    a = input("A (C/F/K): ").upper()

    resultado = convertir_temperatura(valor, de, a)
    print(f"\n{valor}°{de} = {resultado:.2f}°{a}")
    historial.append(f"{valor}°{de} -> {resultado:.2f}°{a}")

def menu_agenda():
    """Sistema de agenda con diccionario"""
    while True:
        print("\n=== AGENDA DE CONTACTOS ===")
        print("1. Agregar contacto")
        print("2. Ver contactos")
        print("3. Buscar contacto")
        print("0. Salir")

        opcion = input("\nOpción: ")

        if opcion == '0':
            break
        elif opcion == '1':
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            contactos[nombre] = telefono
            print(f"Contacto '{nombre}' agregado")
        elif opcion == '2':
            if contactos:
                print("\nMis contactos:")
                for nombre, tel in contactos.items():
                    print(f" {nombre}: {tel}")
            else:
                print("No hay contactos")
        elif opcion == '3':
            nombre = input("Buscar: ")
            if nombre in contactos:
                print(f"{nombre}: {contactos[nombre]}")
            else:
                print("No encontrado")

def formulario():
    """Formulario con diferentes tipos de datos"""
    global contador

    print("\n=== FORMULARIO ===")

    nombre = input("Nombre: ")

    edad = int(input("Edad: "))

    altura = float(input("Altura (m): "))

    estudiante = input("¿Estudiante? (si/no): ").lower() == 'si'

    print("\n--- RESUMEN ---")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad} años")
    print(f"Altura: {altura} m")
    print(f"Estudiante: {estudiante}")

    if edad < 18:
        print("Eres menor de edad")
    else:
        print("Eres mayor de edad")

    contador += 1
    print(f"\nUsuarios registrados: {contador}")

def main():
    """Funcion principal"""
    print(f"\n{'='*40}")
    print(f" {nombre_sistema}")
    print(f"{'='*40}")

    while activo:
        print("\n1. Conversor de temperatura")
        print("2. Analizador de números")
        print("3. Factorial")
        print("4. Tabla de multiplicar")
        print("5. Agenda de contactos")
        print("6. Formulario")
        print("7. Ver historial")
        print("0. Salir")

        opcion = input("\nElige opción: ")

        if opcion == '0':
            print("\n¡Hasta luego!")
            break

        elif opcion == '1':
            menu_conversor()

        elif opcion == '2':
            num = float(input("\nNúmero: "))
            analizar_numero(num)

        elif opcion == '3':
            n = int(input("\nNúmero: "))
            resultado = calcular_factorial(n)
            if resultado:
                print(f"\n{n}! = {resultado}")
            else:
                print("Error: número negativo")

        elif opcion == '4':
            num = int(input("\n¿Tabla del? "))
            tabla_multiplicar(num)

        elif opcion == '5':
            menu_agenda()

        elif opcion == '6':
            formulario()

        elif opcion == '7':
            print("\n=== HISTORIAL ===")
            if historial:
                for i, item in enumerate(historial, 1):
                    print(f"{i}. {item}")
            else:
                print("Sin historial")

if __name__ == "__main__":
    main()

