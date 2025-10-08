
import React, { useEffect, useState} from "react";

function ProductList() {
    const [products, setProducts] = useState([]);
    const [search, setSearch] = useState("");


    useEffect(() => {
        fetch(`/api/products?search=${search}`)
            .then((response) => response.json())
            .then(setProducts);
    }, [search]);

    return (
        <div>
            <input 
                placeholder="Buscar por nombre o SKU"
                value={search}
                onChange={(e) => setSearch(e.target.value)}
            />
            <table>
                <thead>
                    <tr>
                        <th>Nombre</th>
                        <th>SKU</th>
                        <th>Precio</th>
                        <th>Stock</th>
                        <th>Categoría</th>
                    </tr>
                </thead>
                <tbody>
                    {products.map((product) => (
                        <tr key={product.sku}>
                            <td>{product.name}</td>
                            <td>{product.sku}</td>
                            <td>{product.price}</td>
                            <td>{product.stock}</td>
                            <td>{product.category}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default ProductList;