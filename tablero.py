class Tablero:
    frase_revelada : str
    letras_usadas : list [str]
    estado_tablero: bool

    def __init__(self,frase_juego:str):
        self.frase_revelada = frase_juego
        self.letras_usadas = []
        self.estado_tablero = False

    def mostrar_tablero(self,letra: str) -> None:
        for i in self.frase_revelada:
            if letra in self.letras_usadas:
                print(letra)
            else :
                print("_")
