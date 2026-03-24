# producto.py
class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_info(self):
        print(f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}")

    def actualizar(self, nombre=None, precio=None, cantidad=None):
        if nombre: self.nombre = nombre
        if precio: self.precio = precio
        if cantidad: self.cantidad = cantidad


class Libro(Producto):
    def __init__(self, codigo, nombre, precio, cantidad, autor, editorial):
        super().__init__(codigo, nombre, precio, cantidad)
        self.autor = autor
        self.editorial = editorial

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Autor: {self.autor}, Editorial: {self.editorial}")


class Cuaderno(Producto):
    def __init__(self, codigo, nombre, precio, cantidad, tipo):
        super().__init__(codigo, nombre, precio, cantidad)
        self.tipo = tipo

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo: {self.tipo}")


class Accesorio(Producto):
    def __init__(self, codigo, nombre, precio, cantidad, descripcion):
        super().__init__(codigo, nombre, precio, cantidad)
        self.descripcion = descripcion

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Descripción: {self.descripcion}")
