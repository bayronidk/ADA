def raiz_cuadrada_busqueda_binaria(X):
    if X == 0 or X == 1:
        return X
    
    l = 0
    r = X // 2

    while l <= r:
        mitad = (l + r) // 2
        cuadrado_mitad = mitad * mitad

        if cuadrado_mitad == X:
            return mitad
        elif cuadrado_mitad < X:
            l = mitad + 1
            ans = mitad
        else:
            r = mitad - 1

    return ans

numero = int(input("Ingrese el numero a buscar su raiz cuadrada: "))
print(raiz_cuadrada_busqueda_binaria(numero))
