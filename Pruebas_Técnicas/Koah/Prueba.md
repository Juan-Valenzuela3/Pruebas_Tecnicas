Prueba Técnica Junior – PERMODA (Full-Stack .NET + React)
Objetivo: validar fundamentos web/REST, CRUD simple en .NET 8 + EF Core,
consumo desde React, principios SOLID.
1. Diferencia entre GET y POST.
2. Códigos HTTP para: creado, no encontrado, error del cliente.
3. ¿Qué es CORS y cuándo aparece?
4. ¿Qué es una migración en EF Core y cuándo crearías una nueva?
6. DTO vs Entidad: ¿por qué no exponer entidades?
7. ¿Qué es inyección de dependencias (DI) y por qué se usa en ASP.NET Core?
8. Props vs State en React (caso simple).
9. Una buena práctica de commits.
10. Que son los principios SOLID, da ejemplos de cada uno
11. Normalización básica: ¿cuándo evitarías la duplicación de datos?
12. ¿Qué es una FK y por qué es importante?

Práctica (desarrollo de un Catálogo de Productos)
Modelo Producto
 id:int,
 nombre:string*,
 sku:string* (único),
 precio:decimal&gt;=0,
 stock:int&gt;=0,
 categoria:string (*requeridos)

Back-end
 Endpoints:
 GET /api/products (lista)
 GET /api/products/{id}
 POST /api/products (valida campos y sku único)
 PUT /api/products/{id}

- Swagger habilitado.
- Migración inicial
- Cargue de 5 productos.

Front-end
 Página con DataGrid consumiendo GET /api/products.
 Búsqueda por nombre/sku.
 Formulario para crear producto (valida y refresca grilla; mensaje simple
éxito/error).

Bonus opcional (elige 1):
 Auth/JWT
 Node.js: script que convierte CSV→JSON normalizado.
 Python: script que detecte skus potencialmente duplicados.