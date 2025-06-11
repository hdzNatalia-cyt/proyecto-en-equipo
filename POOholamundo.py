import tkinter as tk

class saludo:
    def saludar(self, etiqueta_resultado_saludar):
        etiqueta_resultado_saludar.config(text="hola mundo")

ventana = tk.Tk()
ventana.title("hola mundo")
ventana.geometry("400x250")
ventana.configure(background='thistle')

etiqueta_resultado_saludar = tk.Label(ventana, text="", fg="black", bg="thistle", font=("Arial", 16))
etiqueta_resultado_saludar.pack(pady=20)

saludo1 = saludo()

boton_saludar = tk.Button(ventana, text="saludar", command=lambda: saludo1.saludar(etiqueta_resultado_saludar))
boton_saludar.pack()
boton_saludar.configure(highlightbackground="thistle", highlightthickness=0)

ventana.mainloop()
