// Primeras 4 preguntas técnicas

// 1. ¿Qué es una clase en Java y cómo se define?: Una clase es un modelo o plantilla que define las propiedades de objetos. Contiene métodos y atributos.

public class Empleado {
    String nombre;
    double salario;

    public Empleado(String nombre, double salario) {
        this.nombre = nombre;
        this.salario = salario;
    }

    public void aumentarSalario(double porcentaje) {
        this.salario += this.salario * (porcentaje / 100);
    }
}

// 2. ¿Qué es un método en Java y cómo se define?: un método es una función definida dentro de una clase para ejecutar acciones específicas.

public int sumar(int a, int b) {
    return a + b;
}

// 3. ¿Cuál es la diferencia entre una clase y una interfaz en Java?: Una clase puede tener implementación completa, mientras que una interfaz solo define métodos sin implementación. Una clase puede implementar múltiples interfaces.

public interface Vehiculo {
    void conducir();
    void frenar();
}

public class Carro implements Vehiculo {
    public void conducir() {
        System.out.println("El carro está en movimiento.");
    }
}

// 4. Explica qué es la herencia en Java y cómo se implementa: La herencia permite que una clase (subclase) herede propiedades y métodos de otra clase (superclase). Se implementa usando la palabra clave "extends".

public class Animal {
    void comer() {
        System.out.println("El animal está comiendo.");
    }
}

public class Perro extends Animal {
    void ladrar() {
        System.out.println("El perro está ladrando.");
    }
}