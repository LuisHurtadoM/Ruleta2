#from ruleta import Ruleta

class Jugador:
    def __init__(self, nombre: str, saldo: int = 200):
        self.nombre = nombre
        self.saldo = saldo

    def elegir_letra(self) -> str:
        letra = input("Elige una letra: ").upper()
        return letra

    def aplicar_premio(self, premio: str) -> None:
        if premio == "X2":
            self.saldo *= 2
        elif premio == "Quiebra":
            self.saldo = 0
        elif premio == "1/2":
            self.saldo //= 2
        elif premio == "Comodin":
            pass  # Implementar lógica para Comodin si es necesario
        else:
            self.saldo += int(premio)
