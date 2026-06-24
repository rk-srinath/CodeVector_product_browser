let cursor = null;

async function loadProducts(reset=false){

    if(reset){
        cursor = null;
        document.getElementById("products").innerHTML = "";
    }

    let category =
        document.getElementById("category").value;

    let url =
        "http://127.0.0.1:8000/products?limit=20";

    if(category){
        url += "&category=" + category;
    }

    if(cursor){
        url += "&cursor=" + cursor;
    }

    let response = await fetch(url);

    let products = await response.json();

    let container =
        document.getElementById("products");

    products.forEach(product => {

        container.innerHTML += `
            <div class="card">
                <h3>${product.name}</h3>
                <p>Category: ${product.category}</p>
                <p>Price: ₹${product.price}</p>
                <p>ID: ${product.id}</p>
            </div>
        `;
    });

    if(products.length > 0){
        cursor =
            products[products.length - 1].id;
    }
}