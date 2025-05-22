-- Región de creación de la base de datos
DROP DATABASE IF EXISTS ferremas_db;
CREATE DATABASE IF NOT EXISTS ferremas_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE ferremas_db;

-- Tabla de marcas
CREATE TABLE marca (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- Tabla de categorías
CREATE TABLE categoria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- Tabla de productos
CREATE TABLE producto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo_producto VARCHAR(50) UNIQUE NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    marca_id INT,
    categoria_id INT,
    modelo VARCHAR(100),
    precio DECIMAL(10, 2) NOT NULL,
    imagen_url VARCHAR(255),
    FOREIGN KEY (marca_id) REFERENCES marca(id),
    FOREIGN KEY (categoria_id) REFERENCES categoria(id)
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
    FOREIGN KEY (producto_id) REFERENCES producto(id),
    FOREIGN KEY (sucursal_id) REFERENCES sucursal(id)
);

-- Tabla de usuarios
CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    rol ENUM('admin', 'vendedor', 'cliente') DEFAULT 'cliente',
    creado_en DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de contactos
CREATE TABLE contacto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    mensaje TEXT NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Región de inserción de datos

-- Marcas
INSERT INTO marca (nombre) VALUES 
('Bosch'), 
('Makita'), 
('Stanley'), 
('3M'),
('DeWalt'),
('Black+Decker'),
('Truper');

-- Categorías
INSERT INTO categoria (nombre) VALUES 
('Herramientas Manuales'), 
('Herramientas Eléctricas'), 
('Materiales Básicos'), 
('Acabados'), 
('Equipos de Seguridad'), 
('Tornillos y Anclajes'),
('Fijaciones'),
('Pinturas');

-- Productos
INSERT INTO producto (codigo_producto, nombre, descripcion, marca_id, categoria_id, modelo, precio, imagen_url) VALUES
('FER-001', 'Martillo de Uña 16oz', 'Martillo para carpintería de alta resistencia.', 3, 1, 'ST-1234', 4990.00, 'https://dojiw2m9tvv09.cloudfront.net/16650/product/stht54234-33883.jpeg'),
('FER-002', 'Taladro Percutor 600W', 'Taladro eléctrico con función percutora.', 1, 2, 'BO-600W', 38990.00, 'https://res.cloudinary.com/rsc/image/upload/b_rgb:FFFFFF,c_pad,dpr_1.0,f_auto,q_auto,w_700/c_pad,w_700/F1827539-01'),
('FER-003', 'Cemento Portland 25kg', 'Bolsa de cemento para construcción general.', 2, 3, 'MK-CEM25', 7490.00, 'https://www.emat.com.uy/imgs/productos/productos37_8320.jpg'),
('FER-004', 'Pintura Acrílica Blanca 1gl', 'Pintura lavable para interior/exterior.', 4, 4, '3M-PAW1G', 12990.00, 'https://media.falabella.com/sodimacCL/2733668_01/w=800,h=800,fit=pad'),
('FER-005', 'Guantes de Seguridad Nitrilo', 'Guantes resistentes a químicos y cortes.', 4, 5, '3M-GSN', 3990.00, 'https://www.swsafety.com.co/wp-content/uploads/2021/04/D_NQ_NP_870001-CBT43758541356_102020-W.jpg'),
('FER-006', 'Caja de Tornillos 100un', 'Tornillos para madera, 5 cm.', 2, 6, 'MK-T100', 1990.00, 'https://cdnx.jumpseller.com/my-toolbox-chile/image/57988568/resize/280/280?1739480786'),
('FER-007', 'Atornillador Inalámbrico 12V', 'Atornillador portátil con batería recargable.', 6, 2, 'BD-AS12', 29990.00, 'https://cdnx.jumpseller.com/maqstore/image/43514070/resize/540/540?1702473464'),
('FER-008', 'Caja Organizadora Tornillos', 'Caja plástica con divisiones para tornillos.', 7, 6, 'TP-BOX1', 4990.00, 'https://m.media-amazon.com/images/I/81iUkimnSBL._AC_UF894,1000_QL80_.jpg'),
('FER-009', 'Brocha 2" de Cerda Negra', 'Ideal para pintura de muros y maderas.', 4, 8, '3M-BR2', 1590.00, 'https://imagedelivery.net/4fYuQyy-r8_rpBpcY7lH_A/sodimacCO/204490/public'),
('FER-010', 'Máscara Facial Transparente', 'Protección facial contra salpicaduras.', 5, 5, 'DW-FSM', 2590.00, 'https://images-na.ssl-images-amazon.com/images/I/51CoS3sVsSL._AC_UL495_SR435,495_.jpg'),
('FER-011', 'Nivel de Burbuja 60cm', 'Nivel para trabajos de albañilería.', 3, 1, 'ST-LVL60', 6890.00, 'https://m.media-amazon.com/images/I/41VU0HS5dZL._AC_UF894,1000_QL80_.jpg'),
('FER-012', 'Disco de Corte 4.5"', 'Disco para cortar metal, compatible con esmeriles.', 6, 2, 'DW-DC45', 1790.00, 'https://media.falabella.com/sodimacCL/3185222_17/w=800,h=800,fit=pad'),
('FER-013', 'Pegamento de Contacto 1L', 'Adhesivo multipropósito de alta resistencia.', 4, 4, '3M-ADH1L', 3990.00, 'https://ail.com.mx/wp-content/uploads/2023/07/62109965301-1.jpg.webp');

-- Sucursales
INSERT INTO sucursal (nombre, direccion) VALUES 
('Sucursal Central', 'Av. Principal 123, Santiago'),
('Sucursal Norte', 'Calle Norte 456, Antofagasta'),
('Sucursal Sur', 'Ruta 5 Sur Km 20, Talca'),
('Sucursal Oriente', 'Av. Las Condes 12345, Santiago');

-- Stock
INSERT INTO stock (producto_id, sucursal_id, cantidad) VALUES
(1, 1, 50),
(2, 1, 30),
(3, 1, 100),
(4, 2, 25),
(5, 2, 60),
(6, 2, 90),
(7, 1, 20),
(8, 2, 45),
(9, 3, 70),
(10, 4, 30),
(11, 1, 40),
(12, 2, 60),
(13, 3, 50);

-- Usuarios
INSERT INTO usuario (nombre, email, password, rol) VALUES
('Admin General', 'admin@ferremas.cl', 'admin1234', 'admin'),
('Vendedor Norte', 'ventasnorte@ferremas.cl', 'vendedor456', 'vendedor'),
('Juan Cliente', 'juan@correo.cl', 'cliente789', 'cliente'),
('Claudia Vendedora', 'claudia@ferremas.cl', 'vendedora123', 'vendedor'),
('Carlos Cliente', 'carlos@correo.cl', 'cliente456', 'cliente'),
('Fernanda Cliente', 'fernanda@correo.cl', 'fer789', 'cliente');
