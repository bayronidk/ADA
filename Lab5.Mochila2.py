def mochila_fraccionaria(items, capacidad):
    for item in items:
        item.append(item[0] / item[1])

    items.sort(key=lambda x: x[2], reverse=True)

    resultado = 0
    peso_total = capacidad

    for item in items:
        if item[1] <= peso_total:
            resultado += item[0]
            peso_total -= item[1]
        else:
            fraccion = peso_total / item[1]
            resultado += item[0] * fraccion
            peso_total = 0
            break

    return resultado

items = [[60, 20], [100, 20], [120, 30],[140, 20]]
capacidad = 50
resultado = mochila_fraccionaria(items, capacidad)
print("El maximo obtenido es:", resultado)
