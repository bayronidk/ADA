class Proceso:
    def __init__(self, nombre, tamaño):
        self.nombre = nombre
        self.tamaño = tamaño

class Memoria:
    def __init__(self, tamaño_total):
        self.tamaño_total = tamaño_total
        self.espacios_libres = [(0, tamaño_total)]  # (inicio, tamaño)

    def asignar_proceso(self, proceso):
        for i, (inicio, tamaño) in enumerate(self.espacios_libres):
            if tamaño >= proceso.tamaño:
                self.espacios_libres.pop(i)
                if tamaño > proceso.tamaño:
                    self.espacios_libres.insert(i, (inicio + proceso.tamaño, tamaño - proceso.tamaño))
                print(f"Proceso {proceso.nombre} (Tamaño: {proceso.tamaño} KB) asignado en la dirección de memoria {inicio} - {inicio + proceso.tamaño - 1}")
                return True
        print(f"No hay suficiente espacio para el proceso {proceso.nombre} (Tamaño: {proceso.tamaño} KB)")
        return False

def main():
    tamaño_memoria = 1024  # Tamaño total de la memoria en KB
    memoria = Memoria(tamaño_memoria)

    tamaños_procesos = [300, 6000, 300, 100]  # Tamaños de los procesos en KB
    procesos = [Proceso(f"Proceso {i+1}", tamaño) for i, tamaño in enumerate(tamaños_procesos)]

    print("Tamaño de la memoria:", tamaño_memoria, "KB")
    print("Tamaño de los procesos:")
    for proceso in procesos:
        print(f"{proceso.nombre}: {proceso.tamaño} KB")

    print("\nAsignacion de procesos en la memoria:")
    for proceso in procesos:
        memoria.asignar_proceso(proceso)

if __name__ == "__main__":
    main()