matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México":["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

print("=== CAMBIOS ===\n")

matriz[1][0] = 6
print(f"Matriz actualizada: {matriz}")

cantantes[0]["nombre"] = "Enrique Martin Morales"
print(f"Primer cantante actualizado: {cantantes[0]}")

ciudades["México"][2] = "Monterrey"
print(f"Ciudades de México actualizadas: {ciudades['México']}")

coordenadas[0]["latitud"] = 9.9355431
print(f"Coordenadas actualizadas: {coordenadas[0]}")

print("\n=== RECORRIDO DE CANTANTES ===\n")

for cantante in cantantes:
    print(f"nombre - {cantante['nombre']}, pais - {cantante['pais']}")

print("\n=== VALORES ESPECÍFICOS ===\n")

print("Nombres:")
for cantante in cantantes:
    print(cantante["nombre"])

print("\nPaíses:")
for cantante in cantantes:
    print(cantante["pais"])

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

print("\n=== RECORRIDO DE COSTA RICA ===\n")

for clave, lista in costa_rica.items():
    print(f"{len(lista)} {clave.upper()}")
    for elemento in lista:
        print(elemento)
    print()