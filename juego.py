from jugador import Jugador
from ruleta import Ruleta
from tablero import Tablero
import random

class Juego:
    def __init__(self, jugadores: list[Jugador], ruleta: Ruleta, tablero: Tablero):
        self.jugadores = jugadores
        self.ruleta = ruleta
        self.tablero = tablero
        self.categoria = [1, 2, 3]

    def categoria_juego(self):
        res_categoria = random.choice(self.categoria)
        return res_categoria

    def jugar(self):
        while not self.tablero.frase_completa() and any(jugador.saldo > 0 for jugador in self.jugadores):
            for jugador in self.jugadores:
                if jugador.saldo <= 0:
                    continue
                
                print(f"Turno de {jugador.nombre}:")
                # Girar la ruleta y obtener el premio o penalización
                premio = self.ruleta.girar_ruleta(jugador)
                print(f"La ruleta ha dado como resultado: {premio}")

                # Si el premio es 'Pierde turno' o 'Quiebra', pasamos al siguiente jugador
                if premio in ['Pierde turno', 'Quiebra']:
                    print(f"{jugador.nombre} ha obtenido '{premio}'. Pasando al siguiente jugador.")
                    continue

                letra = input("Elige una letra: ").upper()
                # Verificar si la letra ya ha sido usada
                if letra in self.tablero.letras_usadas:
                    print("Esa letra ya ha sido usada. Elige otra.")
                    continue
                
                # Verificar si la letra está en la frase y actualizar el tablero
                if self.tablero.letra_en_frase(letra):
                    self.tablero.actualizar_tablero(letra)
                    print(f"¡Bien hecho! {letra} está en la frase.")
                else:
                    print(f"{letra} no está en la frase.")
                # Aplicar premio o penalización al jugador
                jugador.aplicar_premio(premio)
                # Mostrar el estado actual del tablero y el saldo del jugador
                print(f"Tablero actual: {self.tablero.mostrar_tablero()}")
                print(f"Saldo actual de {jugador.nombre}: {jugador.saldo}")
                print("-------------------------------------------")

                # Si el premio no es 'Pierde turno' o 'Quiebra', pasamos al siguiente jugador
                if premio not in ['Pierde turno', 'Quiebra']:
                    break

            if self.tablero.frase_completa():
                print("¡Felicidades! ¡La frase ha sido completada!")
                break

            if all(jugador.saldo <= 0 for jugador in self.jugadores):
                print("Todos los jugadores están fuera de saldo. El juego ha terminado.")
                break

# En el bloque __main__
if __name__ == "__main__":
    # Crear jugadores, ruleta y tablero
    jugador1 = Jugador("Luis")
    jugador2 = Jugador("Aura")
    jugador3 = Jugador("Rodolfo")
    jugador4 = Jugador("Alexandra")
    jugadores = [jugador1, jugador2, jugador3, jugador4]
    ruleta = Ruleta(random.choice([1, 2, 3]))
    tablero = Tablero("Colombianisimo")

    # Crear y jugar el juego
    juego = Juego(jugadores, ruleta, tablero)
    juego.jugar()
