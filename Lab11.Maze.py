def contar_caminos(laberinto):
    filas = len(laberinto)
    columnas = len(laberinto[0])
    
    # Si el punto de inicio o el de destino es un obstáculo, no hay rutas posibles
    if laberinto[0][0] == 1 or laberinto[filas-1][columnas-1] == 1:
        return 0
    
    # Crear una matriz dp del mismo tamaño que el laberinto
    dp = [[0]*columnas for _ in range(filas)]
    
    # Inicializar el punto de partida
    dp[0][0] = 1
    
    # Rellenar la matriz dp
    for i in range(filas):
        for j in range(columnas):
            # Si la celda es un obstáculo, continuar
            if laberinto[i][j] == 1:
                continue
            # Si podemos movernos hacia abajo
            if i > 0 and laberinto[i-1][j] != 1:
                dp[i][j] += dp[i-1][j]
            # Si podemos movernos hacia la derecha
            if j > 0 and laberinto[i][j-1] != 1:
                dp[i][j] += dp[i][j-1]
    
    # La cantidad de rutas posibles para llegar a (filas, columnas) está en dp[filas-1][columnas-1]
    return dp[filas-1][columnas-1]

# Ejemplo de uso
laberinto = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 0, 1, 0]
]

print("Hay un total de:", contar_caminos(laberinto), "caminos")

