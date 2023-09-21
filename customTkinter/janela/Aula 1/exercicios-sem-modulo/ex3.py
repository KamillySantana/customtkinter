import customtkinter as tk

tk.set_appearance_mode('ligth')
janela = tk.CTk()
janela.title('Exercicio')
janela.geometry('500x400')
colunas = list(range(13))
linhas = list(range(13))
janela.grid_columnconfigure(colunas,weight=1)
janela.grid_rowconfigure(linhas,weight=1)

compra = tk.CTkEntry(janela, placeholder_text='Informe o valor da compra', width=200, height=30)
compra.grid(row=1, column=6)
texto = compra.get()

prestacoes = tk.CTkEntry(janela, placeholder_text='Informe o valor da quantidade de prestações', width=200, height=30)
prestacoes.grid(row=2, column=6)
texto2 = prestacoes.get()

def clicar():
    valorCompra = float(compra.get())
    ValorPrestacoes = float(prestacoes.get())

    calculoPres = valorCompra / ValorPrestacoes

    if calculoPres > 500:
        exibir.configure(text='O valor passa de 500, o usúario não consegue pagar')

    exibirPrestacao.configure(text=f'Valor da prestação: {calculoPres} reais')

exibir = tk.CTkLabel(janela, text='')
exibir.grid(row=4, column=6)

exibirPrestacao = tk.CTkLabel(janela, text='')
exibirPrestacao.grid(row=5, column=6)

btn = tk.CTkButton(janela, text='Clique', command=clicar, width=30, height=30)
btn.grid(row=3, column=6)

janela.mainloop()