from menu import show_menu, place_order

def main():
    print("Welcome to the Restaurant Ordering System!\n")
    while True:
        print("Options:")
        print("1. View Menu")
        print("2. Place an Order")
        print("3. Exit\n")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            show_menu()
        elif choice == "2":
            place_order()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()