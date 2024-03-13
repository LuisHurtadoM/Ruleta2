import random
from jugador import Jugador

import random


class Ruleta:
    def __init__(self):
        self.valores_ruleta = ["Pierde turno", "Quiebra", "X2", "1/2", "Comodin", "50", "150", "200", "50", "150", "200", "50", "150", "200"]

    def girar_ruleta(self, jugador) -> str:
        resultado = random.choice(self.valores_ruleta)
        
        if resultado == "Comodin":
            jugador.recibir_comodin(1)  
            
            return "Comodin"
        
        return resultado

