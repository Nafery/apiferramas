class User:
    def __init__(self, id, nombre, email, password, rol, creado_en):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.password = password
        self.rol = rol
        self.creado_en = creado_en

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'password': self.password,
            'rol': self.rol,
            'creado_en': self.creado_en
        }