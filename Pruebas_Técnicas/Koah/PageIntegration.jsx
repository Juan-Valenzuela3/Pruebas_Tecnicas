import React, { useState }from "react";
import ProductForm from "./ProductForm";
import ProductList from "./ProductList";

function PageIntegration() {
    const [refresh, setRefresh] = useState(false);
    
    return(
        <div>
            <ProductForm onCreate={() => setRefresh(!refresh)} />
            <ProductList key={refresh} />
        
        </div>
    );
};

export default PageIntegration;