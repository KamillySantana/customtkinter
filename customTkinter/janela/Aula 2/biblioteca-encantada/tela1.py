import customtkinter as tk
from modulotk import *

usuariosLogin = ['aa', 'aaa']
usuariosSenha = ['123', '456']

tk.set_appearance_mode('ligth')

janela = CriarJanela('Biblioteca Encantada', '600x500', 1, redimensionar=True)
janela.configure(fg_color='#f4efec')

loginL = CriarLabel(janela, 'Informe seu login', linha=1, coluna=6)
loginL.configure(text_color='#9b9a98')
loginL.configure(font=('arial',20,'bold'))
caixaLo = CriarCaixaTexto(janela, largura=300, altura=30, linha=2, coluna=6, texto=' ')

senhaL = CriarLabel(janela, 'Informe sua senha', linha=3, coluna=6)
senhaL.configure(text_color='#9b9a98')
senhaL.configure(font=('arial',20,'bold'))
caixaSe = CriarCaixaTexto(janela, largura=300, altura=30, linha=4, coluna=6, texto=' ')

def clicar():
    usuario = caixaLo.get()  # texto da caixa de login
    senha = caixaSe.get()  # texto da caixa de senha e converta para inteiro

    if usuario == usuariosLogin[0] and senha == usuariosSenha[0]:
        janela.withdraw() #esconde janela
        abrir_janela_estoque()
    elif usuario == usuariosLogin[1] and senha == usuariosSenha[1]:
        janela.withdraw() #esconde janela
        abrir_janela_caixa()
    else:
        labelerro.configure(text='login ou senha invalidos')


botaoEntrar = CriarBotao(janela, texto='Entrar', comando=clicar, largura=50, altura=30, linha=5, coluna=6)

labelerro = CriarLabel(janela,' ',7,6)

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
