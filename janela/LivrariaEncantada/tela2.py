import customtkinter as tk
from Modulos import *


def MostrarTelaVendas():
    janela3.deiconify()

def AbrirNavegacao():
    janela3.withdraw()
    from navegacao import MostrarTelaNavegacao
    MostrarTelaNavegacao()


janela3 = CriarJanela('Registro de Vendas','500x600+550+40',2)

def Proximo():
    abas.set('Informações adicionais')

def Voltar():
    abas.set('Informações do livro')

def Volts():
    abas.set('Informações adicionais')

abas = CriarAbas(janela3,1,6,350,450,'Informações do livro','Informações adicionais', 'Registrar venda')
abas.configure(state="disabled")

LB_titulo = CriarLabel(abas.tab('Informações do livro'),'Titulo',2,6)
LB_titulo.grid(sticky = "S")
CX_titulo = CriarCaixaDeTexto(abas.tab("Informações do livro"),150,30,3,6)
CX_titulo.grid(sticky = "S")

LB_autor = CriarLabel(abas.tab('Informações do livro'),'Autor',4,6)
LB_autor.grid(sticky = "S")
CX_autor = CriarCaixaDeTexto(abas.tab("Informações do livro"),150,30,5,6)
CX_autor.grid(sticky = "S")

LB_quantidade = CriarLabel(abas.tab('Informações do livro'),'Quantidade Vendida',6,6)
LB_quantidade.grid(sticky = "S")
CX_quantidade = CriarCaixaDeTexto(abas.tab("Informações do livro"),150,30,7,6)
CX_quantidade.grid(sticky = "S")

LB_preco = CriarLabel(abas.tab('Informações do livro'),'Preço',8,6)
LB_preco.grid(sticky = "S")
CX_preco = CriarCaixaDeTexto(abas.tab("Informações do livro"),150,30,9,6)
CX_preco.grid(sticky = "S")

LB_caixa = CriarLabel(abas.tab('Informações adicionais'),'Numero do caixa',2,6)
LB_caixa.grid(sticky = "S")
CX_caixa = CriarCaixaDeTexto(abas.tab("Informações adicionais"),150,30,3,6)
CX_caixa.grid(sticky = "S")

LB_funcionario = CriarLabel(abas.tab('Informações adicionais'),'Nome do Funcionario',4,6)
LB_funcionario.grid(sticky = "S")
CX_funcionario = CriarCaixaDeTexto(abas.tab("Informações adicionais"),150,30,5,6)
CX_funcionario.grid(sticky = "S")

LB_data = CriarLabel(abas.tab('Informações adicionais'),'Data',6,6)
LB_data.grid(sticky = "S")
CX_data = CriarCaixaDeTexto(abas.tab("Informações adicionais"),150,30,7,6, Modo='Data')
CX_data.grid(sticky = "S")

LB_hora = CriarLabel(abas.tab('Informações adicionais'),'Hora',8,6)
LB_hora.grid(sticky = "S")
CX_hora = CriarCaixaDeTexto(abas.tab("Informações adicionais"),150,30,9,6, Modo='Hora')
CX_hora.grid(sticky = "S")

#--------aba Tabela------
titulo_exibir = CriarLabel(abas.tab('Registrar venda'),'',1,6)
autor_exibir = CriarLabel(abas.tab('Registrar venda'), '',2, 6)
quantidade_exibir = CriarLabel(abas.tab('Registrar venda'), '', 3, 6)
preco_exibir = CriarLabel(abas.tab('Registrar venda'), '', 4, 6)
caixa_exibir = CriarLabel(abas.tab('Registrar venda'), '', 5, 6)
funcionario_exibir = CriarLabel(abas.tab('Registrar venda'), '', 6, 6)
data_exibir = CriarLabel(abas.tab('Registrar venda'), '', 7, 6)
hora_exibir = CriarLabel(abas.tab('Registrar venda'), '', 8, 6)


#-----label erro--------
totalLB = CriarLabel(abas.tab('Registrar venda'),'',9,6)

def RegistrarInformacoes():
    abas.set('Registrar venda')

    titulo = CX_titulo.get()
    autor = CX_autor.get()
    quantidade = int(CX_quantidade.get())
    preco = int(CX_preco.get())
    caixa = CX_caixa.get()
    funcionario = CX_funcionario.get()
    data = CX_data.get()
    hora = CX_hora.get()

    titulo_exibir.configure(text=f'Título: {titulo}')
    autor_exibir.configure(text=f'Autor: {autor}')
    quantidade_exibir.configure(text=f'Quantidade: {quantidade}')
    preco_exibir.configure(text=f'Preço: {preco}')
    caixa_exibir.configure(text=f'Caixa: {caixa}')
    funcionario_exibir.configure(text=f'Funcionário: {funcionario}')
    data_exibir.configure(text=f'Data: {data}')
    hora_exibir.configure(text=f'Hora: {hora}')

    total = quantidade * preco

    totalLB.configure(text=f'Total: R${total}')

#-------------------------BOTOESS-------------------
btn_proximo = CriarBotão(abas.tab('Informações do livro'), "Próximo", Proximo, 10,6,100,30)
btn_voltar = CriarBotão(abas.tab('Informações adicionais'), "Voltar", Voltar, 10,6,100,30 )
btn_volts = CriarBotão(abas.tab('Registrar venda'), "Voltar", Volts, 11,6,100,30)
btn_registrar = CriarBotão(abas.tab('Informações adicionais'), 'Registrar venda', RegistrarInformacoes, 11, 6, 100, 30)
btn_Volar = CriarBotão(janela3,'Voltar',AbrirNavegacao,9,6,100,30)


#----- desing -------

janela3.configure(fg_color='#ba6c6c')
janela3.configure(bg_color='#ba6c6c')

btn_proximo.configure(fg_color='#ffc0cb', text_color='black', hover_color='#cb8e8e')
btn_voltar.configure(fg_color='#ffc0cb', text_color='black', hover_color='#cb8e8e')
btn_volts.configure(fg_color='#ffc0cb', text_color='black', hover_color='#cb8e8e')
btn_registrar.configure(fg_color='#ffc0cb', text_color='black', hover_color='#cb8e8e')
btn_Volar.configure(fg_color='#ffc0cb', text_color='black', hover_color='#cb8e8e')

abas.tab('Informações do livro').configure(fg_color='#f39d9d')
abas.configure(fg_color='#f39d9d')
abas.tab('Informações do livro').configure(bg_color='#f39d9d')

abas.tab('Informações adicionais').configure(fg_color='#f39d9d')
abas.tab('Informações adicionais').configure(bg_color='#f39d9d')

abas.tab('Registrar venda').configure(fg_color='#f39d9d')
abas.tab('Registrar venda').configure(bg_color='#f39d9d')
