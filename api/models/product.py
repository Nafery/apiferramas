class Product:
    def __init__(self, id, codigo_producto, nombre, descripcion, marca_id, categoria_id, modelo, precio):
        self.id = id
        self.codigo_producto = codigo_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.marca_id = marca_id
        self.categoria_id = categoria_id
        self.modelo = modelo
        self.precio = precio

    def to_dict(self):
        return {
            'id': self.id,
            'codigo_producto': self.codigo_producto,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'marca_id': self.marca_id,
            'categoria_id': self.categoria_id,
            'modelo': self.modelo,
            'precio': self.precio
        }