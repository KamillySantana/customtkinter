import customtkinter as tk
from Modulos import *

def MostrarTelaNavegacao():
    janela2.deiconify()

def Vendas():
    from tela2 import MostrarTelaVendas
    janela2.withdraw()
    MostrarTelaVendas()

def Estoque():
    from tela3 import MostrarTelaEstoque
    janela2.withdraw()
    MostrarTelaEstoque()

janela2 = CriarJanela('Tela de Navegação','500x600',2)
janela2.configure(fg_color='#f4efec')

#--------BOTAO
btn_vendas = CriarBotão(janela2,'Registro de vendas',Vendas,5,6,100,30)
btn_estoque = CriarBotão(janela2,'Estoque de Livros',Estoque,6,6,100,30)

