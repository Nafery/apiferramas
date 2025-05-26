from api.models.product import Product

class ProductService:
    def __init__(self, mysql):
        self.mysql = mysql

    #Obtenemos todos los productos desde la base de datos
    def get_all_products(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT id, codigo_producto, nombre, descripcion, marca_id, categoria_id, modelo, precio, imagen_url FROM producto")
        results = cursor.fetchall()
        products = [Product(id=row[0], codigo_producto=row[1], nombre=row[2], descripcion=row[3], marca_id=row[4], categoria_id=row[5], modelo=row[6], precio=row[7], imagen_url=row[8]).to_dict() for row in results]
        return products
    
    #Obtenemos un producto por su ID
    def get_products_by_category(self, category_id):
        cursor = self.mysql.connection.cursor()
        query = """
            SELECT p.id, p.codigo_producto, p.nombre, p.descripcion, 
                p.modelo, p.precio, p.imagen_url, m.nombre AS marca, c.nombre AS categoria
            FROM producto p
            LEFT JOIN marca m ON p.marca_id = m.id
            LEFT JOIN categoria c ON p.categoria_id = c.id
            WHERE p.categoria_id = %s
        """
        cursor.execute(query, (category_id,))
        data = cursor.fetchall()
        column_names = [col[0] for col in cursor.description]
        cursor.close()
        return [dict(zip(column_names, row)) for row in data]