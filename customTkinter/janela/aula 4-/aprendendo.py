import customtkinter as tk
from modulotk import *

#STICKY
# alinhar de acordo com uma bússula
# faz com qualquer obj

janela = CriarJanela('teste','500x500',1)


label = CriarLabel(janela,'nome',1,6)
label.grid(sticky='SW')
caixa = CriarCaixaTexto(janela,200,30,2,6,modo='Senha')
caixa.grid(sticky='N') #deixa juntinho

#FRAME
#uma caixinha dentro da janela, a janela é sempre 12 por 12, o frame é uma caixinha dentro de apenas 1 dos 12, com 12 por 12 tambem
frame = CriarFrame()

#ABAS
abas = CriarAbas()

janela.mainloop()




