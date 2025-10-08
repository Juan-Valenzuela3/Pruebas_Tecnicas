package Practicas.Wallib;

// Una clase en Java es la estructura básica que define un objeto. Contiene métodos y atributos.

public class Ejercicio {
    // Atributos son las características o propiedades de un objeto
    protected  String nombre;
    protected  int edad;
    // Un método es una acción que puede ejecutar un objeto de la clase asociada
    public static void main(String[] args) {
        
        System.out.println("Hola, Mundo!");
    }

}

// La herencia es un mecanismo por el cual puedo extender las propiedades y métodos de una clase padre a una clase hija
public class Persona extends Ejercicio {
    private String direccion;
    private String telefono;

    public void mostrarDatos() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad);
        System.out.println("Dirección: " + direccion);
        System.out.println("Teléfono: " + telefono);
    }
}

// Ejercicio 1
class Utilidades {
    public int sumarLista(int[] lista) {
        int suma = 0;
        for (int num : lista) {
            suma += num;
        }
        return suma;
    }
}

// Una interfaz en Java es una estructura que define un contrato con otras clases y puede implemtnar métodos o atributos
interface Calculadora {
    int sumar(int a, int b);
}

// Ejercicio 2
class Persona2 {
    private String nombre;
    private int edad;

    // Constructor para inicializar los atributos
    public Persona2(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    public String imprimirSaludo() {
        return "Hola, mi nombre es " + nombre + " y tengo " + edad + " años.";
    }
}