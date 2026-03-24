from inventario import Inventario, ProductoNoEncontrado
from producto import Libro, Cuaderno, Accesorio

# --- Banner de bienvenida ---
def mostrar_banner():
    print("==========================================")
    print("     BIENVENIDO A LA LIBRERÍA UNIVERSITARIA DE LA CUN")
    print("==========================================\n")

# --- Menú principal ---
def menu():
    print("1. Agregar producto")
    print("2. Consultar producto")
    print("3. Modificar producto")
    print("4. Eliminar producto")
    print("5. Listar productos")
    print("6. Salir")

# --- Programa principal ---
def main():
    mostrar_banner()  # ✅ Mostrar el banner al inicio
    inventario = Inventario()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("Tipo de producto (libro/cuaderno/accesorio): ").lower()
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))

            if tipo == "libro":
                autor = input("Autor: ")
                editorial = input("Editorial: ")
                producto = Libro(codigo, nombre, precio, cantidad, autor, editorial)
            elif tipo == "cuaderno":
                tipo_cuaderno = input("Tipo de cuaderno: ")
                producto = Cuaderno(codigo, nombre, precio, cantidad, tipo_cuaderno)
            elif tipo == "accesorio":
                descripcion = input("Descripción: ")
                producto = Accesorio(codigo, nombre, precio, cantidad, descripcion)
            else:
                print("Tipo no válido.\n")
                continue

            inventario.agregar_producto(producto)
            print("Producto agregado correctamente.\n")

        elif opcion == "2":
            codigo = input("Ingrese el código del producto: ")
            try:
                producto = inventario.buscar_producto(codigo)
                producto.mostrar_info()
            except ProductoNoEncontrado as e:
                print(e)

        elif opcion == "3":
            codigo = input("Ingrese el código del producto a modificar: ")
            try:
                producto = inventario.buscar_producto(codigo)
                nombre = input("Nuevo nombre (enter para mantener): ")
                precio = input("Nuevo precio (enter para mantener): ")
                cantidad = input("Nueva cantidad (enter para mantener): ")
                producto.actualizar(
                    nombre=nombre if nombre else None,
                    precio=float(precio) if precio else None,
                    cantidad=int(cantidad) if cantidad else None
                )
                print("Producto actualizado.\n")
            except ProductoNoEncontrado as e:
                print(e)

        elif opcion == "4":
            codigo = input("Ingrese el código del producto a eliminar: ")
            try:
                inventario.eliminar_producto(codigo)
                print("Producto eliminado.\n")
            except ProductoNoEncontrado as e:
                print(e)

        elif opcion == "5":
            inventario.listar_productos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.\n")

# --- Punto de entrada ---
if __name__ == "__main__":
    main()
