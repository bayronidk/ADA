from math import sqrt

#1 Casos base
print("Ingrese un número para calcular su raíz cuadrada:")
x = int(input())
if x == 0 or x == 1:
    print("Caso base: ", x) 
else: 
    print("La raíz es:", sqrt(x))

#2 Variables para almacenar límites
print("\nLímites:")
l = 0
r = x // 2
print("l =", l)
print("r =", r)

#3 Bucle de búsqueda
print("\nBucle de búsqueda:")
while l <= r:
    mid = (l + r) // 2
    print("l =", l, ", r =", r, ", mid =", mid)
    if mid * mid == x:
        print("Encontrado:", mid)
        break
    elif mid * mid < x:
        l = mid + 1
    else:
        r = mid - 1

# 4 y 5 Actualización de límites
print("\nActualización de límites:")
l = 0
r = x // 2
ans = 0
while l <= r:
    mid = (l + r) // 2
    if mid * mid == x:
        ans = mid
        break
    elif mid * mid < x:
        l = mid + 1
        ans = mid
    else:
        r = mid - 1

print("r:",r ,"l:", l,"ans:", ans,"mid:", mid)


print("Resultado:", ans)
