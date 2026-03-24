
from producto import Producto, Libro, Cuaderno, Accesorio

class ProductoNoEncontrado(Exception):
    pass

class Inventario:
    def __init__(self):
        self.productos = []
                                                           # inventario.py
    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_producto(self, codigo):
        for p in self.productos:
            if p.codigo == codigo:
                return p
        raise ProductoNoEncontrado(f"Producto con código {codigo} no encontrado.")

    def eliminar_producto(self, codigo):
        producto = self.buscar_producto(codigo)
        self.productos.remove(producto)

    def listar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        for p in self.productos:
            p.mostrar_info()
            print("-" * 20)
