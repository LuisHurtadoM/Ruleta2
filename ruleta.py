import random
from jugador import Jugador

import random


class Ruleta:
    def __init__(self):
        self.valores_ruleta = ["Pierde turno", "Quiebra", "X2", "1/2", "Comodin", "50", "150", "200", "50", "150", "200", "50", "150", "200"]

    def girar_ruleta(self, jugador) -> str:
        resultado = random.choice(self.valores_ruleta)
        
        # Si el resultado es "Comodin", se le entrega un comodín al jugador y se permite seguir jugando
        if resultado == "Comodin":
            jugador.recibir_comodin(1)  # Se le entrega un comodín al jugador
            
            return "Comodin"
        
        

        return resultado

