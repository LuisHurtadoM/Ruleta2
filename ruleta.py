import random
from jugador import Jugador

import random

class Ruleta:
    def __init__(self, categoria: int):
        self.valores_ruleta = ["Pierde turno", "Quiebra", "X2", "1/2", "Comodin", "50", "150", "200", "50", "150", "200", "50", "150", "200"]

    def girar_ruleta(self, jugador) -> str:
        resultado = random.choice(self.valores_ruleta)
        
        # Si el resultado es "Comodin", entonces el jugador puede elegir otro valor
        if resultado == "Comodin":
            nuevo_valor = input("La ruleta ha dado como resultado 'Comodin'. Elige otro valor (50, 150, 200): ")
            while nuevo_valor not in ["50", "150", "200"]:
                nuevo_valor = input("Valor no válido. Por favor, elige entre 50, 150 o 200: ")
            resultado = nuevo_valor
        
        # Si el resultado es "X2", "1/2" o un valor numérico, se convierte a int
        if resultado in ["X2", "1/2", "50", "150", "200"]:
            resultado = (resultado)

        return resultado
