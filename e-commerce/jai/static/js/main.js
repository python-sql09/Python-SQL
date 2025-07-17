console.log("✅ main.js loaded");

let cart = [];

function updateCartCount() {
  const count = cart.reduce((sum, item) => sum + item.quantity, 0);
  document.getElementById("cartCount").textContent = count;
}

function addToCart(productId, title, price) {
  console.log("Adding to cart:", productId, title);
  const item = cart.find(p => p.id === productId);
  if (item) {
    item.quantity += 1;
  } else {
    cart.push({ id: productId, title, price, quantity: 1 });
  }
  updateCartCount();
}

function showCart() {
  const modal = document.getElementById("cartModal");
  const cartItems = document.getElementById("cartItems");
  const cartTotal = document.getElementById("cartTotal");

  cartItems.innerHTML = "";
  let total = 0;

  if (cart.length === 0) {
    cartItems.innerHTML = "<p>Your cart is empty.</p>";
  } else {
    cart.forEach(item => {
      const row = document.createElement("div");
      row.innerHTML = `
        <p>${item.title} - $${item.price.toFixed(2)} × ${item.quantity}
        <button onclick="removeFromCart(${item.id})">Remove</button></p>
      `;
      cartItems.appendChild(row);
      total += item.price * item.quantity;
    });
  }

  cartTotal.textContent = total.toFixed(2);
  modal.style.display = "flex";
}

function closeCart() {
  document.getElementById("cartModal").style.display = "none";
}

function removeFromCart(productId) {
  cart = cart.filter(item => item.id !== productId);
  updateCartCount();
  showCart();
}

function checkout() {
  alert("Thank you for your purchase!");
  cart = [];
  updateCartCount();
  closeCart();
}

document.addEventListener("DOMContentLoaded", () => {
  const productList = document.getElementById("product-list");

  fetch("/api/products")
    .then(res => res.json())
    .then(products => {
      console.log("✅ Products loaded:", products);

      products.forEach(product => {
        const div = document.createElement("div");
        div.classList.add("product-card");
        div.innerHTML = `
          <h3>${product.title}</h3>
          <p>Price: $${product.price.toFixed(2)}</p>
          <button onclick="addToCart(${product.id}, \`${product.title}\`, ${product.price})">Add to Cart</button>
        `;
        productList.appendChild(div);
      });
    })
    .catch(err => {
      console.error("❌ Failed to fetch products:", err);
      productList.innerHTML = "<p>Failed to load products.</p>";
    });
});