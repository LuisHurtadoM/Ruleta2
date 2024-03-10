from jugador import Jugador
from ruleta import Ruleta
from tablero import Tablero
import random

class Juego:
    categoria = ["Bajo", "Medio", "Alto"]
    veces_aparece_letra = 1

    def __init__(self, jugadores: list[Jugador], ruleta: Ruleta, tablero: Tablero):
        self.jugadores = jugadores
        self.ruleta = ruleta
        self.tablero = tablero
        
        self.indice_jugador_actual = 0

    def asignar_turnos(self):
        for jugador in self.jugadores:
            print(f"Girando la ruleta para determinar el turno de {jugador.nombre}...")
            premio = self.ruleta.girar_ruleta(jugador)  # Realiza el primer giro de la ruleta
            jugador.premio_inicial = premio  # Guarda el premio inicial obtenido por el jugador
        self.jugadores.sort(key=lambda jugador: jugador.premio_inicial, reverse=True)  # Ordena los jugadores por premio
        print("Orden de los turnos:")
        for i, jugador in enumerate(self.jugadores, start=1):
            print(f"{i}. {jugador.nombre}")
        
        print(f"{self.tablero.pista}")
    

    def mostrar_orden_turnos(self):
        print("Orden de los turnos:")
        for i, jugador in enumerate(self.jugadores, start=1):
            print(f"{i}. {jugador.nombre}")

    """ def categoria_juego(self)-> str:
        return random.choice(self.categoria) """

  
    def comprar_vocal(self, jugador: Jugador, letra: str):
        costo_vocal = 100  # Costo de comprar una vocal

        if jugador.saldo >= costo_vocal:
            vocal = letra.upper()
            if vocal in 'AEIOU':
                jugador.saldo -= costo_vocal
                print(f"{jugador.nombre} ha comprado la vocal '{vocal}'.")
            else:
                print("No es una vocal válida.")
                return False
        else:
            print("Saldo insuficiente para comprar una vocal.")
            return False
        return True

    def cambiar_turno(self):
        self.indice_jugador_actual = (self.indice_jugador_actual + 1) % len(self.jugadores)

    def jugar(self):
        while not self.tablero.frase_completa() and any(jugador.saldo > 0 for jugador in self.jugadores):
            jugador = self.jugadores[self.indice_jugador_actual]

            """ if jugador.saldo <= 0:
                self.cambiar_turno()
                continue """

            print(f"Turno de {jugador.nombre}:")
            # Girar la ruleta y obtener el premio o penalización
            premio = self.ruleta.girar_ruleta(jugador)
            print(f"La ruleta ha dado como resultado: {premio}")

            if premio in ['Quiebra', 'Pierde turno']:
                print(f"{jugador.nombre} ha obtenido '{premio}'. Pasando al siguiente jugador.")
                self.cambiar_turno()
                continue

            """ if premio == 'Comodin':
                self.cambiar_turno()  # Pasar al siguiente jugador sin realizar más acciones en el turno actual
                continue """

            letra = input("Elige una letra: ").upper()

            if letra in 'AEIOU':
                print("Deseas entonces comprar una vocal") # Si es una vocal, intentar comprarla
                if not self.comprar_vocal(jugador,letra):
                    # Si no se pudo comprar, verificar si el jugador tiene comodines disponibles
                    if jugador.comodines_disponibles > 0:
                        usar_comodin = input(f"{jugador.nombre}, ¿quieres usar un comodín? (S/N): ").upper()
                        if usar_comodin == 'S':
                            if jugador.usar_comodin():
                                # Si se utilizó un comodín con éxito, se decrementa el número de comodines disponibles
                                continue
                    # Si no tiene comodines disponibles o decide no usarlos, pasar al siguiente jugador
                    self.cambiar_turno()
                    continue

            # Verificar si la letra ya ha sido usada
            if letra in self.tablero.letras_usadas:
                print("Esa letra ya ha sido usada. Elige otra.")
                continue

            # Verificar si la letra está en la frase y actualizar el tablero
            if self.tablero.letra_en_frase(letra):
                veces_aparece_letra = int(self.tablero.cantidad_letras(letra))
                self.tablero.actualizar_tablero(letra)  # Llamada para actualizar el tablero
                print(f"¡Bien hecho! {letra} está en la frase.")
            else:
                print(f"{letra} no está en la frase.")
                self.cambiar_turno()
                # Pasar al siguiente jugador si la letra no está en la frase y no es una vocal
                if letra in 'AEIOU':
                    print("Letra incorrecta. Pasando al siguiente jugador.")
                    self.cambiar_turno()
                    continue

            # Aplicar premio o penalización al jugador
            jugador.aplicar_premio(premio,veces_aparece_letra)
            # Mostrar el estado actual del tablero y el saldo del jugador
            print(self.tablero.mostrar_tablero())
            print(f"Saldo actual de {jugador.nombre}: {jugador.saldo}")
            print("-------------------------------------------")

            # Si el premio no es 'Pierde turno' o 'Quiebra', pasamos al siguiente jugador
            if premio in ['Pierde turno', 'Quiebra']:
                self.cambiar_turno()

        if self.tablero.frase_completa():
            print("¡Felicidades! ¡La frase ha sido completada!")
        elif all(jugador.saldo <= 0 for jugador in self.jugadores):
            print("Todos los jugadores están fuera de saldo. El juego ha terminado.")

if __name__ == "__main__":
    # Crear jugadores, ruleta y tablero
    jugador1 = Jugador("Luis")
    jugador2 = Jugador("Aura")
    jugador3 = Jugador("Rodolfo")
    jugador4 = Jugador("Alexandra")
    jugadores = [jugador1, jugador2, jugador3, jugador4]
    ruleta = Ruleta()
    nivel = random.choice(["bajo", "medio", "alto"])
    tablero = Tablero(nivel)
    juego = Juego(jugadores, ruleta, tablero)
    juego.asignar_turnos()
    juego.jugar()
