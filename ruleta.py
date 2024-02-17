import random
from jugador import Jugador

class Ruleta:
    res_ruleta: str #Resutado que genera la ruleta al aplcarse el random
    ruleta_categoria: int
    valores_ruleta: list [str]
    frase_juego: str

    def __init__(self, ruleta_categoria:int):
        self.res_ruleta = ""
        self.ruleta_categoria = ruleta_categoria
        self.valores_ruleta = ["Pierde turno", "Quiebra","X2", "1/2","Comodin","50", "150", "200"]

    def girar_ruleta(self,jugador: Jugador)-> str:
        res_ruleta = random.choice(self.valores_ruleta)
        return res_ruleta

    def letra_en_frase(self,letra: str)-> bool:
        if letra in self.frase_juego:
            return True
        else:
            return False
