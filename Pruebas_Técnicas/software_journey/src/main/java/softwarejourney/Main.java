package softwarejourney;

import java.util.Scanner;

public class Main {
     public static void main(String[] args) {
        // 1. Leer el tamaño de la matriz (n)
        Scanner sc = new Scanner(System.in);
        System.out.println("Introducir el valor de n:");
        int n = sc.nextInt();

        int numero = 1; // Contador global de números ascendentes
        int numeroD = n * (n + 3) / 2; // Primer número descendente (fila 0)
        
        // Generar matriz por filas
        for (int fila = 0; fila < n; fila++) {
            // Imprimir guiones de indentación
            for (int dash = 0; dash < fila; dash++) {
                System.out.print("--");
            }
            
            // Números ascendentes: desde 'numero' hasta que se completen (n - fila) números
            for (int col = 0; col < (n - fila); col++) {
                System.out.print(numero);
                if (col < (n - fila - 1)) {
                    System.out.print("*");
                }
                numero++;
            }
            
            // Imprimir asterisco de separación antes de los descendentes
            System.out.print("*");
            
            // Números descendentes: desde numeroD y descendiendo (n - fila) números
            int inicio = numeroD;
            for (int col = 0; col < (n - fila); col++) {
                System.out.print(inicio);
                if (col < (n - fila - 1)) {
                    System.out.print("*");
                }
                inicio--;
            }
            
            // Actualizar numeroD para la siguiente fila: el incremento disminuye en cada fila
            numeroD += (n - fila - 1);
            
            System.out.println(); // Nueva línea después de cada fila
        }
        
        sc.close();
    }
}