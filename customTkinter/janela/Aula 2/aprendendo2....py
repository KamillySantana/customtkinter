import customtkinter as tk
from modulotk import *

tk.set_appearance_mode('ligth')
janela = CriarJanela('check', '500x500')

# CHECK BOX
check = tk.CTkCheckBox(janela, text='Marque')
check.grid(row=1, column=1)
check.get()

label = CriarLabel(janela, texto=' ', linha=3, coluna=1)

def clicar():
    if check.get() == 1:
        label.configure(text='Marcado')
    else:
        label.configure(text='Desmarcado')


botao = CriarBotao(janela, texto='Clique', comando=clicar, largura=30, altura=30, linha=2, coluna=1)

# SWITCH
swi = tk.CTkSwitch(janela, text='Marque')
swi.grid(row=4, column=1)
swi.get()

#COMBO BOX
listaCB = ['Item 1', 'Item 2', 'Item 3'] #A lista precisa ser string sempre
combo = tk.CTkComboBox(janela, width=200, height=30, values=listaCB, state='readonly')
combo.grid(row=5, column=1)

#PROGRESS BAR
progress = tk.CTkProgressBar(janela, width=200, height=10)
progress.grid(row=6, column=1)
progress.set(0.2) #Progresso vai de 0 a 1, sendo 1 barrinha cheia

#SLIDER
slider = tk.CTkSlider(janela, width=200, height=10)
slider.grid(row=7, column=1)
slider.get()

janela.mainloop()

