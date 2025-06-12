class JuegoDelGato:
    def __init__(self):
        self.tablero = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]
        self.jugador_actual = "X"
        self.contador_jugadas = 0
        self.juego_activo = True

    def mostrar_tablero(self):
        print("\n-------------")
        for fila in range(3):
            print(f"| {self.tablero[fila][0]} | {self.tablero[fila][1]} | {self.tablero[fila][2]} |")
            print("-------------")

    def hacer_jugada(self, numero_casilla):
        if not self.juego_activo:
            print("¡Juego Terminado! Inicia uno nuevo.")
            return

        fila = (numero_casilla - 1) // 3
        columna = (numero_casilla - 1) % 3

        if self.tablero[fila][columna] != "X" and self.tablero[fila][columna] != "O":
            self.tablero[fila][columna] = self.jugador_actual
            self.contador_jugadas += 1

            self.verificar_final_del_juego()

            if self.juego_activo:
                if self.jugador_actual == "X":
                    self.jugador_actual = "O"
                else:
                    self.jugador_actual = "X"
        else:
            print("¡Esa casilla ya está ocupada o no es válida! Elige otra.")


    def verificar_final_del_juego(self):
        lineas_ganadoras = [
            [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]
        ]

        for linea in lineas_ganadoras:
            (r1, c1), (r2, c2), (r3, c3) = linea

            if (self.tablero[r1][c1] == self.jugador_actual and
                    self.tablero[r2][c2] == self.jugador_actual and
                    self.tablero[r3][c3] == self.jugador_actual):

                self.mostrar_tablero()
                print(f"¡GANÓ: {self.jugador_actual}!")
                self.juego_activo = False
                return

        if self.contador_jugadas == 9:
            self.mostrar_tablero()
            print("¡Es un empate! Nadie ganó.")
            self.juego_activo = False

    def reiniciar_juego(self):
        self.tablero = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]
        self.jugador_actual = "X"
        self.contador_jugadas = 0
        self.juego_activo = True
        print("\n--- ¡Juego Reiniciado! ---")

if __name__ == "__main__":
    mi_juego_del_gato = JuegoDelGato()

    while mi_juego_del_gato.juego_activo:
        mi_juego_del_gato.mostrar_tablero()
        print(f"Es el turno de {mi_juego_del_gato.jugador_actual}.")

        try:
            eleccion = int(input("Elige un número de casilla (1-9): "))
            if not (1 <= eleccion <= 9):
                print("Por favor, ingresa un número entre 1 y 9.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")
            continue

        mi_juego_del_gato.hacer_jugada(eleccion)

        if not mi_juego_del_gato.juego_activo:
            respuesta = input("¿Quieres jugar de nuevo? (s/n): ").lower()
            if respuesta == 's':
                mi_juego_del_gato.reiniciar_juego()
            else:
                print("¡Gracias por jugar! Adiós.")
                break