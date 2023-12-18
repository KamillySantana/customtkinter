import customtkinter as tk

tk.set_appearance_mode('ligth')
janela = tk.CTk()
janela.title('Exercicio')
janela.geometry('500x400')
colunas = list(range(13))
linhas = list(range(13))
janela.grid_columnconfigure(colunas,weight=1)
janela.grid_rowconfigure(linhas,weight=1)

pergunta = tk.CTkLabel(janela, text='Informe o ano que você nasceu', font=('Arial',20))
pergunta.grid(row=1, column=6)

ano = tk.CTkEntry(janela, width=200, height=30)
ano.grid(row=2, column=6)
texto = ano.get()

def clicar():
    anoConvertido = int(ano.get())

    idade = 2023 - anoConvertido

    if idade >= 18:
        exibir.configure(text='Você é maior de idade')
    elif idade < 18:
        exibir.configure(text='Você é menor de idade')

    exibirIdade.configure(text=f'Você tem {idade} anos')


exibir = tk.CTkLabel(janela, text='')
exibir.grid(row=4, column=6)

exibirIdade = tk.CTkLabel(janela, text='')
exibirIdade.grid(row=5, column=6)

btn = tk.CTkButton(janela, text='Clique', command=clicar, width=30, height=30)
btn.grid(row=3, column=6)

janela.mainloop()