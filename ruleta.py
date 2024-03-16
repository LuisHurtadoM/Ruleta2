import random
from jugador import Jugador

class Ruleta:

    # Inicializa la ruleta con los valores posibles de los premios.

    def __init__(self):
        self.valores_ruleta = ["Pierde turno", "Quiebra", "X2", "1/2", "Comodin", "50", "150", "200", "50", "150", "200", "50", "150", "200"]
      
       
    # Simula el giro de la ruleta y devuelve el premio obtenido.    
        
    def girar_ruleta(self, jugador) -> str:
         
        
        try:
            resultado = random.choice(self.valores_ruleta)
        
            if resultado == "Comodin":
                jugador.recibir_comodin(1)  
                
                return "Comodin"
            
            return resultado
        except Exception as e:
            raise Exception(f"Error al girar la ruleta: {e}")
