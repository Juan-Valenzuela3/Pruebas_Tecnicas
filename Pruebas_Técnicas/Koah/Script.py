products = [
    {"name": "Laptop", "price": 999.99, "stock": 10, "SKU": "LP1001"},
    {"name": "Smartphone", "price": 499.99, "stock": 20, "SKU": "SP2001"},
    {"name": "Tablet", "price": 299.99, "stock": 15, "SKU": "TB3001"},
    {"name": "Headphones", "price": 89.99, "stock": 50, "SKU": "HP4001"},
    {"name": "Smartwatch", "price": 199.99, "stock": 25, "SKU": "SW5001"},
]

def detectar_skus_duplicados(productos):
    skus = [p["SKU"] for p in productos]
    duplicados = set([sku for sku in skus if skus.count(sku) > 1])
    return duplicados

if __name__ == "__main__":
    duplicados = detectar_skus_duplicados(products)
    if duplicados:
        print("SKUs duplicados encontrados:", duplicados)
    else:
        print("No se encontraron SKUs duplicados.")