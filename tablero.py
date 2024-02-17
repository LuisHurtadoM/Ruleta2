class Tablero:
    def __init__(self, frase_juego: str):
        self.frase_juego = frase_juego.upper()
        self.frase_revelada = "_" * len(frase_juego)
        self.letras_usadas = set()

    def mostrar_tablero(self) -> str:
        letras_reveladas = " ".join([letra if letra in self.letras_usadas else "_" for letra in self.frase_juego])
        letras_usadas_str = ", ".join(sorted(self.letras_usadas))
        return f"Letras usadas: {letras_usadas_str}\nTablero: {letras_reveladas}"

    def letra_en_frase(self, letra: str) -> bool:
        return letra.upper() in self.frase_juego

    def actualizar_tablero(self, letra: str) -> None:
        letra = letra.upper()
        nueva_frase = ""
        for letra_actual, letra_revelada in zip(self.frase_juego, self.frase_revelada):
            if letra_actual == letra:
                nueva_frase += letra_actual
            else:
                nueva_frase += letra_revelada
        self.frase_revelada = nueva_frase
        self.letras_usadas.add(letra)

    def frase_completa(self) -> bool:
        return self.frase_juego == self.frase_revelada
