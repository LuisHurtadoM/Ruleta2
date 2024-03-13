# Clase Modelo: Jugador
class Jugador:
    def __init__(self, nombre: str, saldo: int = 200):
        self.nombre = nombre
        self.saldo = saldo
        self.comodines_disponibles = 0

    def usar_comodin(self):
        if self.comodines_disponibles > 0:
            self.comodines_disponibles -= 1
            print(f"{self.nombre} ha utilizado un comodín para seguir jugando.")
            return True
        else:
            print("No tienes comodines disponibles.")
            return False

    def recibir_comodin(self, cantidad: int):
        self.comodines_disponibles += cantidad

    def aplicar_premio(self, premio: str, veces_aparece_letra: int = 1) -> None:
        if premio == "X2":
            self.saldo *= 2 * veces_aparece_letra
        elif premio == "Quiebra":
            self.saldo = 0
        elif premio == "1/2":
            self.saldo //= 2
        elif premio == "Comodin":
            pass
        else:
            self.saldo += int(premio) * veces_aparece_letra

# Clase Modelo: Ruleta
class Ruleta:
    def __init__(self):
        self.valores_ruleta = ["Pierde turno", "Quiebra", "X2", "1/2", "Comodin", "50", "150", "200", "50", "150",
                               "200", "50", "150", "200"]

    def girar_ruleta(self, jugador) -> str:
        resultado = random.choice(self.valores_ruleta)

        if resultado == "Comodin":
            jugador.recibir_comodin(1)
            return "Comodin"

        return resultado

# Clase Modelo: Tablero
class Tablero:
    pista = ""

    def __init__(self, nivel_dificultad: str):
        self.frase_juego, self.pista = self.leer_frase_desde_archivo(nivel_dificultad)
        self.frase_revelada = "".join([letra if not letra.isalpha() else "_" for letra in self.frase_juego])
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
        letras_reveladas = " ".join([letra if letra in self.letras_usadas or letra == " " else "_"
                                     for letra in self.frase_juego])
        letras_usadas_str = ", ".join(sorted(self.letras_usadas))
        return f"Pista: {self.pista}\nLetras usadas: {letras_usadas_str}\nTablero: {letras_reveladas}"

    def letra_en_frase(self, letra: str) -> bool:
        self.letras_usadas.add(letra)
        return letra.upper() in self.frase_juego

    def cantidad_letras(self, letra: str) -> int:
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

# Clase Controlador: Juego
class Juego:
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

            letra = jugador.elegir_letra()

            if letra in 'AEIOU':
                print("Deseas entonces comprar una vocal")
                if not self.comprar_vocal(jugador, letra):

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

            jugador.aplicar_premio(premio, veces_aparece_letra)

            print(self.tablero.mostrar_tablero())
            print(f"Saldo actual de {jugador.nombre}: {jugador.saldo}")
            print("-------------------------------------------")

            if premio in ['Pierde turno', 'Quiebra']:
                self.cambiar_turno()

        if self.tablero.frase_completa():
            print("¡Felicidades! ¡La frase ha sido completada!")
        elif all(jugador.saldo <= 0 for jugador in self.jugadores):
            print("Todos los jugadores están fuera de saldo. El juego ha terminado.")

# Código de inicio del juego
if __name__ == "__main__":
    import random

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
#=============================================================
class Vista:
    @staticmethod
    def mostrar_turno(jugador_nombre: str):
        print(f"Turno de {jugador_nombre}:")
    
    @staticmethod
    def mostrar_resultado_ruleta(resultado: str):
        print(f"La ruleta ha dado como resultado: {resultado}")

    @staticmethod
    def mostrar_vocal_comprada(jugador_nombre: str, vocal: str):
        print(f"{jugador_nombre} ha comprado la vocal '{vocal}'.")

    @staticmethod
    def mostrar_letra_no_valida():
        print("No es una vocal válida.")

    # Otros métodos para mostrar información al usuario según sea necesario...

# Dentro de la clase Juego, en lugar de imprimir directamente, utilizaríamos métodos de la clase Vista para mostrar información al usuario
class Juego:
    def __init__(self, jugadores: list[Jugador], ruleta: Ruleta, tablero: Tablero):
        self.jugadores = jugadores
        self.ruleta = ruleta
        self.tablero = tablero
        self.indice_jugador_actual = 0
        self.vista = Vista()

    def jugar(self):
        while not self.tablero.frase_completa() and any(jugador.saldo > 0 for jugador in self.jugadores):
            jugador = self.jugadores[self.indice_jugador_actual]
            self.vista.mostrar_turno(jugador.nombre)

            premio = self.ruleta.girar_ruleta(jugador)
            self.vista.mostrar_resultado_ruleta(premio)
            
            # Resto del código...
