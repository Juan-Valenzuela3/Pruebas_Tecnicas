# 1 Una variable es un espacio en memoria el cual puede almacenar diferentes tipos de datos. Se declara de la siguiente forma:

nombre_variable = "Valor de la variable"

# Una función es un programa que puede ejecutar varias tareas dentro de sí. Recibe argumentos y parámetros, se declara de la siguiente forma:

def sumar (numero1, numero2):
    return numero1 + numero2

resultado = sumar(5, 10)
print(resultado)

# 3 Una lista y una tupla son estructuras de datos que almacen valores. La diferencia es que las listas son mutables, mientras que las tuplas inmutables. Usaría una lista cuando sé que los valores cambiarán de forma constante y una tupla cuando los valores deben permanecere constantes.
## Las listas permiten métodos como append, remove, pop, etc., mientras que las tuplas no permiten modificar sus elementos después de su creación.

lista = [1, 2, 3]
tupla = (1, 2, 3)

# Ejercicio 1: Crea una función llamada filtrar_pares que reciba una lista de números y retorne una nueva lista solo con los números pares.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filtrar_pares(numeros):
    return [numero for numero in numeros if numero % 2 == 0]

print(filtrar_pares(numeros))

# Los decoradores son extensiones de funciones, se utilizan para agregar funcionalidades a una función sin modificar la existente.

def decorador(funcion):
    def nueva_funcion(*args, **kwargs):
        print("Antes de la función")
        resultado = funcion(*args, **kwargs)
        print("Después de la función")
        return resultado
    return nueva_funcion

@decorador
def saludar(nombre):
    print(f"Hola, {nombre}!")

print(saludar("Juan"))

## Ejercicio 2 POO: Crea una clase llamada Empleado que tenga los atributos nombre y salario. Agrega un método llamado aumentar_salario que reciba un porcentaje y aumente el salario del empleado en ese porcentaje. Demuestra su uso crando un empleado y aumentando su salario en un 10%.

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def aumentar_salario(self, porcentaje):
        self.salario += self.salario * (porcentaje / 100)
        return self.salario

empleado = Empleado("Juan", 1000)
print(empleado.aumentar_salario(10))

## Ejercicio 3 PF: Crea una función llamada cuadrados que recibe una lista de números y retorne una nueva lista con el cuadrado de cada número usando la función map.

def cuadrados(numeros):
    return list(map(lambda x: x**2, numeros))

print(cuadrados([1, 2, 3, 4, 5]))

## Ejercicio 4 PR: Simula un flujo de datos usando generadores en Python. Crea una función generadora llamada contador que reciba un número n y produzca los números del 1 al n, uno por uno. Demuestra cómo consumir el generador usando un ciclo for.

def contador(n):
    for i in range(1, n + 1):
        yield i

gen = contador(5)

print(next(gen))  # Salida esperada: 1
print(next(gen))  # Salida esperada: 2
print(next(gen))  # Salida esperada: 3
print(next(gen))  # Salida esperada: 4
print(next(gen))  # Salida esperada: 5
print(next(gen))  # Esto lanzará una excepción StopIteration ya que el generador