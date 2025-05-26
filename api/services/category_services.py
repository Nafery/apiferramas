from api.models.category import Category

class CategoryService:
    def __init__(self, mysql):
        self.mysql = mysql

    #Obtenemos todas las categorías desde la base de datos
    def get_all_categories(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT id, nombre FROM categoria")
        results = cursor.fetchall()
        cursor.close()
        categorias = [Category(id=row[0], nombre=row[1]).to_dict() for row in results]
        return categorias
