def minimo_monedas(V):
    monedas = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    n = len(monedas)
    resultado = []

    # Inicializar el resultado
    for _ in range(n):
        resultado.append(0)

    # Empezar desde la cantidad más grande de monedas
    i = n - 1
    while i >= 0:
        # Encontrar el número de monedas de la denominación actual
        resultado[i] = V // monedas[i]
        V = V % monedas[i]
        i -= 1

    # Imprimir el resultado
    for i in range(n):
        if resultado[i] != 0:
            print("Monedas de", monedas[i], ":", resultado[i])

# Solicitar al usuario que ingrese el valor V
V = int(input("Ingrese el valor V: "))

# Calcular el número mínimo de monedas
print("\nNúmero mínimo de monedas para V =", V, ":")
minimo_monedas(V)
