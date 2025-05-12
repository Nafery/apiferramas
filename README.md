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

## Estructura del proyecto
apiferramas/
│
├── .gitignore
├── app.py
├── credenciales.txt
├── ferramas.sql
├── requirements.txt
├── README.md
└── api/
    ├── db
    ├── models/
    ├── services/
    ├── utils/
    └── routes/

## Instalación y ejecución

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
CREATE DATABASE ferramas;
EXIT;

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

## Endpoints de la API

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
