CREATE DATABASE ecommerce
    DEFAULT CHARACTER SET = 'utf8mb4';

USE ecommerce;

CREATE TABLE Categorias (
    categoria_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255)
);

CREATE TABLE Usuarios (
    usuario_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Productos (
    producto_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    categoria_id INT,
    FOREIGN KEY (categoria_id) REFERENCES Categorias(categoria_id)
);

CREATE TABLE Pedidos (
    pedido_id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT,
    fecha_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado VARCHAR(50) DEFAULT 'pendiente',
    total DECIMAL(10, 2),
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id)
);

CREATE TABLE Detalles_Pedido (
    detalle_id INT PRIMARY KEY AUTO_INCREMENT,
    pedido_id INT,
    producto_id INT,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES Pedidos(pedido_id),
    FOREIGN KEY (producto_id) REFERENCES Productos(producto_id)
);

-- Insertar datos de ejemplo

-- Insertar en Categorias
INSERT INTO Categorias (nombre, descripcion) VALUES
('Electrónica', 'Dispositivos electrónicos y gadgets'),
('Ropa', 'Vestimenta y accesorios'),
('Hogar', 'Artículos para el hogar y decoración');

-- Insertar en Usuarios
INSERT INTO Usuarios (nombre, correo, contrasena) VALUES
('Juan Pérez', 'juan.perez@example.com', 'password123'),
('Ana López', 'ana.lopez@example.com', 'securepass'),
('Carlos Gómez', 'carlos.gomez@example.com', 'mypassword');

-- Insertar en Productos
INSERT INTO Productos (nombre, descripcion, precio, stock, categoria_id) VALUES
('Smartphone', 'Teléfono inteligente de última generación', 699.99, 50, 1),
('Camisa Casual', 'Camisa de algodón de manga larga', 29.99, 100, 2),
('Sofá de 3 plazas', 'Sofá cómodo de tela', 399.99, 20, 3);

-- Insertar en Pedidos
INSERT INTO Pedidos (usuario_id, estado, total) VALUES
(1, 'pendiente', 729.98),
(2, 'completado', 29.99);

-- Insertar en Detalles_Pedido
INSERT INTO Detalles_Pedido (pedido_id, producto_id, cantidad, precio_unitario) VALUES
(1, 1, 1, 699.99),
(1, 2, 1, 29.99),
(2, 2, 1, 29.99);