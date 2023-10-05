import customtkinter as tk

tk.set_appearance_mode('ligth')
janela = tk.CTk()
janela.title('Exercicio')
janela.geometry('500x400')
colunas = list(range(14)) #colunas e linhas 13
linhas = list(range(14))
janela.grid_columnconfigure(colunas,weight=1)
janela.grid_rowconfigure(linhas,weight=1)

num = tk.CTkEntry(janela, placeholder_text='Digite um numero',width=200, height=30)
num.grid(row=2, column=6)
texto = num.get()

num2 = tk.CTkEntry(janela, placeholder_text='Digite um segundo numero',width=200, height=30)
num2.grid(row=3, column=6)
texto2 = num2.get()

def clicar():
    n1 = float(num.get())
    n2 = float(num2.get())

    if n1 > n2:
        maior.configure(text=f'O {n1} é maior')
    elif n1 < n2:
        maior.configure(text=f'O {n2} é maior')
    else:
        maior.configure(text='Eles são iguais')

maior = tk.CTkLabel(janela, text='')
maior.grid(row=5, column=6)

btn = tk.CTkButton(janela, text='Clique', command=clicar, width=30, height=30)
btn.grid(row=4, column=6)

janela.mainloop()
