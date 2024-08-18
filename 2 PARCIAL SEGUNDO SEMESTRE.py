class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, id, nombre, cantidad, precio):
        if any(p.get_id() == id for p in self.productos):
            print(f"Error: Ya existe un producto con el ID {id}.")
        else:
            nuevo_producto = Producto(id, nombre, cantidad, precio)
            self.productos.append(nuevo_producto)
            print("Producto añadido con éxito.")

    def eliminar_producto(self, id):
        producto_a_eliminar = next((p for p in self.productos if p.get_id() == id), None)
        if producto_a_eliminar:
            self.productos.remove(producto_a_eliminar)
            print(f"Producto con ID {id} eliminado con éxito.")
        else:
            print(f"Error: No se encontró producto con el ID {id}.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        producto = next((p for p in self.productos if p.get_id() == id), None)
        if producto:
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            print(f"Producto con ID {id} actualizado con éxito.")
        else:
            print(f"Error: No se encontró producto con el ID {id}.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacío.")


def menu():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Gestión de Inventarios ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto(s)")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = int(input("Ingrese ID del producto: "))
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            inventario.añadir_producto(id, nombre, cantidad, precio)

        elif opcion == '2':
            id = int(input("Ingrese ID del producto a eliminar: "))
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = int(input("Ingrese ID del producto a actualizar: "))
            cantidad = input("Ingrese nueva cantidad (dejar en blanco si no se cambia): ")
            precio = input("Ingrese nuevo precio (dejar en blanco si no se cambia): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == '4':
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    menu()
