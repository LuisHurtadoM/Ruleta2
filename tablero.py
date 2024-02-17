class Tablero:
    def __init__(self, frase_juego: str):
        self.frase_juego = frase_juego
        self.frase_revelada = "_" * len(frase_juego)
        self.letras_usadas = set()

    def mostrar_tablero(self) -> str:
        return " ".join(self.frase_revelada)

    def letra_en_frase(self, letra: str) -> bool:
        return letra in self.frase_juego

    def actualizar_tablero(self, letra: str) -> None:
        nueva_frase = ""
        for letra_actual, letra_revelada in zip(self.frase_juego, self.frase_revelada):
            if letra_actual == letra:
                nueva_frase += letra_actual
            else:
                nueva_frase += letra_revelada
        self.frase_revelada = nueva_frase

    def registrar_letra_usada(self, letra: str) -> None:
        self.letras_usadas.add(letra)

    def frase_completa(self) -> bool:
        return self.frase_juego == self.frase_revelada

