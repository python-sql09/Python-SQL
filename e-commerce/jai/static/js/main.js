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
        <img src="${product.image}" alt="${product.title}" class="product-image">
        <h3>${product.emoji || "🛍️"} ${product.title}</h3>
        <p>Price: $${product.price.toFixed(2)}</p>
        <button onclick="addToCart(${product.id}, '${product.title}', ${product.price})">Add to Cart</button>
`       ;
        productList.appendChild(div);
      });
    })
    .catch(err => {
      console.error("❌ Failed to fetch products:", err);
      productList.innerHTML = "<p>Failed to load products.</p>";
    });
});

// 🌗 Dark Mode Toggle
const themeToggle = document.getElementById("themeToggle");
themeToggle.addEventListener("change", () => {
  document.body.classList.toggle("dark-mode");
  localStorage.setItem("theme", themeToggle.checked ? "dark" : "light");
});

// Load theme on page load
if (localStorage.getItem("theme") === "dark") {
  document.body.classList.add("dark-mode");
  themeToggle.checked = true;
}

function loadCategory(category) {
  fetch("/api/products")
    .then((res) => res.json())
    .then((products) => {
      const filtered = products.filter(p => p.category === category);
      const productList = document.getElementById("product-list");
      productList.innerHTML = "";
      filtered.forEach((product) => {
        const div = document.createElement("div");
        div.classList.add("product-card");
        div.innerHTML = `
          <img src="${product.image}" class="product-image" alt="${product.title}">
          <h3>${product.title}</h3>
          <p>Price: $${product.price}</p>
          <button onclick="addToCart(${product.id}, '${product.title}', ${product.price})">Add to Cart</button>
        `;
        productList.appendChild(div);
      });
    });
}

function searchProducts() {
  const term = document.getElementById("searchInput").value.toLowerCase();
  fetch("/api/products")
    .then((res) => res.json())
    .then((products) => {
      const filtered = products.filter(p => p.title.toLowerCase().includes(term));
      const productList = document.getElementById("product-list");
      productList.innerHTML = "";
      filtered.forEach(product => {
        const div = document.createElement("div");
        div.classList.add("product-card");
        div.innerHTML = `
          <img src="${product.image}" class="product-image" alt="${product.title}">
          <h3>${product.title}</h3>
          <p>Price: $${product.price}</p>
          <button onclick="addToCart(${product.id}, '${product.title}', ${product.price})">Add to Cart</button>
        `;
        productList.appendChild(div);
      });
    });
}

function showLogin() {
  const modal = document.getElementById("authModal");
  document.getElementById("loginForm").style.display = "block";
  document.getElementById("signupForm").style.display = "none";
  modal.style.display = "flex";
}

function showSignup() {
  const modal = document.getElementById("authModal");
  document.getElementById("loginForm").style.display = "none";
  document.getElementById("signupForm").style.display = "block";
  modal.style.display = "flex";
}

function closeAuth() {
  document.getElementById("authModal").style.display = "none";
}

function showCart() {
  document.getElementById("cartModal").style.display = "flex";
}

function closeCart() {
  document.getElementById("cartModal").style.display = "none";
}

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const show = "{{ show_modal }}";
    if (show === "login") showLogin();
    else if (show === "signup") showSignup();
  });
</script>