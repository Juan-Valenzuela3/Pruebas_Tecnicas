import React, { useState }from "react";
import ProductForm from "../components/ProductForm";
import ProductList from "../components/ProductList";

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