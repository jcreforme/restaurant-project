from db import get_connection

def show_menu():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, price FROM menu")
    items = cursor.fetchall()
    print("\nMenu:")
    for item in items:
        print(f"{item[0]}. {item[1]} - ${item[2]:.2f}")
    cursor.close()
    connection.close()

def place_order():
    show_menu()
    item_id = input("\nEnter the ID of the item you want to order: ").strip()
    quantity = input("Enter the quantity: ").strip()

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO orders (menu_id, quantity) VALUES (%s, %s)", (item_id, quantity))
    connection.commit()
    print("Order placed successfully!")
    cursor.close()
    connection.close()