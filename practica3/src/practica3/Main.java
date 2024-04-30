/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package practica3;

/**
 *
 * @author laort
 */
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Casos base
        System.out.println("Ingrese un numero para calcular su raiz cuadrada:");
        int x = scanner.nextInt();
        if (x == 0 || x == 1) {
            System.out.println("Caso base: " + x);
        } else {
            System.out.println("La raiz es: " + Math.sqrt(x));
        }

        // Variables para almacenar límites
        System.out.println("\nLimites:");
        int l = 0;
        int r = x / 2;
        System.out.println("l = " + l);
        System.out.println("r = " + r);

        // Bucle de búsqueda
        System.out.println("\nBucle de busqueda:");
        while (l <= r) {
            int mid = (l + r) / 2;
            System.out.println("l = " + l + ", r = " + r + ", mid = " + mid);
            if (mid * mid == x) {
                System.out.println("Encontrado: " + mid);
                break;
            } else if (mid * mid < x) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }

        // Actualización de límites
        System.out.println("\nActualizacion de limites:");
        l = 0;
        r = x / 2;
        int ans = 0;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (mid * mid == x) {
                ans = mid;
                break;
            } else if (mid * mid < x) {
                l = mid + 1;
                ans = mid;
            } else {
                r = mid - 1;
            }
        }

        System.out.println("Resultado: " + ans);

        scanner.close();
    }
}

    