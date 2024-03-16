import random

class Tablero:
    pista = ""
    # En el constructor se asigna la frase a ser adivinada segun la dificultad aleatoria que fue generada en la clase juego
    def __init__(self, nivel_dificultad: str):
        try:
            self.frase_juego, self.pista = self.leer_frase_desde_archivo(nivel_dificultad)
            self.frase_revelada = "".join([letra if not letra.isalpha()  else "_" for letra in self.frase_juego])
            self.letras_usadas = set()
        except Exception as e:
            raise Exception(f"Error al inicializar el tablero: {e}")

    # Funcion que lee las frases del fichero
    def leer_frase_desde_archivo(self, nivel_dificultad: str) -> tuple:
        try:
            with open('frases.txt', 'r') as file:
                frases_por_dificultad = {
                    'bajo': [],
                    'medio': [],
                    'alto': []
                }
                for line in file:
                    dificultad, frase, pista = line.strip().split('|')
                    frases_por_dificultad[dificultad].append((frase.upper(), pista))
                
                return random.choice(frases_por_dificultad[nivel_dificultad])
        except Exception as e:
            raise Exception(f"Error al leer las frases desde el archivo: {e}")

    # Funcion que muestra en pantalla las letras que han sido adivinadas
    def mostrar_tablero(self) -> str:
        try:
            if not Tablero.pista:
                Tablero.pista = self.pista
            letras_reveladas = " ".join([letra if letra in self.letras_usadas or letra == " " else "_" for letra in self.frase_juego])
            letras_usadas_str = ", ".join(sorted(self.letras_usadas))
            return f"Pista: {self.pista}\nLetras usadas: {letras_usadas_str}\nTablero: {letras_reveladas}"
        except Exception as e:
            raise Exception(f"Error al mostrar el tablero: {e}")
        
     # Funcion que determina si la letra ingresada por el jugador se encuentra dentro de la frase a adinivar y agrega a un arreglo todas las letras usadas
    def letra_en_frase(self, letra: str) -> bool:
        try:
            self.letras_usadas.add(letra)
            return letra.upper() in self.frase_juego
        except Exception as e:
            raise Exception(f"Error al verificar la letra en la frase: {e}")

    # Funcion que luego de que una letra se ha encontrado dentro de la frase, cuenta la cantidad de veces que esta para aplicar el premio generado por la ruleta
    def cantidad_letras(self, letra: str) -> int:
        try:
            return int(self.frase_juego.count(letra))
        except Exception as e:
            raise Exception(f"Error al contar la cantidad de letras: {e}")

    # Funcion que actualiza el estado del tablero
    def actualizar_tablero(self, letra: str) -> None:
        try:
            letra = letra.upper()
            nueva_frase = ""
            for letra_actual, letra_revelada in zip(self.frase_juego, self.frase_revelada):
                if letra_actual == letra:
                    nueva_frase += letra_actual
                else:
                    nueva_frase += letra_revelada
            self.frase_revelada = nueva_frase
        except Exception as e:
            raise Exception(f"Error al actualizar el tablero: {e}")

    # Funcion que determina si la frase ha sido adivinada
    def frase_completa(self) -> bool:
        try:
            return self.frase_juego == self.frase_revelada
        except Exception as e:
            raise Exception(f"Error al verificar si la frase está completa: {e}")
