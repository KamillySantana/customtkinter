import customtkinter as tk
import random

tk.set_appearance_mode('ligth')
janela = tk.CTk()
janela.title('Exercicio')
janela.geometry('500x500')
colunas = list(range(13))
linhas = list(range(13))
janela.grid_columnconfigure(colunas,weight=1)
janela.grid_rowconfigure(linhas,weight=1)

numero_aleatorio = random.randint(1, 100)

intrducao = tk.CTkLabel(janela, text='Jogo de adivinhação', font=('Arial',22))
intrducao.grid(row=1, column=6)

intrducao2 = tk.CTkLabel(janela, text='Estou pensando em um número de 1 a 100, tente adivinha-lo!', font=('Arial',17))
intrducao2.grid(row=2, column=6)

num = tk.CTkEntry(janela, placeholder_text='Chute um numero',width=200, height=30)
num.grid(row=3, column=6)
texto = num.get()

def clique():
    n1 = int(num.get())

    if n1 < numero_aleatorio:
        exibir.configure(text=f'é maior do que {n1}')
    elif n1 > numero_aleatorio:
        exibir.configure(text=f'é menor do que {n1}')
    elif n1 == numero_aleatorio:
        exibir.configure(text=f'Parabens! Voce acerto, o número era: {n1} ')

botao = tk.CTkButton(janela, text="Chutar", command=clique)
botao.grid(row=4, column=6)

exibir = tk.CTkLabel(janela, text='')
exibir.grid(row=5, column=6)

janela.mainloop()



