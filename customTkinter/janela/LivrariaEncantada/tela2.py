import customtkinter as tk
from Modulos import *

def MostrarTelaVendas():
    janela3.deiconify()

def AbrirNavegacao():
    janela3.withdraw()
    from navegacao import MostrarTelaNavegacao
    MostrarTelaNavegacao()


janela3 = CriarJanela('Registro de Vendas','500x600+550+40',2)
janela3.configure(fg_color='#f4efec')

#--------------------INFORMÇÕES LIVROS----------
abas = CriarAbas(janela3,1,6,350,450,'Informações do livro','Informações adicionais')

#Titulo----------------------
LB_titulo = CriarLabel(abas.tab('Informações do livro'),'Titulo',2,6)
LB_titulo.grid(sticky = "S")
CX_titulo = CriarCaixaDeTexto(abas.tab("Informações do livro"),150,30,3,6)
CX_titulo.grid(sticky = "S")

#Autor-----------------------
LB_autor = CriarLabel(abas.tab('Informações do livro'),'Autor',4,6)
LB_autor.grid(sticky = "S")
CX_autor = CriarCaixaDeTexto(abas.tab("Informações do livro"),150,30,5,6)
CX_autor.grid(sticky = "S")

#Quantidade------------------
LB_quantidade = CriarLabel(abas.tab('Informações do livro'),'Quantidade Vendida',6,6)
LB_quantidade.grid(sticky = "S")
CX_quantidade = CriarCaixaDeTexto(abas.tab("Informações do livro"),150,30,7,6)
CX_quantidade.grid(sticky = "S")

#Preço-----------------------
LB_preco = CriarLabel(abas.tab('Informações do livro'),'Preço',8,6)
LB_preco.grid(sticky = "S")
CX_preco = CriarCaixaDeTexto(abas.tab("Informações do livro"),150,30,9,6, Modo='Moeda')
CX_preco.grid(sticky = "S")

#--------------------INFORMÇÕES ADICIONAIS----------
#Numero caixa----------------
LB_caixa = CriarLabel(abas.tab('Informações adicionais'),'Numero do caixa',2,6)
LB_caixa.grid(sticky = "S")
CX_caixa = CriarCaixaDeTexto(abas.tab("Informações adicionais"),150,30,3,6)
CX_caixa.grid(sticky = "S")

#Nome funcionario------------
LB_funcionario = CriarLabel(abas.tab('Informações adicionais'),'Nome do Funcionario',4,6)
LB_funcionario.grid(sticky = "S")
CX_funcionario = CriarCaixaDeTexto(abas.tab("Informações adicionais"),150,30,5,6)
CX_funcionario.grid(sticky = "S")

#Data------------------------
LB_data = CriarLabel(abas.tab('Informações adicionais'),'Data',6,6)
LB_data.grid(sticky = "S")
CX_data = CriarCaixaDeTexto(abas.tab("Informações adicionais"),150,30,7,6, Modo='Data')
CX_data.grid(sticky = "S")

#Hora------------------------
LB_hora = CriarLabel(abas.tab('Informações adicionais'),'Data',8,6)
LB_hora.grid(sticky = "S")
CX_hora = CriarCaixaDeTexto(abas.tab("Informações adicionais"),150,30,9,6, Modo='Hora')
CX_hora.grid(sticky = "S")

#-------------------------BOTOESS-------------------
btn_Volar = CriarBotão(janela3,'Voltar',AbrirNavegacao,6,6,100,30)

janela3.mainloop()
