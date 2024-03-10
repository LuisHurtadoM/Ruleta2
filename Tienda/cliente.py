from producto import Producto

class Cliente:
    def __init__(self, id: str, nombre: str, telefono: str, direccion: str):
        self._id = id
        self._nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.productos_comprados = []

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def comprar_producto(self, producto: Producto, cantidad: int) -> bool:
        if producto.actualizar_stock(-cantidad):
            self.productos_comprados.append((producto, cantidad))
            return True
        raise Exception ("La cantidad solicitada excede el stock. No se puede realizar la venta")
   
   
       
