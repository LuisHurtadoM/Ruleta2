from jugador import Jugador
from ruleta import Ruleta
from tablero import Tablero
import random

# Clase que gestiona el juego en su generalidad.
class Juego:
    
    veces_aparece_letra = 1

    def __init__(self, jugadores: list[Jugador], ruleta: Ruleta, tablero: Tablero):
        self.jugadores = jugadores
        self.ruleta = ruleta
        self.tablero = tablero
        
        self.indice_jugador_actual = 0

    def asignar_turnos(self):
        for jugador in self.jugadores:
            print(f"Girando la ruleta para determinar el turno de {jugador.nombre}...")
            premio = self.ruleta.girar_ruleta(jugador)  
            jugador.premio_inicial = premio  
        self.jugadores.sort(key=lambda jugador: jugador.premio_inicial, reverse=True) 
        print("Orden de los turnos:")
        for i, jugador in enumerate(self.jugadores, start=1):
            print(f"{i}. {jugador.nombre}")
        
        print(f"{self.tablero.pista}")
    
    # Funcion que saca por pantalla el orden en el que los jugadores han quedado y jugaran
    def mostrar_orden_turnos(self):
        print("Orden de los turnos:")
        for i, jugador in enumerate(self.jugadores, start=1):
            print(f"{i}. {jugador.nombre}")

    def comprar_vocal(self, jugador: Jugador, letra: str):
        costo_vocal = 100  

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

    # Funcion que gestiona los cambios de turno que se pueden dar por distintas razones
    def cambiar_turno(self):
        self.indice_jugador_actual = (self.indice_jugador_actual + 1) % len(self.jugadores)

    def jugar(self):
        
        while not self.tablero.frase_completa() and any(jugador.saldo > 0 for jugador in self.jugadores):
            jugador = self.jugadores[self.indice_jugador_actual]

            print(f"Turno de {jugador.nombre}:")
            
            premio = self.ruleta.girar_ruleta(jugador)
            print(f"La ruleta ha dado como resultado: {premio}")

            if premio in ['Quiebra', 'Pierde turno']:
                print(f"{jugador.nombre} ha obtenido '{premio}'. Pasando al siguiente jugador.")
                self.cambiar_turno()
                continue

            letra = input("Elige una letra: ").upper()

            if letra in 'AEIOU':
                print("Deseas entonces comprar una vocal") 
                if not self.comprar_vocal(jugador,letra):
                   
                    if jugador.comodines_disponibles > 0:
                        usar_comodin = input(f"{jugador.nombre}, ¿quieres usar un comodín? (S/N): ").upper()
                        if usar_comodin == 'S':
                            if jugador.usar_comodin():
                                
                                continue
                    
                    self.cambiar_turno()
                    continue

            
            if letra in self.tablero.letras_usadas:
                print("Esa letra ya ha sido usada. Elige otra.")
                continue

            
            if self.tablero.letra_en_frase(letra):
                veces_aparece_letra = int(self.tablero.cantidad_letras(letra))
                self.tablero.actualizar_tablero(letra)  
                print(f"¡Bien hecho! {letra} está en la frase.")
            else:
                print(f"{letra} no está en la frase.")
                self.cambiar_turno()
                
                if letra in 'AEIOU':
                    print("Letra incorrecta. Pasando al siguiente jugador.")
                    self.cambiar_turno()
                    continue

            
            jugador.aplicar_premio(premio,veces_aparece_letra)
            
            print(self.tablero.mostrar_tablero())
            print(f"Saldo actual de {jugador.nombre}: {jugador.saldo}")
            print("-------------------------------------------")


            if premio in ['Pierde turno', 'Quiebra']:
                self.cambiar_turno()

        if self.tablero.frase_completa():
            print("¡Felicidades! ¡La frase ha sido completada!")
        elif all(jugador.saldo <= 0 for jugador in self.jugadores):
            print("Todos los jugadores están fuera de saldo. El juego ha terminado.")

if __name__ == "__main__":
   
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
