import random

# Definir la cantidad de bloques de memoria y procesos
num_bloques = 5
num_procesos = 5

# Generar tamaños aleatorios para los bloques de memoria y procesos
tamanos_bloques = [random.randint(100, 600) for _ in range(num_bloques)]
tamanos_procesos = [random.randint(100, 500) for _ in range(num_procesos)]

# Función para asignar memoria utilizando el algoritmo best-fit
def asignar_memoria_best_fit(tamanos_bloques, tamanos_procesos):
    asignaciones = {}  # Diccionario para almacenar las asignaciones de memoria
    espacio_disponible = tamanos_bloques.copy()  # Copiar los tamaños de los bloques de memoria

    for proceso in sorted(tamanos_procesos):
        mejor_ajuste = float('inf')  # Inicializar con un valor infinito
        bloque_seleccionado = None
        for i, bloque in enumerate(espacio_disponible):
            if bloque >= proceso and bloque - proceso < mejor_ajuste:
                mejor_ajuste = bloque - proceso
                bloque_seleccionado = i
        if bloque_seleccionado is not None:
            asignaciones[proceso] = bloque_seleccionado
            espacio_disponible[bloque_seleccionado] -= proceso
        else:
            asignaciones[proceso] = None

    return asignaciones, espacio_disponible

# Ejecutar la función y obtener las asignaciones
asignaciones, espacio_disponible = asignar_memoria_best_fit(tamanos_bloques, tamanos_procesos)

# Imprimir tamaños de bloques y procesos
print("Tamaños de bloques de memoria:")
for i, bloque in enumerate(tamanos_bloques):
    print(f"Bloque {i + 1}: {bloque} KB")

print("\nTamaños de procesos:")
for i, proceso in enumerate(tamanos_procesos):
    print(f"Proceso {i + 1}: {proceso} KB")

# Imprimir resultados de asignaciones y espacio disponible
print("\nAsignaciones de memoria:")
for proceso, bloque in asignaciones.items():
    if bloque is not None:
        print(f"Proceso de tamaño {proceso} KB asignado al bloque {bloque + 1}")
    else:
        print(f"Proceso de tamaño {proceso} KB no pudo ser asignado a ningún bloque")

print("\nEspacio disponible en cada bloque después de asignar procesos:")
for i, espacio in enumerate(espacio_disponible):
    print(f"Bloque {i + 1}: {espacio} KB")