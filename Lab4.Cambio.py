def monedas(V):
    denominaciones = [1,2,5,10,20,50,100,500,1000]
    n = len(denominaciones)
    cambio = []

    for i in range(n - 1, -1, -1):
        while V >= denominaciones[i]:
            V -= denominaciones[i]
            cambio.append(denominaciones[i])

    return cambio

cantidades = [2550, 8432, 263]
for cantidad in cantidades:
    print(f"Cantidad: {cantidad}")
    print(f"Cambio: {monedas(cantidad)}")
    print()