CREATE DATABASE IF NOT EXISTS restaurant;

USE restaurant;

CREATE TABLE IF NOT EXISTS menu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    menu_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (menu_id) REFERENCES menu(id)
);

INSERT INTO menu (name, price) VALUES
('Burger', 5.99),
('Pizza', 8.99),
('Pasta', 7.99),
('Salad', 4.99);