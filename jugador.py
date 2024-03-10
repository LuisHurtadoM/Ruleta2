#from ruleta import Ruleta

class Jugador:
    def __init__(self, nombre: str, saldo: int = 200):
        self.nombre = nombre
        self.saldo = saldo
        self.comodines_disponibles = 0

    def usar_comodin(self):
        if self.comodines_disponibles > 0:
            self.comodines_disponibles -= 1
            print(f"{self.nombre} ha utilizado un comodín para seguir jugando.")
            return True  # Se utilizó un comodín con éxito
        else:
            print("No tienes comodines disponibles.")
            return False  # No se pudo utilizar un comodín

    def recibir_comodin(self, cantidad: int):
        self.comodines_disponibles += cantidad
        # print(f"{self.nombre} ha recibido {cantidad} comodines.")

    def elegir_letra(self) -> str:
        letra = input("Elige una letra: ").upper()
        return letra

    def aplicar_premio(self, premio: str, veces_aparece_letra: int = 1) -> None:
        if premio == "X2":
            self.saldo *= 2 * veces_aparece_letra
        elif premio == "Quiebra":
            self.saldo = 0
        elif premio == "1/2":
            self.saldo //= 2
        elif premio == "Comodin":
            pass  # Implementar lógica para Comodin si es necesario
        else:
            self.saldo += int(premio)* veces_aparece_letra
