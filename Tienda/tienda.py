from producto import Producto
from cliente import Cliente

class Tienda:
    productos: list[Producto]
    clientes: list[Cliente]
    
    def __init__(self):
        self.productos = []
        self.clientes = []

    def crear_cliente(self, cliente: Cliente) -> None:
        self.clientes.append(cliente)

    def agregar_producto(self, producto: Producto) -> None:
        self.productos.append(producto)

    def vender_producto(self, producto: Producto, cliente: Cliente, cantidad: int) -> bool:
        if producto in self.productos and producto.verificar_stock(-cantidad):
            cliente.comprar_producto(producto, cantidad)
            return True
        else: raise Exception ("La venta no se pudo realizar.")

    def __str__(self) -> str:
        tienda_info = "Tienda:\n Productos en stock:\n"
       # tienda_info += ""
        for producto in self.productos:
            tienda_info += f"{producto.id}: {producto._nombre} - Precio: {producto.precio} - Cantidad en stock: {producto.cantidad_stock}\n"
        tienda_info += "Clientes:\n"
        for cliente in self.clientes:
            tienda_info += f"{cliente.id}: {cliente._nombre} - Productos comprados:\n"
            for producto_comprado, cantidad in cliente.productos_comprados:
                tienda_info += f"   {producto_comprado.id}: {producto_comprado._nombre} - Cantidad: {cantidad}\n"
        return tienda_info


if __name__ == "__main__":
    # Crear productos
    producto1 = Producto("001", "Laptop", 1000, 10)
    producto2 = Producto("002", "Smartphone", 500, 20)

    # Crear clientes
    cliente1 = Cliente("1001", "Juan", "123456789", "Calle 123")
    cliente2 = Cliente("1002", "Maria", "987654321", "Calle 456")

    # Crear tienda
    tienda = Tienda()

    # Agregar productos a la tienda
    tienda.agregar_producto(producto1)
    tienda.agregar_producto(producto2)

    # Crear clientes en la tienda
    tienda.crear_cliente(cliente1)
    tienda.crear_cliente(cliente2)

    # Vender productos
    tienda.vender_producto(producto1, cliente1, 8)
    tienda.vender_producto(producto2, cliente2, 10)

    # Imprimir información de la tienda
    print(tienda)
    Producto.actualizar_stock(producto2,20)
    print(tienda)
    


