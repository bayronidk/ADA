def policeThief(arr, n, k):
    i = 0
    l = 0
    r = 0
    res = 0
    thi = []
    pol = []
    
    # Almacena índices en listas
    while i < n:
        if arr[i] == 'P':
            pol.append(i)
        elif arr[i] == 'T':
            thi.append(i)
        i += 1
    
    # Rastrea los índices mínimos actuales de ladrones (thief) y policías (police)
    while l < len(thi) and r < len(pol):
        # Puede ser capturado
        if abs(thi[l] - pol[r]) <= k:
            res += 1
            l += 1
            r += 1
        # Incrementa el índice mínimo
        elif thi[l] < pol[r]:
            l += 1
        else:
            r += 1
    
    return res

# Programa principal
if __name__ == '__main__':
    arr1 = ['T', 'P', 'T', 'P', 'T','T','T','P','T','T']
    k = 3
    n = len(arr1)
    print("Maximum thieves caught:", policeThief(arr1, n, k))
    