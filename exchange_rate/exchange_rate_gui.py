import requests as r
from tkinter import *

def pegar_cotacao():
    requisicao = r.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_bitcoin = requisicao_dic ['BTCBRL']['bid']
    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    Bitcoin: {cotacao_bitcoin}'''

    texto_cotacao["text"] = texto

janela = Tk()
janela.geometry('400x200')
janela.title('Cotação Atual 🪙')

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)

texto_orientacao = Label(janela, text="Clique aqui para ver a atual cotação (EURO/DOL/BIT)")
texto_orientacao.grid(column= 1, row= 0, sticky="n")

botao_cotacao = Button(janela, text="Visualizar Cotação", command=pegar_cotacao)
botao_cotacao.grid(column=1, row=1, pady=10)

texto_cotacao = Label(janela, text="")
texto_cotacao.grid(column=1, row=2)

janela.mainloop()