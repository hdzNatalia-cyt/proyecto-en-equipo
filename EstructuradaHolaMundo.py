import tkinter as tk

def saludar(etiqueta_resultado):

    etiqueta_resultado.config(text="hola mundo")

ventana = tk.Tk()
ventana.title("Hola Mundo")
ventana.geometry("400x250")
ventana.configure(background='thistle')

etiqueta_resultado_saludar = tk.Label(ventana, text="", fg="black", bg="thistle", font=("Arial", 16))
etiqueta_resultado_saludar.pack(pady=20)

boton_saludar = tk.Button(ventana, text="saludar", command=lambda: saludar(etiqueta_resultado_saludar))
boton_saludar.pack()
boton_saludar.configure(highlightbackground="thistle", highlightthickness=0)

ventana.mainloop()
