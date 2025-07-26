# Python CLI for Restaurant Ordering System

def display_menu(menu):
    print("\n--- Menu ---")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")
    print()

def take_order(menu):
    order = {}
    while True:
        display_menu(menu)
        choice = input("Enter the name of the item to order (or type 'done' to finish): ").strip().lower()
        if choice == 'done':
            break
        elif choice in menu:
            quantity = input(f"How many {choice}(s) would you like to order? ").strip()
            if quantity.isdigit():
                quantity = int(quantity)
                if choice in order:
                    order[choice] += quantity
                else:
                    order[choice] = quantity
                print(f"Added {quantity} {choice}(s) to your order.")
            else:
                print("Invalid quantity. Please enter a number.")
        else:
            print("Invalid item. Please choose from the menu.")
    return order

def calculate_total(order, menu):
    total = 0
    for item, quantity in order.items():
        total += menu[item] * quantity
    return total

def main():
    menu = {
        "burger": 5.99,
        "pizza": 8.99,
        "salad": 4.99,
        "soda": 1.99,
        "fries": 2.99
    }
    
    print("Welcome to the Restaurant Ordering System!")
    while True:
        print("\nOptions:")
        print("1. View Menu")
        print("2. Place an Order")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            display_menu(menu)
        elif choice == '2':
            order = take_order(menu)
            if order:
                print("\n--- Order Summary ---")
                for item, quantity in order.items():
                    print(f"{item}: {quantity} x ${menu[item]:.2f} = ${menu[item] * quantity:.2f}")
                total = calculate_total(order, menu)
                print(f"Total: ${total:.2f}")
                confirm = input("Would you like to confirm your order? (yes/no): ").strip().lower()
                if confirm == 'yes':
                    print("Thank you for your order! It has been placed.")
                else:
                    print("Order canceled.")
            else:
                print("No items were ordered.")
        elif choice == '3':
            print("Thank you for visiting! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()