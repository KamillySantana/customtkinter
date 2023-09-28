import customtkinter as tk
from PIL import Image


def CriarJanela(titulo,tamanho,tipo,redimensionar=False):
    if tipo ==1:
        janela = tk.CTk()
    elif tipo ==2:
        janela = tk.CTkToplevel()
    elif tipo ==3:
        janela = tk.CTkInputDialog()
    janela.title(titulo)
    janela.geometry(tamanho)
    if redimensionar !=False:
        janela.resizable(width=True, height=True)
    else:
        janela.resizable(width=False, height=False)
    colunas = list(range(13))
    linhas = list(range(13))
    janela.grid_columnconfigure(colunas, weight=1)
    janela.grid_rowconfigure(linhas, weight=1)
    return janela


def CriarLabel(local, texto, linha, coluna):
    label = tk.CTkLabel(local, text=texto)
    label.grid(row=linha, column=coluna)
    return label


def CriarCaixaTexto(local, largura, altura, linha, coluna, texto=0, modo='Padrao'):
    caixa = tk.CTkEntry(local, width=largura, height=altura)
    caixa.grid(row=linha, column=coluna)
    if texto !=0:
        caixa.configure(placeholder_text=texto)

    #Mascaras
    if modo == "Senha":
        caixa.configure(show="*")
    elif modo == "Moeda":
        def format_moeda(event=None):
            text = caixa.get().replace("R$", "")[:11]
            new_text = ""
            if event.keysym.lower() == "backspace": return
            for index in range(len(text)):
                if not text[index] in "0123456789": continue
                if index == 0:
                    new_text += "R$" + text[index]
                else:
                    new_text += text[index]
            caixa.delete(0, "end")
            caixa.insert(0, new_text)

        caixa.bind("<KeyRelease>", format_moeda)
    if modo == "CPF":
        def format_cpf(event=None):
            text = caixa.get().replace(".", "").replace("-", "")[:11]
            new_text = ""
            if event.keysym.lower() == "backspace": return
            for index in range(len(text)):

                if not text[index] in "0123456789": continue
                if index in [2, 5]:
                    new_text += text[index] + "."
                elif index == 8:
                    new_text += text[index] + "-"
                else:
                    new_text += text[index]
            caixa.delete(0, "end")
            caixa.insert(0, new_text)

        caixa.bind("<KeyRelease>", format_cpf)
    elif modo == "CNPJ":
        def format_CNPJ(event=None):
            text = caixa.get().replace(".", "").replace("/", "").replace("-", "")[:14]
            new_text = ""
            if event.keysym.lower() == "backspace": return
            for index in range(len(text)):
                if not text[index] in "0123456789": continue
                if index == 0:
                    new_text += "(" + text[index]
                elif index == 7:
                    new_text += text[index] + "/"
                elif index == 11:
                    new_text += text[index] + "-"
                else:
                    new_text += text[index]
            caixa.delete(0, "end")
            caixa.insert(0, new_text)

        caixa.bind("<KeyRelease>", format_CNPJ)
    elif modo == "Telefone":
        def format_tel(event=None):
            text = caixa.get().replace("(", "").replace(")", "").replace("-", "")[:11]
            new_text = ""
            if event.keysym.lower() == "backspace": return
            for index in range(len(text)):
                if not text[index] in "0123456789": continue
                if index == 0:
                    new_text += "(" + text[index]
                elif index == 1:
                    new_text += text[index] + ")"
                elif index == 5:
                    new_text += text[index] + "-"
                else:
                    new_text += text[index]
            caixa.delete(0, "end")
            caixa.insert(0, new_text)

        caixa.bind("<KeyRelease>", format_tel)
    elif modo == "Data":
        def format_data(event=None):
            text = caixa.get().replace("/", "")[:8]
            new_text = ""
            if event.keysym.lower() == "backspace":
                return
            for index in range(len(text)):
                if not text[index] in "0123456789":
                    continue
                if index in [1, 3]:
                    new_text += text[index] + "/"
                elif index == 9:
                    new_text += text[index]
                else:
                    new_text += text[index]
            caixa.delete(0, "end")
            caixa.insert(0, new_text)

        caixa.bind("<KeyRelease>", format_data)

    return caixa
def CriarBotao(local, texto, comando, largura, altura, linha, coluna):
    btn = tk.CTkButton(local, text=texto, command=comando, width=largura, height=altura)
    btn.grid(row=linha, column=coluna)
    return btn


#check box
def CriarCheck(local, texto, linha, coluna, comando=0):
    check = tk.CTkCheckBox(local, text=texto)
    check.grid(row=linha, column=coluna)
    if comando != 0:
        check.configure(command=comando)
    return check


#switch
def CriarSwitch(local, texto, linha, coluna, comando=0):
    swi = tk.CTkSwitch(local, text=texto)
    swi.grid(row=linha, column=coluna)
    if comando != 0:
        swi.configure(command=comando)
    return swi


# Combo box
def CriarCombo(local, valores, largura, altura, linha, coluna, comando=0):
    combo = tk.CTkComboBox(local, width=largura, height=altura, values=valores, state='readonly')
    combo.grid(row=linha, column=coluna)
    combo.set('Selecione')
    if comando != 0:
        combo.configure(command=comando)
    return combo

#progress bar
def CriarProgress(local, largura, altura, linha, coluna):
    progress = tk.CTkProgressBar(local, width=largura, height=altura)
    progress.grid(row=linha, column=coluna)
    progress.set(0)
    return progress

#slider
def CriarSlider(local, largura, altura, linha, coluna):
    slider = tk.CTkSlider(local, width=largura, height=altura)
    slider.grid(row=linha, column=coluna)
    slider.set(0)
    return slider

#Imagem PIL
def CriarImagem(Local,Caminho,Linha,Coluna,Altura,Largura):
    imagem_pillow = Image.open(Caminho)
    imageTk = tk.CTkImage(imagem_pillow,size=[Largura,Altura])
    imagem = tk.CTkLabel(Local, image=imageTk, text='')
    imagem.grid(row=Linha, column =Coluna)
    return imagem