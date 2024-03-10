import random

class Tablero:
    pista = ""

    def __init__(self, nivel_dificultad: str):
        self.frase_juego, self.pista = self.leer_frase_desde_archivo(nivel_dificultad)
        self.frase_revelada = "_" * len(self.frase_juego)
        self.letras_usadas = set()

    def leer_frase_desde_archivo(self, nivel_dificultad: str) -> tuple:
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

    def mostrar_tablero(self) -> str:
        if not Tablero.pista:
            Tablero.pista = self.pista
        letras_reveladas = " ".join([letra if letra in self.letras_usadas else "_" for letra in self.frase_juego])
        letras_usadas_str = ", ".join(sorted(self.letras_usadas))
        return f"Pista: {Tablero.pista}\nLetras usadas: {letras_usadas_str}\nTablero: {letras_reveladas}"

    def letra_en_frase(self, letra: str) -> bool:
        self.letras_usadas.add(letra)
        return letra.upper() in self.frase_juego

    def cantidad_letras(self, letra: str)-> int:
        return int(self.frase_juego.count(letra))

    def actualizar_tablero(self, letra: str) -> None:
        letra = letra.upper()
        nueva_frase = ""
        for letra_actual, letra_revelada in zip(self.frase_juego, self.frase_revelada):
            if letra_actual == letra:
                nueva_frase += letra_actual
            else:
                nueva_frase += letra_revelada
        self.frase_revelada = nueva_frase

    def frase_completa(self) -> bool:
        return self.frase_juego == self.frase_revelada
