-- Región de creación de la base de datos
-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS ferremas_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE ferremas_db;

-- Tabla de marcas
CREATE TABLE marca (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- Tabla de categorías (sin subcategorías)
CREATE TABLE categoria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE producto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo_producto VARCHAR(50) UNIQUE NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    marca_id INT,
    categoria_id INT,
    modelo VARCHAR(100),
    precio DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (marca_id) REFERENCES marcas(id),
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);

-- Tabla de sucursales
CREATE TABLE sucursal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    direccion VARCHAR(255)
);

-- Tabla de stock por sucursal
CREATE TABLE stock (
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto_id INT,
    sucursal_id INT,
    cantidad INT DEFAULT 0,
    FOREIGN KEY (producto_id) REFERENCES productos(id),
    FOREIGN KEY (sucursal_id) REFERENCES sucursales(id)
);

-- Tabla de usuarios (para login y roles)
CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    rol ENUM('admin', 'vendedor', 'cliente') DEFAULT 'cliente',
    creado_en DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de contactos de clientes
CREATE TABLE contacto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    mensaje TEXT NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- REGIÓN DE INSERCIÓN DE DATOS
INSERT INTO marca (nombre) VALUES 
('Bosch'), 
('Makita'), 
('Stanley'), 
('3M');

INSERT INTO categoria (nombre) VALUES 
('Herramientas Manuales'), 
('Herramientas Eléctricas'), 
('Materiales Básicos'), 
('Acabados'), 
('Equipos de Seguridad'), 
('Tornillos y Anclajes');

INSERT INTO producto (codigo_producto, nombre, descripcion, marca_id, categoria_id, modelo, precio)
VALUES
('FER-001', 'Martillo de Uña 16oz', 'Martillo para carpintería de alta resistencia.', 3, 1, 'ST-1234', 4990.00),
('FER-002', 'Taladro Percutor 600W', 'Taladro eléctrico con función percutora.', 1, 2, 'BO-600W', 38990.00),
('FER-003', 'Cemento Portland 25kg', 'Bolsa de cemento para construcción general.', 2, 3, 'MK-CEM25', 7490.00),
('FER-004', 'Pintura Acrílica Blanca 1gl', 'Pintura lavable para interior/exterior.', 4, 4, '3M-PAW1G', 12990.00),
('FER-005', 'Guantes de Seguridad Nitrilo', 'Guantes resistentes a químicos y cortes.', 4, 5, '3M-GSN', 3990.00),
('FER-006', 'Caja de Tornillos 100un', 'Tornillos para madera, 5 cm.', 2, 6, 'MK-T100', 1990.00);

INSERT INTO sucursal (nombre, direccion)
VALUES 
('Sucursal Central', 'Av. Principal 123, Santiago'),
('Sucursal Norte', 'Calle Norte 456, Antofagasta');

INSERT INTO stock (producto_id, sucursal_id, cantidad)
VALUES
(1, 1, 50),
(2, 1, 30),
(3, 1, 100),
(4, 2, 25),
(5, 2, 60),
(6, 2, 90);

INSERT INTO usuario (nombre, email, password, rol)
VALUES
('Admin General', 'admin@ferremas.cl', 'admin1234', 'admin'),
('Vendedor Norte', 'ventasnorte@ferremas.cl', 'vendedor456', 'vendedor'),
('Juan Cliente', 'juan@correo.cl', 'cliente789', 'cliente');

RENAME TABLE product TO producto;
RENAME TABLE CATEGORIAs TO categoria;
RENAME TABLE CONTACTOS TO contacto;
RENAME TABLE MARCAS TO marca;
RENAME TABLE SUCURSALES TO sucursal;
RENAME TABLE USUARIOS TO usuario;