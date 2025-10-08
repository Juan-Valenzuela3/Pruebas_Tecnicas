# ----------------- NIVEL BÁSICO -----------------
# Ejercicio 1
numeros = [1, 2, 3, 4, 5]

def suma_lista(numeros):
    return sum(numeros)

# Ejercicio 2

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    
persona = Persona("Juan", 27)

# Ejercicio 3
numeros = [1, 2, 3, 4, 5, 6]
def filtrar_pares(numeros):
    return [num for num in numeros if num % 2 == 0]

# Ejercicio 4
def invertir_cadena(cadena):
    return cadena[::-1]

# ----------------- NIVEL INTERMEDIO -----------------

# Question 1: Una función lambda es una función anónonima, es decir, una función sin nombre que se define en una sola línea. Se utiliza para operaciones simples y rápidas, especialmente como argumento en funciones como map, filter y sorted. Es como una función flecha (arrow functions) en JavaScript.
suma = lambda x, y: x + y

# Ejercicio 1: Crea una función llamda duplicar_pares que reciba una lista de números y retorne una nueva lista ocn lso números pares duplicados y los impares sin cambios.

numeros = [1, 2, 3, 4, 5, 6]

def duplicar_pares(numeros):
    return [num * 2 if num % 2 == 0 else num for num in numeros]


# Question 2: Una lista es una colección ordenada y mutable de elementos. Permite duplicados y puedes acceder a los elementos por índice. Un conjunto set es una colección no ordenada y mutable de elementos únicos (no permite duplicados). No puedess acceder a los elementos por índice.
    # Cuándo usar cada uno? Una lista cuando necesitas mantener el orden de los elementos o permitir duplicados. Un set cuando necesitas eliminar duplicados o realizar operaciones de conjuntos como unión, intersección y diferencia.

# Ejercicio 2
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            return "Fondos insuficientes"

cuenta = CuentaBancaria("Ana", 1000)

# Ejercicio 3