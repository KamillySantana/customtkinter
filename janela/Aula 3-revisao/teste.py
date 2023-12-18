import customtkinter as tk
from modulotk import *

tela1 = CriarJanela('Login', '500x600+500+50',1)

def clicar():
    tela1.withdraw()
    tela2.deiconify()


def clicarTela2():
    tela2.withdraw()
    tela3.deiconify()


def clicarTela3():
    tela3.withdraw()
    tela1.deiconify()


lo_tela1 = CriarLabel(tela1, 'Login',1,6)
caixa_lo_tela1 = CriarCaixaTexto(tela1,300,30,2,6)

se_tela1 = CriarLabel(tela1, 'Senha',3,6)
caixa_se_tela1 = CriarCaixaTexto(tela1,300,30,4,6,modo='Senha')

btn_tela1 = CriarBotao(tela1,'Não cadastrado ? cadastra-se',clicar,100,30,5,6)

tela2 = CriarJanela('Tela 2','500x600+500+50',2)
tela2.withdraw()

email_tela2 = CriarLabel(tela2, 'Email',1,6)
caixa_email_tela2 = CriarCaixaTexto(tela2,300,30,2,6)

se_tela2 = CriarLabel(tela2, 'Senha',3,6)
caixa_se_tela2 = CriarCaixaTexto(tela2,300,30,4,6,modo='Senha')

btn_tela2 = CriarBotao(tela2,'Cadastrar',clicarTela2,100,30,5,6)

tela3 = CriarJanela('Cadastrado','500x600+500+50',2)
tela3_cadastrado = CriarLabel(tela3, 'Login efetuado com sucesso, Parabens!',1,6)
tela3.withdraw()
imagem = CriarImagem(tela3,'gato_joinha.jpg',2,6,300,300)
btn_tela3 = CriarBotao(tela3,'Voltar para a pagina inicial',clicarTela3,100,30,3,6)


tela1.mainloop()

