import customtkinter as tk
from modulotk import *

def clicar():
    usuario = caixa_login_janela1.get()  # texto da caixa de login
    senha = caixa_senha_janela1.get()  # texto da caixa de senha e converta para inteiro

    if usuario == usuariosLogin[0] and senha == usuariosSenha[0]:
        janela.withdraw() #esconde janela
        abrir_janela_estoque()
    elif usuario == usuariosLogin[1] and senha == usuariosSenha[1]:
        janela.withdraw() #esconde janela
        abrir_janela_caixa()
    else:
        labelErro.configure(text='Login ou senha invalidos', font=('arial', 15))

def ClicarRegistar():
    pass

def abrir_janela_estoque():
    janela3 = CriarJanela('Estoque', '600x500', 2, redimensionar=True)
    janela3.configure(fg_color='#f4efec')

# -------------------- JANELA CAIXA -------------------
def abrir_janela_caixa():
    janela2 = CriarJanela('Caixa com Registro de Vendas', '600x500', 2, redimensionar=True)
    janela2.configure(fg_color='#f4efec')

    #INFORMÇÕES LIVROS----------
    informacoes_livros = CriarAbas(janela2, 1, 6, 550, 150,'Localizar','Venda')

    label_titulo = CriarLabel(informacoes_livros.tab("Localizar"),'Título do livro:',1,1)
    label_titulo.configure(font=('arial',15))
    caixa_titulo = CriarCaixaTexto(informacoes_livros.tab("Localizar"),300,30,2,1)

    label_autor = CriarLabel(informacoes_livros.tab("Localizar"),'Autor do livro:',1,2)
    label_autor.configure(font=('arial',15))
    caixa_autor = CriarCaixaTexto(informacoes_livros.tab("Localizar"),300,30,2,2)
    #-----------
    label_qnt = CriarLabel(informacoes_livros.tab("Venda"),'Quantidade de venda:',1,1)
    label_qnt.configure(font=('arial',15))
    caixa_qnt = CriarCaixaTexto(informacoes_livros.tab("Venda"),300,30,2,1,)

    label_qnt = CriarLabel(informacoes_livros.tab("Venda"), 'Preço:', 1, 2)
    label_qnt.configure(font=('arial', 15))
    caixa_qnt = CriarCaixaTexto(informacoes_livros.tab("Venda"), 300, 30, 2, 2,modo='Moeda')

    #INFORMÇÕES VENDEDOR----------
    informacoes_vendedor = CriarAbas(janela2, 2, 6, 550, 150,'Caixa','Data e Hora')

    label_Ncaixa = CriarLabel(informacoes_vendedor.tab("Caixa"), 'Número do caixa', 1, 1)
    label_Ncaixa.configure(font=('arial', 15))
    caixa_Ncaixa = CriarCaixaTexto(informacoes_vendedor.tab("Caixa"), 300, 30, 2, 1,)

    label_vendedor = CriarLabel(informacoes_vendedor.tab("Caixa"), 'Nome do funcionário', 1, 2)
    label_vendedor.configure(font=('arial', 15))
    caixa_vendedor = CriarCaixaTexto(informacoes_vendedor.tab("Caixa"), 300, 30, 2, 2)

    label_data = CriarLabel(informacoes_vendedor.tab("Data e Hora"), 'Data', 1, 1)
    label_data.configure(font=('arial', 15))
    caixa_data = CriarCaixaTexto(informacoes_vendedor.tab("Data e Hora"), 300, 30, 2, 1, modo='Data')

    label_hora = CriarLabel(informacoes_vendedor.tab("Data e Hora"), 'Hora', 1, 2)
    label_hora.configure(font=('arial', 15))
    caixa_hora = CriarCaixaTexto(informacoes_vendedor.tab("Data e Hora"), 300, 30, 2, 2)

    botao_registar = CriarBotao(janela2,'Registrar Venda',ClicarRegistar,50,30,3,6)


# -------------------- JANELA 1 -------------------
usuariosLogin = ['aa', 'aaa']
usuariosSenha = ['123', '456']

janela = CriarJanela('Leitura Encantada', '700x600', 1, redimensionar=True)
janela.configure(fg_color='#f4efec')

# Titulo-------
titulo_janela1 = CriarLabel(janela, 'Leitura Encantada', linha=1, coluna=6)
titulo_janela1.configure(text_color='black')
titulo_janela1.configure(font=('arial',22,'bold'))

# Campo login-------
login_janela1 = CriarLabel(janela, 'Informe seu login:', linha=3, coluna=6)
login_janela1.configure(text_color='#9b9a98')
login_janela1.configure(font=('arial',12,'bold'))
login_janela1.grid(sticky='SW')

caixa_login_janela1 = CriarCaixaTexto(janela, largura=300, altura=30, linha=4, coluna=6, texto=' ')
caixa_login_janela1.grid(sticky='NW')

# campo senha-------
senha_janela1 = CriarLabel(janela, 'Informe sua senha:', linha=5, coluna=6)
senha_janela1.configure(text_color='#9b9a98')
senha_janela1.configure(font=('arial',12,'bold'))
senha_janela1.grid(sticky='SW')

caixa_senha_janela1 = CriarCaixaTexto(janela, largura=300, altura=30, linha=6, coluna=6, modo='Senha')
caixa_senha_janela1.grid(sticky='NW')

# Botãio entar-------
botaoEntrar = CriarBotao(janela, texto='Entrar', comando=clicar, largura=100, altura=30, linha=7, coluna=6)

# para invalido-------
labelErro = CriarLabel(janela,' ',8,6)

janela.mainloop()
