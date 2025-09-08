import tkinter as tk
import time

def mostrar_hora():
    hora_atual = time.strftime('%H:%M:%S')
    texto.config(text= hora_atual)
    janela.after(1000, mostrar_hora)

janela = tk.Tk()
janela.title('Mundial Clock ⌚')
janela.geometry('250x100')
janela.configure(bg= 'black')

texto = tk.Label(janela, font= ('Courier', 40), bg= 'black', fg= 'white')
texto.pack(anchor= 'center')

mostrar_hora()

janela.mainloop()