import customtkinter as tk

# JANELA
tk.set_appearance_mode('Dark') #cria uma janela, onde pode escolher em light ou dark, claro ou escuro
janela = tk.CTk() #instanciando uma classe para um objeto
janela.title('Janela 1') #titulo da janela
janela.geometry('400x350') #tamanho da janela

janela.configure(fg_color='SkyBlue') #cor da janela
janela.resizable(width=False, height=False) #a janela fica fixa no tamanho q coloquei
colunas = list(range(13)) #colocar colunas e linhas
linhas = list(range(13))
janela.grid_columnconfigure(colunas,weight=1)
janela.grid_rowconfigure(linhas,weight=1)

# LABEL
#text = 'o que vai aparecer'
#text_color = 'red'
#font = ('Arial',16, 'bold')
texto1 = tk.CTkLabel(janela, text='Olá, mundo!', font=('Arial',20), text_color=('black'))
texto1.grid(row=2, column=6) #Onde deve ser posicionado o texto

texto2 = tk.CTkLabel(janela, text='TEXTÃO', font=('Arial',16), text_color=('black'))
texto2.grid(row=3, column=6) #Onde deve ser posicionado o texto

# BOTAO
def clicar(): #função do clicar, para funcionar o botão
    texto2.configure(text=caixa1.get()) #aqui o que eu digitar na caixa de texto vai ser alterado no texto2 pelo botao

# BOTÃO
btn1 = tk.CTkButton(janela, text='Clique aqui', command=clicar, width=20, height=20) #configurações da botao
btn1.grid(row=5, column=6) #posicionamneto dele

# CAIXA DE TEXTO
caixa1 = tk.CTkEntry(janela, placeholder_text='Digete seu nome',width=200, height=30) #configurações do caixa de texto
caixa1.grid(row=4, column=6) #posicionamneto
texto = caixa1.get()

# A janela precisa entrar em um loop, se n ela vai abrir e fecha
# Tudo que declarar precisa ser acima do mainloop, ele tem q ser o ultimo
janela.mainloop()


