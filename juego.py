from jugador import Jugador
from ruleta import Ruleta
from tablero import Tablero
import random

class Juego:
    jugadores : list[Jugador]
    ruleta : Ruleta
    tablero : Tablero
    categoria: [] # type: ignore
    res_categoria: int

    def __init__(self,jugador: Jugador, ruleta: Ruleta, tablero: Tablero):
        self.jugadores.append(jugador)
        self.ruleta = Ruleta
        self.tablero = Tablero
        self.categoria =[1,2,3] 

    def categoria_juego(self,):
        res_categoria = random.choice(self.categoria)
        return res_categoria


if __name__=="__main__":
    jugador1= Jugador("Luis")
    jugador2= Jugador("Aura")
    jugador3= Jugador("Rodolfo")
    jugador4= Jugador("Alexandra")
