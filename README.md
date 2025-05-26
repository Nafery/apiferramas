![Badge en Desarollo](https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green)
# 🛠️ Ferramas API (Arquitectura en capas)

API RESTful para gestión de productos, usuarios para inicios de sesión, conversión de divisa
y pagos con Transbank para la cadena de ferreterías Ferramas. 

## 🚀 Tecnologías

- Python 3
- Flask
- MySQL
- Flask-MySQL
- Flasgger (Swagger UI)
- Transbank SDK
- Requests 

## 📁 Estructura del proyecto
```plaintext
apiferramas/
├── .gitignore
├── app.py
├── credenciales.txt
├── ferramas.sql
├── requirements.txt
├── README.md
└── api/
    ├── db/
    ├── models/
    ├── services/
    ├── utils/
    └── routes/
```
## 🧱 Arquitectura en capas

La API sigue una arquitectura en capas para mantener el código organizado, reutilizable y escalable. A continuación se describe cada capa:

- **`routes/`**: Define las rutas de la API y maneja las solicitudes HTTP. Se encarga de recibir y enviar respuestas.
- **`services/`**: Contiene la lógica de negocio y orquesta el flujo de datos entre las rutas y los modelos. Aquí se ubican las funciones principales que procesan los datos.
- **`models/`**: Encapsula la estructura de los datos y realiza consultas SQL directas a la base de datos.
- **`db/`**: Puede contener configuraciones adicionales para la conexión a la base de datos (si se usan).
- **`utils/`**: Funciones auxiliares o utilitarias que pueden ser compartidas entre servicios.

Este enfoque modular facilita el mantenimiento del proyecto y permite realizar pruebas o cambios en una capa sin afectar directamente a las demás.



## 🔧 Instalación y ejecución

```bash
git clone https://github.com/Nafery/apiferramas
cd apiferramas
pip install -r requirements.txt
python3 app.py
```

## 🛠️  Configuración de la base de datos
### 1.- Crear una base de datos
Abre la terminal o línea de comandos y ejecuta el siguiente comando:

```bash
mysql -u root -p
```
Luego dentro de tu editor de MySQL de preferencia ejecuta el siguiente código:
```bash
CREATE DATABASE ferramas;
EXIT;
```

### 2.- Importar el archivo de la base de datos ferramas.sql
Asegurándote de tener el archivo ferramas.sql en la carpeta del repositorio, ejecuta:
```bash
mysql -u root -p ferramas <ferramas.sql
```

### 3.- Configurar la conexión en app.py
En el archivo app.py verifica las siguientes lineas de código
```python
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root' #Tu usuario mysql propio
app.config['MYSQL_PASSWORD'] = '' #Contraseña del usuario
app.config['MYSQL_DB'] = 'ferramas'
```

## 🌐 Endpoints de la API

### Productos
| Método | Ruta        | Descripción                 |
| ------ | ----------- | --------------------------- |
| GET    | `/products` | Obtener todos los productos |

### Usuarios

| Método | Ruta     | Descripción                |
| ------ | -------- | -------------------------- |
| GET    | `/users` | Obtener todos los usuarios |

### Divisas

| Método | Ruta                              | Descripción                       |
| ------ | --------------------------------- | --------------------------------- |
| GET    | `/currency/usd`                   | Obtener el valor actual del dólar |
| GET    | `/currency/eur`                   | Obtener el valor actual del euro  |

### Pagos Webpay

| Método | Ruta                | Descripción                        |
| ------ | ------------------- | ---------------------------------- |
| POST   | `/webpay/init`      | Iniciar transacción de pago Webpay |
| POST   | `/webpay/confirmar` | Confirmar transacción Webpay       |

## 🧪 Pruebas y ejemplos

### 📦 Requisitos

Asegúrate de tener la API corriendo en http://localhost:5000

### ✅ Obtener lista de productos

En el navegador de tu preferencia busca http://localhost:5000/products.
Al ejecutar el código anterior deberías ver un json que te retorne la información de los productos registrados (adjuntamos un fragmento).

```json
{
    "categoria_id": 1,
    "codigo_producto": "FER-001",
    "descripcion": "Martillo para carpinter\u00eda de alta resistencia.",
    "id": 1,
    "marca_id": 3,
    "modelo": "ST-1234",
    "nombre": "Martillo de U\u00f1a 16oz",
    "precio": "4990.00"
}
```

### 🧍 Obtener lista de usuarios

En el navegador de tu preferencia busca http://localhost:5000/users.
Al ejecutar el código anterior deberías ver un json que te retorne la información de los usuarios registrados (adjuntamos un fragmento).

```json
{
    "creado_en": "Wed, 07 May 2025 12:42:42 GMT",
    "email": "admin@ferremas.cl",
    "id": 1,
    "nombre": "Admin General",
    "password": "admin1234",
    "rol": "admin"
}
```

### 💸 Iniciar prueba de pago con Webpay

Acá puedes ejecutar una prueba de la integración del SDK de Transbank con Postman o con curl, la prueba con cada una de estas opciones sería:

#### Curl

Request:

```bash
curl -X POST http://localhost:5000/webpay/init \
  -H "Content-Type: application/json" \
  -d '{"amount": 5000, "session_id": "user123", "return_url": "http://localhost:3000/webpay/response"}'
```

Response:

```json
{
  "url": "https://webpay.someurl.com/init",
  "token": "abc123xyz"
}
```

#### 🧪 Postman

Para probar la api con Postman debemos seguir los siguientes pasos:

1.- Abre Postman.
2.- Crea un nuevo request.
3.- Selecciona el método POST.
4.- URL: http://localhost:5000/webpay/init
5.- Body: Selecciona raw y JSON y pega lo siguiente
```bash
{
  "amount": 5000,
  "session_id": "usuario_demo",
  "return_url": "http://localhost:3000/webpay/response"
}
```
6.- Haz click en SEND.

👉 Respuesta esperada:
```json
{
  "url": "https://webpay.url/...",
  "token": "XYZ123..."
}
```
