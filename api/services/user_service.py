from api.models.user import User

class UserService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    def get_all_users(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT id, nombre, email, password, rol, creado_en FROM usuario")
        results = cursor.fetchall()
        users = [User(id=row[0], nombre=row[1], email=row[2], password=row[3], rol=row[4], creado_en=row[5]).to_dict() for row in results]
        return users