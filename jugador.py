class Jugador:

    
    # Inicializa un objeto Jugador con un nombre y un saldo inicial (por defecto 200).
        
    def __init__(self, nombre: str, saldo: int = 200):
        
        self.__nombre = nombre
        self.__saldo = saldo
        self.comodines_disponibles = 0

    @property
    def nombre(self) -> str:
        
        return self.__nombre

    @property
    def saldo(self) -> int:
        """
        Obtiene el saldo del jugador.
        """
        return self.__saldo

    # Permite modificar el saldo del jugador
    @saldo.setter
    def saldo(self, nuevo_saldo: int):
        
        try:
            if nuevo_saldo >= 0:
                self.__saldo = nuevo_saldo
            else:
                raise ValueError("El saldo no puede ser negativo.")
        except Exception as e:
            raise Exception(f"Error al modificar el saldo: {e}")

    # Permite al jugador usar un comodín si tiene disponible.
    def usar_comodin(self):
        
        try:
            if self.comodines_disponibles > 0:
                self.comodines_disponibles -= 1
                print(f"{self.__nombre} ha utilizado un comodín para seguir jugando.")
                return True  
            else:
                print("No tienes comodines disponibles.")
                return False  
        except Exception as e:
            raise Exception(f"Error al usar comodín: {e}")

    # Agrega comodines a la cuenta del jugador.
    def recibir_comodin(self, cantidad: int):
        
        try:
            if cantidad > 0:
                self.comodines_disponibles += cantidad
            else:
                raise ValueError("La cantidad de comodines debe ser positiva.")
        except Exception as e:
            raise Exception(f"Error al recibir comodines: {e}")

    # Permite al jugador elegir una letra.
    def elegir_letra(self) -> str:
        
        try:
            letra = input("Elige una letra: ").upper()
            return letra
        except Exception as e:
            raise Exception(f"Error al elegir letra: {e}")

    # Aplica el premio obtenido al saldo del jugador.
    def aplicar_premio(self, premio: str, veces_aparece_letra: int = 1) -> None:
        
        try:
            if premio == "X2":
                self.__saldo *= 2 * veces_aparece_letra
            elif premio == "Quiebra":
                self.__saldo = 0
            elif premio == "1/2":
                self.__saldo //= 2
            elif premio == "Comodin":
                pass  
            else:
                self.__saldo += int(premio) * veces_aparece_letra
        except Exception as e:
            raise Exception(f"Error al aplicar premio: {e}")
