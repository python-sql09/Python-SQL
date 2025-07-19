console.log("✅ Enhanced main.js loaded");

// Application state
let cart = [];
let products = [];

// Utility functions
function formatPrice(price) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(price);
}

function showNotification(message, type = 'success') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 1.5rem;
        background: ${type === 'success' ? '#48bb78' : '#f56565'};
        color: white;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        z-index: 3000;
        animation: slideInRight 0.3s ease;
    `;
    
    document.body.appendChild(notification);
    
    // Remove after 3 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease';
        setTimeout(() => {
            if (notification.parentNode) {
                document.body.removeChild(notification);
            }
        }, 300);
    }, 3000);
}

// Cart functions
function updateCartCount() {
    const count = cart.reduce((sum, item) => sum + item.quantity, 0);
    const cartCountElement = document.getElementById("cartCount");
    if (cartCountElement) {
        cartCountElement.textContent = count;
        
        // Add animation effect
        cartCountElement.style.animation = 'bounce 0.3s ease';
        setTimeout(() => {
            cartCountElement.style.animation = '';
        }, 300);
    }
}

function addToCart(productId, title, price) {
    console.log("Adding to cart:", productId, title, price);
    
    // Find the product to check stock
    const product = products.find(p => p.id === productId);
    if (!product) {
        showNotification("Product not found!", "error");
        return;
    }
    
    // Check if item already exists in cart
    const existingItem = cart.find(item => item.id === productId);
    const currentQuantity = existingItem ? existingItem.quantity : 0;
    
    // Check stock availability
    if (currentQuantity >= (product.stock || 0)) {
        showNotification("Sorry, not enough stock available!", "error");
        return;
    }
    
    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cart.push({ 
            id: productId, 
            title, 
            price, 
            quantity: 1,
            stock: product.stock || 0
        });
    }
    
    updateCartCount();
    showNotification(`${title} added to cart!`);
    
    // Save cart to sessionStorage for persistence
    saveCartToStorage();
}

function removeFromCart(productId) {
    const itemIndex = cart.findIndex(item => item.id === productId);
    if (itemIndex > -1) {
        const item = cart[itemIndex];
        showNotification(`${item.title} removed from cart!`);
        cart.splice(itemIndex, 1);
        updateCartCount();
        saveCartToStorage();
        showCart(); // Refresh cart display
    }
}

function updateCartItemQuantity(productId, newQuantity) {
    const item = cart.find(item => item.id === productId);
    if (!item) return;
    
    if (newQuantity <= 0) {
        removeFromCart(productId);
        return;
    }
    
    if (newQuantity > item.stock) {
        showNotification("Not enough stock available!", "error");
        return;
    }
    
    item.quantity = newQuantity;
    updateCartCount();
    saveCartToStorage();
    showCart(); // Refresh cart display
}

function showCart() {
    const modal = document.getElementById("cartModal");
    const cartItems = document.getElementById("cartItems");
    const cartTotal = document.getElementById("cartTotal");
    
    if (!modal || !cartItems || !cartTotal) return;
    
    cartItems.innerHTML = "";
    let total = 0;
    
    if (cart.length === 0) {
        cartItems.innerHTML = '<div class="empty-cart"><p>Your cart is empty.</p><p>Add some products to get started!</p></div>';
    } else {
        cart.forEach(item => {
            const itemTotal = item.price * item.quantity;
            total += itemTotal;
            
            const cartItemDiv = document.createElement("div");
            cartItemDiv.className = "cart-item";
            cartItemDiv.innerHTML = `
                <div class="cart-item-info">
                    <div class="cart-item-title">${item.title}</div>
                    <div class="cart-item-price">${formatPrice(item.price)} each</div>
                </div>
                <div class="cart-item-controls">
                    <button onclick="updateCartItemQuantity(${item.id}, ${item.quantity - 1})" 
                            ${item.quantity <= 1 ? 'class="danger"' : ''}>
                        ${item.quantity <= 1 ? '🗑️' : '−'}
                    </button>
                    <span style="margin: 0 1rem; font-weight: bold;">${item.quantity}</span>
                    <button onclick="updateCartItemQuantity(${item.id}, ${item.quantity + 1})" 
                            ${item.quantity >= item.stock ? 'disabled' : ''}>+</button>
                </div>
                <div class="cart-item-total">${formatPrice(itemTotal)}</div>
            `;
            cartItems.appendChild(cartItemDiv);
        });
    }
    
    cartTotal.textContent = formatPrice(total);
    modal.classList.add('show');
    modal.style.display = "flex";
}

function closeCart() {
    const modal = document.getElementById("cartModal");
    if (modal) {
        modal.classList.remove('show');
        setTimeout(() => {
            modal.style.display = "none";
        }, 300);
    }
}

function checkout() {
    if (cart.length === 0) {
        showNotification("Your cart is empty!", "error");
        return;
    }
    
    const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    const itemCount = cart.reduce((sum, item) => sum + item.quantity, 0);
    
    // Simulate checkout process
    showNotification("Processing your order...");
    
    setTimeout(() => {
        showNotification(`Thank you for your purchase! Total: ${formatPrice(total)} for ${itemCount} item(s)`);
        cart = [];
        updateCartCount();
        closeCart();
        saveCartToStorage();
    }, 1500);
}

// Storage functions
function saveCartToStorage() {
    try {
        sessionStorage.setItem('jai-market-cart', JSON.stringify(cart));
    } catch (error) {
        console.warn("Could not save cart to storage:", error);
    }
}

function loadCartFromStorage() {
    try {
        const savedCart = sessionStorage.getItem('jai-market-cart');
        if (savedCart) {
            cart = JSON.parse(savedCart);
            updateCartCount();
        }
    } catch (error) {
        console.warn("Could not load cart from storage:", error);
        cart = [];
    }
}

// Product display functions
function displayProducts(productsToDisplay) {
    const productList = document.getElementById("product-list");
    if (!productList) return;
    
    productList.innerHTML = "";
    
    if (!productsToDisplay || productsToDisplay.length === 0) {
        productList.innerHTML = '<div class="empty-products"><p>No products available at the moment.</p></div>';
        return;
    }
    
    productsToDisplay.forEach(product => {
        const productCard = document.createElement("div");
        productCard.classList.add("product-card");
        
        const stockClass = (product.stock || 0) < 5 ? 'low' : '';
        const stockText = (product.stock || 0) === 0 ? 'Out of Stock' : 
                         (product.stock || 0) < 5 ? `Only ${product.stock} left!` : 
                         `${product.stock} in stock`;
        
        productCard.innerHTML = `
            <h3>${product.title}</h3>
            ${product.description ? `<p class="description">${product.description}</p>` : ''}
            <div class="price">${formatPrice(product.price)}</div>
            <div class="stock ${stockClass}">${stockText}</div>
            <button onclick="addToCart(${product.id}, \`${product.title.replace(/`/g, '\\`')}\`, ${product.price})" 
                    ${(product.stock || 0) === 0 ? 'disabled' : ''}>
                ${(product.stock || 0) === 0 ? 'Out of Stock' : 'Add to Cart'}
            </button>
        `;
        
        productList.appendChild(productCard);
    });
}

// Event listeners and initialization
function initializeApp() {
    console.log("🚀 Initializing Jai Market app...");
    
    // Load cart from storage
    loadCartFromStorage();
    
    // Fetch products
    fetch("/api/products")
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log("✅ Products loaded:", data);
            products = data;
            displayProducts(products);
        })
        .catch(error => {
            console.error("❌ Failed to fetch products:", error);
            const productList = document.getElementById("product-list");
            if (productList) {
                productList.innerHTML = `
                    <div class="error-message">
                        <p>Failed to load products. Please refresh the page to try again.</p>
                        <button onclick="location.reload()">Refresh Page</button>
                    </div>
                `;
            }
        });
    
    // Close modal when clicking outside
    const modal = document.getElementById("cartModal");
    if (modal) {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                closeCart();
            }
        });
    }
    
    // Add keyboard shortcuts
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeCart();
        }
    });
    
    console.log("✅ App initialization complete!");
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideOutRight {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 0; }
    }
    
    @keyframes bounce {
        0%, 20%, 60%, 100% { transform: translateY(0); }
        40% { transform: translateY(-10px); }
        80% { transform: translateY(-5px); }
    }
    
    .error-message {
        text-align: center;
        padding: 2rem;
        background: #fed7d7;
        border-radius: 8px;
        color: #e53e3e;
    }
    
    .empty-products {
        text-align: center;
        padding: 3rem;
        color: #718096;
        grid-column: 1 / -1;
    }
`;
document.head.appendChild(style);

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeApp);
} else {
    initializeApp();
}