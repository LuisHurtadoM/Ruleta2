from ruleta import Ruleta

class Jugador:
    nombre: str
    saldo: int
    premio: str

    def __init__(self, nombre: str, saldo: int = 0):
        self.nombre = nombre
        if saldo < 0:
            self.saldo = 0
        else:
            self.saldo = saldo

    def obtener_permio(self) -> str:
        self.premio = Ruleta.girar_ruleta()
        if self.premio == "X2":
                self.saldo += self.saldo
        elif self.premio == "Quiebra":
                self.saldo = 0
        elif self.premio == "1/2":
            self.saldo = self.saldo / 2
        elif self.premio == "Comodin":
            self.premio = Ruleta.girar_ruleta
            
        
            
        
    def aplicar_premio(self, ganado: bool) -> None:
        if ganado:
             self.saldo += self.premio
