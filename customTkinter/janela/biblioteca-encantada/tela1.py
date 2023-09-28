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
        labelerro.configure(text='Login ou senha invalidos', font=('arial', 15))


usuariosLogin = ['aa', 'aaa']
usuariosSenha = ['123', '456']


janela = CriarJanela('Biblioteca Encantada', '700x600', 1, redimensionar=True)
janela.configure(fg_color='#f4efec')

imagem_janela1 = CriarImagem(janela,'folha.png',1,6,400,700)

#Titulo
titulo_janela1 = CriarLabel(janela, 'Biblioteca Encantada', linha=1, coluna=6)
titulo_janela1.configure(text_color='black')
titulo_janela1.configure(font=('arial',22,'bold'))

#Campo login
login_janela1 = CriarLabel(janela, 'Informe seu login', linha=3, coluna=6)
login_janela1.configure(text_color='#9b9a98')
login_janela1.configure(font=('arial',12,'bold'))

caixa_login_janela1 = CriarCaixaTexto(janela, largura=300, altura=30, linha=4, coluna=6, texto=' ')

#campo senha
senha_janela1 = CriarLabel(janela, 'Informe sua senha', linha=5, coluna=6)
senha_janela1.configure(text_color='#9b9a98')
senha_janela1.configure(font=('arial',12,'bold'))

caixa_senha_janela1 = CriarCaixaTexto(janela, largura=300, altura=30, linha=6, coluna=6, texto=' ')

#Botãio entar
botaoEntrar = CriarBotao(janela, texto='Entrar', comando=clicar, largura=100, altura=30, linha=7, coluna=6)

# para invalido
labelerro = CriarLabel(janela,' ',8,6)

def abrir_janela_estoque():
    janela2 = CriarJanela('Estoque', '600x500', 2, redimensionar=True)
    janela2.configure(fg_color='#f4efec')

    # Livro vendido fixo
    tituloLivro = CriarLabel(janela2,'Titulo: A culpa é das estrelas',1,1)
    autorLivro = CriarLabel(janela2,'Autor: John Green',2,1)
    qntLivro = CriarLabel(janela2,'Qnt vendida: 3' ,3,1)
    precoLivro = CriarLabel(janela2,'preço: 50', 4,1)

def abrir_janela_caixa():
    janela3 = CriarJanela('Caixa com Registro de Vendas', '600x500', 2, redimensionar=True)
    janela3.configure(fg_color='#f4efec')


janela.mainloop()
