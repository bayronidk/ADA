def cont_formas(n):
    # Casos base
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2

    formas = [0] * (n + 1)

    # Arreglos para casos base
    formas[0] = 1
    formas[1] = 1
    formas[2] = 2

    # Calculamos el número de formas posibles para cada peldaño
    for i in range(3, n + 1):
        formas[i] = formas[i - 1] + formas[i - 2] + formas[i - 3]

    return formas[n]

# Ejemplo de uso
n = int(input("Ingrese el numero de peldaños: "))
print("Número de formas posibles de subir la escalera de", n, "peldaños:",cont_formas(n))
