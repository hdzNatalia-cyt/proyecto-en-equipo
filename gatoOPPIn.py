import tkinter as tk
from tkinter import messagebox

class JuegoDelGato:
    def __init__(self, master_ventana):
        self.master_ventana = master_ventana
        master_ventana.title("El Gato (Fácil)")
        master_ventana.geometry("340x450")
        master_ventana.resizable(False, False)
        master_ventana.configure(bg='lightgray')

        self.tablero = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
        self.jugador_actual = "X"
        self.contador_jugadas = 0
        self.juego_activo = True

        self.etiqueta_estado = tk.Label(master_ventana, text=f"Turno de: {self.jugador_actual}", font=('Arial', 16, 'bold'), bg='lightgray', fg='navy')
        self.etiqueta_estado.pack(pady=10)

        marco_tablero = tk.Frame(master_ventana, bg='darkgray', bd=3, relief='raised')
        marco_tablero.pack(pady=5)

        self.botones_del_juego = []

        for fila in range(3):
            for columna in range(3):
                boton = tk.Button(marco_tablero, text="", font=('Arial', 30, 'bold'),width=3, height=1, bg='white', fg='black')

                if fila == 0 and columna == 0:
                    boton.config(command=self.hacer_jugada_0_0)
                elif fila == 0 and columna == 1:
                    boton.config(command=self.hacer_jugada_0_1)
                elif fila == 0 and columna == 2:
                    boton.config(command=self.hacer_jugada_0_2)
                elif fila == 1 and columna == 0:
                    boton.config(command=self.hacer_jugada_1_0)
                elif fila == 1 and columna == 1:
                    boton.config(command=self.hacer_jugada_1_1)
                elif fila == 1 and columna == 2:
                    boton.config(command=self.hacer_jugada_1_2)
                elif fila == 2 and columna == 0:
                    boton.config(command=self.hacer_jugada_2_0)
                elif fila == 2 and columna == 1:
                    boton.config(command=self.hacer_jugada_2_1)
                elif fila == 2 and columna == 2:
                    boton.config(command=self.hacer_jugada_2_2)

                boton.grid(row=fila, column=columna, padx=4, pady=4)
                self.botones_del_juego.append(boton)

        self.boton_reiniciar = tk.Button(master_ventana, text="Reiniciar Juego", font=('Arial', 12), bg='skyblue', fg='white',command=self.reiniciar_juego)
        self.boton_reiniciar.pack(pady=15)


    def hacer_jugada_0_0(self):
        self.manejar_clic(0, 0)

    def hacer_jugada_0_1(self):
        self.manejar_clic(0, 1)

    def hacer_jugada_0_2(self):
        self.manejar_clic(0, 2)

    def hacer_jugada_1_0(self):
        self.manejar_clic(1, 0)

    def hacer_jugada_1_1(self):
        self.manejar_clic(1, 1)

    def hacer_jugada_1_2(self):
        self.manejar_clic(1, 2)

    def hacer_jugada_2_0(self):
        self.manejar_clic(2, 0)

    def hacer_jugada_2_1(self):
        self.manejar_clic(2, 1)

    def hacer_jugada_2_2(self):
        self.manejar_clic(2, 2)

    def manejar_clic(self, fila, columna):
        if not self.juego_activo:
            messagebox.showinfo("Juego Terminado", "¡Haz clic en 'Reiniciar Juego' para volver a jugar!")
            return

        indice_del_boton = fila * 3 + columna
        boton_actual = self.botones_del_juego[indice_del_boton]

        if self.tablero[fila][columna] == "":
            self.tablero[fila][columna] = self.jugador_actual
            boton_actual.config(text=self.jugador_actual, state=tk.DISABLED)
            self.contador_jugadas += 1

            self.verificar_final_del_juego()

            if self.juego_activo:
                if self.jugador_actual == "X":
                    self.jugador_actual = "O"
                else:
                    self.jugador_actual = "X"
                self.etiqueta_estado.config(text=f"Turno de: {self.jugador_actual}")
        else:
            messagebox.showwarning("Casilla Ocupada", "¡Esa casilla ya está ocupada! Elige otra.")

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
                self.etiqueta_estado.config(text=f"¡GANÓ: {self.jugador_actual}!", fg='green')
                messagebox.showinfo("Juego Terminado", f"¡El jugador {self.jugador_actual} ha ganado!")
                self.deshabilitar_todos_los_botones()
                self.juego_activo = False
                return

        if self.contador_jugadas == 9:
            self.etiqueta_estado.config(text="¡EMPATE!", fg='orange')
            messagebox.showinfo("Juego Terminado", "¡Es un empate!")
            self.deshabilitar_todos_los_botones()
            self.juego_activo = False

    def deshabilitar_todos_los_botones(self):
        for boton in self.botones_del_juego:
            boton.config(state=tk.DISABLED)

    def reiniciar_juego(self):
        self.tablero = [["" for _ in range(3)] for _ in range(3)]
        self.jugador_actual = "X"
        self.contador_jugadas = 0
        self.juego_activo = True
        self.etiqueta_estado.config(text=f"Turno de: {self.jugador_actual}", fg='navy')

        for boton in self.botones_del_juego:
            boton.config(text="", state=tk.NORMAL, bg='white', fg='black')


if __name__ == "__main__":
    ventana_principal = tk.Tk()
    mi_juego_del_gato = JuegoDelGato(ventana_principal)
    ventana_principal.mainloop()
