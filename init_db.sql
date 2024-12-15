-- Создание таблицы пользователей
CREATE TABLE users (
   id SERIAL PRIMARY KEY,
   name VARCHAR(255) NOT NULL,
   email VARCHAR(255) UNIQUE NOT NULL
);

-- Создание таблицы продуктов  
CREATE TABLE products (
   id SERIAL PRIMARY KEY,
   name VARCHAR(255) NOT NULL,
   price DECIMAL(10, 2) NOT NULL
);

-- Создание таблицы заказов
CREATE TABLE orders (
   id SERIAL PRIMARY KEY,
   user_id INTEGER NOT NULL,
   product_id INTEGER NOT NULL,
   FOREIGN KEY (user_id) REFERENCES users(id),
   FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Добавление пользователей
INSERT INTO users (name, email)
VALUES
('Иван Иванов', 'ivan@example.com'),
('Анна Петрова', 'anna@example.com');

-- Добавление продуктов
INSERT INTO products (name, price)
VALUES
('Футболка', 25.99),
('Джинсы', 120.50),
('Кепка', 15.00);

-- Добавление заказов
INSERT INTO orders (user_id, product_id)
VALUES
(1, 2), -- Иван Иванов заказал джинсы
(2, 1), -- Анна Петрова заказала футболку
(1, 3); -- Иван Иванов заказал кепку