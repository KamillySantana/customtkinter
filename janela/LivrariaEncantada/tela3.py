import customtkinter as tk
from Modulos import *
from livrosTela3 import *


def MostrarTelaEstoque():
    janela4.deiconify()

def AbrirNavegacao():
    janela4.withdraw()
    from navegacao import MostrarTelaNavegacao
    MostrarTelaNavegacao()

janela4 = CriarJanela('Estoque de Livros','500x600+550+40',2)
abas = CriarAbas(janela4,1,6,350,450,'Livros em estoque','Adicionar Livros')

#----------Botao Voltar---------
btn_Volar = CriarBotão(janela4,'Voltar',AbrirNavegacao,9,6,100,30)

def pesquisar_livros():
    pesquisa = caixa_pesquisa.get()
    resultado = pesquisar(pesquisa)

    match resultado:
        case 'vazio':
            LB_erro2.configure(text='Não há livros registrados')
        case 'erro':
            LB_erro2.configure(text='nome do livro incorreto')
        case _:
            LB_erro2.configure(text=f'Nome: {listaLivros[resultado].nome}')
            LB_erro3 = CriarLabel(abas.tab('Livros em estoque'),f'Autor: {listaLivros[resultado].autor}',5,6)
            LB_erro4 = CriarLabel(abas.tab('Livros em estoque'),f'Quantidade: {listaLivros[resultado].qnt}',6,6)
            LB_erro5 = CriarLabel(abas.tab('Livros em estoque'),f'Preço: {listaLivros[resultado].preco}',7,6)

def adicionar_livros():
    titulo = titulo_caixa.get()
    autor = autor_caixa.get()
    qnt = qnt_caixa.get()
    preco = preco_caixa.get()

    if titulo and autor and qnt and preco:
        adicionarLivros(titulo,autor,qnt,preco)
        LB_erro.configure(text='Livro registrado!')
    else:
        LB_erro.configure(text='Obigatório prencher todos os campos')


#----------------Livros em estoque-----------
barra_pesquisa = CriarLabel(abas.tab('Livros em estoque'),'Pesquisa',1,6)
caixa_pesquisa = CriarCaixaDeTexto(abas.tab('Livros em estoque'),150,30,2,6)
btn_pesquisa = CriarBotão(abas.tab('Livros em estoque'),'Pesquisar',pesquisar_livros,3,6,100,30)

#----------------Adicionar Livros------------
titulo = CriarLabel(abas.tab('Adicionar Livros'), 'Nome:', 1, 6)
autor = CriarLabel(abas.tab('Adicionar Livros'), 'Autor:', 3, 6)
qnt = CriarLabel(abas.tab('Adicionar Livros'), 'Quantidade:', 5, 6)
preco = CriarLabel(abas.tab('Adicionar Livros'), 'Preço:', 7, 6)

titulo_caixa = CriarCaixaDeTexto(abas.tab('Adicionar Livros'), 150, 30, 2, 6)
autor_caixa = CriarCaixaDeTexto(abas.tab('Adicionar Livros'), 150, 30, 4, 6)
qnt_caixa = CriarCaixaDeTexto(abas.tab('Adicionar Livros'), 150, 30, 6, 6)
preco_caixa = CriarCaixaDeTexto(abas.tab('Adicionar Livros'), 150, 30, 8, 6,Modo='Moeda')

btn_adiL = CriarBotão(abas.tab('Adicionar Livros'),'Adicionar Livro',adicionar_livros,9,6,100,30)

#------Label de erro------------
LB_erro = CriarLabel(abas.tab('Adicionar Livros'),'',10,6)
LB_erro2 = CriarLabel(abas.tab('Livros em estoque'),'',4,6)
