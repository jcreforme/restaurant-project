# Restaurant Ordering System

A simple command-line interface (CLI) application for ordering food at a restaurant. This Python-based system allows users to view a menu, place an order, and calculate the total cost of their order.

---

## Features

- **View Menu**: Displays a list of available menu items with their prices.
- **Place an Order**: Allows users to select items from the menu and specify quantities.
- **Calculate Total**: Automatically calculates the total cost of the order.
- **Order Summary**: Displays a summary of the order before confirmation.
- **Error Handling**: Handles invalid inputs gracefully (e.g., invalid item names or quantities).

---

## How to Run

1. **Save the Script**:
   - Save the Python script as `restaurant_ordering_system.py`.

2. **Install Python**:
   - Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/).

3. **Run the Script**:
   - Open a terminal and navigate to the directory containing the script.
   - Run the script using:
     ```bash
     python restaurant_ordering_system.py
     ```

4. **Follow the Instructions**:
   - Interact with the program by following the prompts in the terminal.

---

## Code Overview

### Key Functions

- **`display_menu(menu)`**:
  - Displays the menu items and their prices.

- **`take_order(menu)`**:
  - Allows the user to select items from the menu and specify quantities.
  - Returns the user's order as a dictionary.

- **`calculate_total(order, menu)`**:
  - Calculates the total cost of the order based on the menu prices.

- **`main()`**:
  - The main function that drives the program, providing options to view the menu, place an order, and exit.

---

## Example Usage

1. **Start the Program**:
   - Run the script and follow the menu options.

2. **View the Menu**:
   - Select the option to view the menu and see the available items with prices.

3. **Place an Order**:
   - Enter the name of the item and specify the quantity.

4. **View Order Summary**:
   - Review the items in your order and the total cost.

5. **Confirm or Cancel**:
   - Confirm your order to complete the process or cancel to start over.

---

## Sample Menu

The menu is defined in the script and can be customized. Example:

```python
menu = {
    "burger": 5.99,
    "pizza": 8.99,
    "salad": 4.99,
    "soda": 1.99,
    "fries": 2.99
}