# restaurant_ordering.py

menu = {
    "Tacos": 25,
    "Burger": 45,
    "Pizza": 60,
    "Salad": 30,
    "Soda": 15,
    "Coffee": 20
}

cart = []

def show_menu():
    print("\n📋 MENU:")
    for item, price in menu.items():
        print(f"- {item}: ${price} MXN")

def add_to_cart():
    item = input("🔹 What would you like to order? (type exact name): ").title()
    if item in menu:
        quantity = input(f"🔹 How many {item}s would you like? ")
        if quantity.isdigit():
            cart.append((item, int(quantity)))
            print(f"✅ {quantity} x {item} added to your cart.")
        else:
            print("⚠️ Please enter a valid number.")
    else:
        print("❌ Item not found in menu.")

def view_cart():
    print("\n🛒 Your Cart:")
    total = 0
    for item, quantity in cart:
        price = menu[item] * quantity
        print(f"- {item} x{quantity}: ${price} MXN")
        total += price
    print(f"💰 Total: ${total} MXN")

def confirm_order():
    if cart:
        view_cart()
        confirm = input("🔔 Confirm order? (yes/no): ").lower()
        if confirm == "yes":
            print("🎉 Order confirmed! Thank you for ordering.")
            cart.clear()
        else:
            print("📝 Order not confirmed. You can continue ordering.")
    else:
        print("🛒 Your cart is empty!")

def run():
    print("🍽️ Welcome to Terminal Bistro!")
    while True:
        print("\nChoose an option:")
        print("1. View Menu")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Confirm Order")
        print("5. Exit")

        choice = input("➡️ Enter choice (1-5): ")

        if choice == "1":
            show_menu()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            confirm_order()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    run()
