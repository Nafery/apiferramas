from flask import Flask
from api.db.database import init_db
from flask_mysqldb import MySQL
from api.routes.route import register_routes

app = Flask(__name__)

# Configuración para base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ferremas_db'

mysql = init_db(app)

# Importar y registrar las rutas
register_routes(app, mysql)

if __name__ == '__main__':
    app.run(debug=True)