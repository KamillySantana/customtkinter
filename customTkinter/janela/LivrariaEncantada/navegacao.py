import customtkinter as tk
from Modulos import *

def MostrarTelaNavegacao():
    janela2.deiconify()

def Vendas():
    janela2.withdraw()
    from tela2 import MostrarTelaVendas
    MostrarTelaVendas()

def Estoque():
    janela2.withdraw()
    from tela3 import MostrarTelaEstoque
    MostrarTelaEstoque()

janela2 = CriarJanela('Tela de Navegação','500x600+550+40',2)

#--------BOTAO----------
btn_vendas = CriarBotão(janela2,'Registro de vendas',Vendas,5,6,100,40)
btn_estoque = CriarBotão(janela2,'Estoque de Livros',Estoque,6,6,100,40)

#---------design--------
janela2.configure(fg_color='#BA6C6C')
btn_vendas.configure(fg_color='#FFC0CB',hover_color='#CB8E8E',text_color='black')
btn_estoque.configure(fg_color='#FFC0CB',hover_color='#CB8E8E',text_color='black')



