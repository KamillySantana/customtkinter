import customtkinter as tk
from Modulos import *

def ClicarEntar():
    usuario = login_caixa.get()  # texto da caixa de login
    senha = senha_caixa.get()  # texto da caixa de senha e converta para inteiro

    if usuario == usuariosLogin[0] and senha == usuariosLogin[1]:
        from navegacao import MostrarTelaNavegacao
        janela1.withdraw() #esconde janela
        MostrarTelaNavegacao()
    else:
        LB_erro.configure(text='Login ou senha invalidos', font=('arial', 15))


janela1 = CriarJanela('Leitura Encantada','500x600+550+40',1)

#-------------Login e senha--------
usuariosLogin = ['aaa', '123']

#---------------- Campo login-------
login_label = CriarLabel(janela1,'Login:',2,6)
login_label.grid(sticky = 'S')
login_caixa = CriarCaixaDeTexto(janela1,150,30,3,6)
login_caixa.grid(sticky = 'N')

#---------------- Campo Senha-------
senha_label = CriarLabel(janela1,'Senha:',4,6)
senha_label.grid(sticky = 'S')
senha_caixa = CriarCaixaDeTexto(janela1,150,30,5,6,Modo='Senha')
senha_caixa.grid(sticky = 'N')

#--------------- Botão entrar-------
botaoEntrar = CriarBotão(janela1,'Entrar',ClicarEntar,6,6,100,30)

#--------------Label de erro--------
LB_erro = CriarLabel(janela1,'',7,6)

#----------------design---------------
imagem = CriarImagem(janela1,'logo.png',1,6,200,200)
janela1.configure(fg_color='#BA6C6C')
login_caixa.configure(fg_color='#F39D9D')
senha_caixa.configure(fg_color='#F39D9D')
botaoEntrar.configure(fg_color='#FFC0CB',text_color='black',hover_color='#CB8E8E')

janela1.mainloop()
