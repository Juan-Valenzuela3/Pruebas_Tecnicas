import React, { useState } from "react";

function ProductForm({onCreate}) {
    const [form, setForm] = useState({ nombre: '', sku: '', precio: 0, stock: 0, categoria: ''});
    const [msg, setMsg] = useState('');

    const handleChange = (e) => {
        const { name, value } = e.target;
        setForm((prevForm) => ({ ...prevForm, [name]: value }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        fetch('/api/products', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(form),
        })
        .then((response) => {
            if (response.ok) {
                setMsg('Producto creado exitosamente');
                onCreate();
            } else {
                response.text().then(text => setMsg(`Error: ${text}`));
            }
        })
    }

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" name="nombre" placeholder="Nombre" value={form.nombre} required onChange={handleChange} />
            <input type="text" name="sku" placeholder="SKU" value={form.sku} required onChange={handleChange} />
            <input type="number" name="precio" placeholder="Precio" value={form.precio} required onChange={handleChange} />
            <input type="number" name="stock" placeholder="Stock" value={form.stock} required onChange={handleChange} />
            <input type="text" name="categoria" placeholder="Categoría" value={form.categoria} required onChange={handleChange} />
            <button type="submit">Crear Producto</button>
            {msg && <p>{msg}</p>}
        </form>
    )
};

export default ProductForm;