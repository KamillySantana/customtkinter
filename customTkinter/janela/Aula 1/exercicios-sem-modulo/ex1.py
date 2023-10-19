import customtkinter as tk

tk.set_appearance_mode('ligth')
janela = tk.CTk()
janela.title('Exercicio')
janela.geometry('500x400')
colunas = list(range(13)) #colunas e linhas 12
linhas = list(range(13))
janela.grid_columnconfigure(colunas,weight=1)
janela.grid_rowconfigure(linhas,weight=1)

nota1 = tk.CTkEntry(janela, placeholder_text='Digite a nota do aluno',width=200, height=30)
nota1.grid(row=2, column=6)
texto = nota1.get()

nota2 = tk.CTkEntry(janela, placeholder_text='Digite a segunda nota do aluno',width=200, height=30)
nota2.grid(row=3, column=6)
texto2 = nota2.get()

def clicar():
    n1 = float(nota1.get())
    n2 = float(nota2.get())

    media = (n1 + n2) / 2

    if media >= 6:
        resultado.configure(text='Aprovado')
    elif media < 6:
        resultado.configure(text='Reprovado')

    nota.configure(text=f'sua nota é {media}')


btn = tk.CTkButton(janela, text='Clique', command=clicar, width=30, height=30)
btn.grid(row=4, column=6)

resultado = tk.CTkLabel(janela, text='')
resultado.grid(row=5, column=6)

nota = tk.CTkLabel(janela, text='')
nota.grid(row=6, column=6)

janela.mainloop()