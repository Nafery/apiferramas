from api.models.product import Product

class ProductService:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_products(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT id, codigo_producto, nombre, descripcion, marca_id, categoria_id, modelo, precio FROM producto")
        results = cursor.fetchall()
        products = [Product(id=row[0], codigo_producto=row[1], nombre=row[2], descripcion=row[3], marca_id=row[4], categoria_id=row[5], modelo=row[6], precio=row[7]).to_dict() for row in results]
        return products