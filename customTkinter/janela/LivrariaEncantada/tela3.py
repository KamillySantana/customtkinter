import customtkinter as tk
from Modulos import *

def MostrarTelaEstoque():
    janela4.deiconify()

def AbrirNavegacao():
    janela4.withdraw()
    from navegacao import MostrarTelaNavegacao
    MostrarTelaNavegacao()

janela4 = CriarJanela('Estoque de Livros','500x600+550+40',2)
janela4.configure(fg_color='#f4efec')

#----------Botao Voltar---------
btn_Volar = CriarBotão(janela4,'Voltar',AbrirNavegacao,1,6,100,30)