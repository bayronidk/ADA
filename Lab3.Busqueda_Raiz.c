#include <stdio.h>

int raiz_cuadrada_busqueda_binaria(int X) {
    if (X == 0 || X == 1)
        return X;
    
    int l = 0;
    int r = X / 2;
    int ans;

    while (l <= r) {
        int mitad = (l + r) / 2;
        int cuadrado_mitad = mitad * mitad;

        if (cuadrado_mitad == X)
            return mitad;
        else if (cuadrado_mitad < X) {
            l = mitad + 1;
            ans = mitad;
        }
        else
            r = mitad - 1;
    }

    return ans;
}

int main() {
    int numero;
    printf("Ingrese el número para encontrar su raíz cuadrada: ");
    scanf("%d", &numero);
    printf("La raíz cuadrada de %d es: %d\n", numero, raiz_cuadrada_busqueda_binaria(numero));
    return 0;
}
