def cont_formas(n, memo={}):
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    elif n == 2:
        return 2
    formas = cont_formas(n - 1, memo) + cont_formas(n - 2, memo) + cont_formas(n - 3, memo)
    memo[n] = formas
    return formas

n = int(input("Ingrese el número de peldaños: "))
print("Número de formas posibles de subir la escalera de", n, "peldaños:", cont_formas(n))
