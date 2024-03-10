class Producto:
    def __init__(self, id: str, nombre: str, precio: float, cantidad_stock: int):
        self._id = id
        self._nombre = nombre
        self.precio = precio
        self.cantidad_stock = cantidad_stock

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id

    def actualizar_stock(self, cantidad: int) -> bool:
        if self.cantidad_stock + cantidad >= 0:
            self.cantidad_stock += cantidad
            return True
        return False
    
    def verificar_stock(self, cantidad: int) -> bool:
        if self.cantidad_stock + cantidad >= 0:
            return True
        return False