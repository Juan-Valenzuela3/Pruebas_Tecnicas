# Prueba Técnica Permoda

1. Get es una solicitud http usada para solicitar información o datos de una API o endpoint específico. POST, se encarga de enviar información - datos a este endpoint, API o backend.

2. Para creado se utiliza el código 201, para no encontrado se utiliza el 404, para error del cliente se utiliza el 400.

3. Cors es una medida de seguridad utilizada en los navegadores web para una conexión segura con un servidor externo. Si tengo un servicio como un backend desplegado en la nube, si quiero conectarlo a un frontend en la web desplegado , como por ejemplo Vercel, se necesita configurar los CORS para indicarle al servicio la dirección del frontend que debe usarse. Esto debe configurarse tanto en el backend como en el frontend y permitir una conección segura por https.

4. Es un mecanismo que permite actualizar y sincronizar el esquema de la base de datos con los cambios realizados en el modelo de datos. Crearía una migración cadda vez que modifique el modelo de los datos.

5. Exponer las entidades implica que el servicio recibirá toda la información de la base de datos relacionada con esta entidad, lo que genera problemas de rendimiento y lentitud. En cambio, usar un DTO nos permite indicar qué datos son los que requiero, de esta manera, solo recibiré los datos solicitados. Esto solucionará los problemas de rendimiendo o bugs que se puedan presentar.

6. La inyección de dependencias es un patrón de diseño que proporciona los objetos o servicios que una clase necesita. Esto facilita la reutilización, el mantenimiento y las pruebas del código. En ASP.NET se usa para gestionar la creación y ciclo de vida de los servicios, esto permite desacoplar las clases y mejorar la modularidad.

7. En React los props son propiedades que se pasan desde un componente padre a un componente hijo, Son de solo lectura. El State indica el estado interno de un componente, este puede cambiar a lo largo del ciclo de vida del componente y afectar su renderizado.

## Caso simple
---
// Componente padre
functions App() {
    return <Saludo nombre="Farid" />
}

// Componente hijo, se pasa la propiedad nombre del componente padre al hijo.
function Saludo(props) {
    return <h1>Hola, {props.nombre}!</h1>
}
---

8. Buenas prácticas en commits involucran  que sean pequeños y enfocados en una sola tarea. Deben tener mensajes claros y descriptivos. Debe responder el por qué se hace el commit y no el cómo.

9. Los principios solid son cinco buenas prácticas para el diseño de software que ayudan a crear sistemas más mantenibles, escalables y comprensibles.

## S - Responsabilidad única: Una clase debe tener una sola responsabilidad.
---
class ReportGeneratos:
    def generate(self):
    # Genera solo el reporte

class ReportPrinter:
    def print(self):
    # Imprime el reporte
---
## O - Principio de abierto y cerrado: Las clases deben estar abiertas para extensión, pero cerradas para modificación.
--- 
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        pass

class Square(Shape):
    def area(self):
        pass
---
## L - Principio de sustitución: Las classes derivadas deben poder sustituir a sus clases base sin alterar el  funcionamiento del programa.
---
def print_area(shape: Shape):
    print(shape.area())
    # Circle y Square pueden usarse sin prblemas en print_area
---
## I - Principio de segregación de interfaces: Los clientes no deben verse obligados a depender de interfaces que no se usan.
---
class Printable:
    def print(self):
        pass

class Scannable:
    def scan(self):
        pass
   # Una clase puede implementar solo la interfaz que necesita.
---
## D - Principio de inversión de Dependencias: Las clases deben depender de abstracciones y no de implementaciones concretas.
---
class Database:
    def save(self, data):
        pass

class Service:
    def __init__(self, db: Database):
        self.db = db
---

10. Evitaría la duplicación de datos al guardar un usuario, por ejemplo, en la base de datos. Pues en la entidad solo debe existir un único usuario con un mismo identificador, que en este caso podría ser el correo o un ID. De esta manera aseguramos que exista solo un usuario y solo este se pueda registrar o iniciar sesión en la DB.

11. Un FK clave foránea, un campo específico de una DB que crea relaciones con la clave primaria de otra tabla. Es importante porque garantiza la integridad referencial, asegurando que los datos relacionados entre las tablas sean consistentess y válidos.

# Práctica - Desarrollo de un catálogo de productos

