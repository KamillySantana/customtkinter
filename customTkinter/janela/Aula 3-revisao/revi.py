import customtkinter as tk
from modulotk import *


def clicar():
    # caixa1 = slider_tela1.get()
    # b_tela1.configure(text=caixa1)

    # barraProgresso.set(0.5)

    tela1.withdraw()
    tela2.deiconify()

def alterarTema():
    tema = switch_tela1.get()
    if tema == 1:
        tk.set_appearance_mode('Dark')
    else:
        tk.set_appearance_mode('Light')

tela1 = CriarJanela('revisão', '500x600+500+50',1)
#criar label
lb_tela1 = CriarLabel(tela1, 'Olá, Mundo!',1,6)
#alterações label (opcional)0
lb_tela1.configure(text_color='blue', font=('arial', 18, 'bold'))
#criar botao
btn_tela1 = CriarBotao(tela1,'Clique',clicar,100,30,2,6)
#alterações bota (opcional)
btn_tela1.configure(fg_color='red', hover_color='blue')
#caica de texto
caixa_tela1 = CriarCaixaTexto(tela1,300,30,3,6,'Cpf',modo='CPF')
#criar swi
switch_tela1 = CriarSwitch(tela1,'Alterar tema',4,6,comando=alterarTema)

listaNomes = ['kamilly', 'Isabella', 'Barbara']
combo_tela1 = CriarCombo(tela1,listaNomes,200,30,5,6)

slider_tela1 = CriarSlider(tela1,300,10,6,6)
barraProgresso = CriarProgress(tela1, 400,20,7,6)

imagem = CriarImagem(tela1,'gatinho.webp',8,6,150,300)

tela2 = CriarJanela('Tela 2','500x600+500+50',2)
tela2.withdraw()


tela1.mainloop()