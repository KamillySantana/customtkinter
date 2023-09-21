import customtkinter as tk


def CriarJanela(titulo, tamanho, redimensionar=False):
    janela = tk.CTk()
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

    # import modulo-tk-para-import *
    # janela = CriarJanela(titulo, tamanho)


def CriarLabel(local, texto, linha, coluna):
    label = tk.CTkLabel(local, text=texto)
    label.grid(row=linha, column=coluna)
    return label

    #label.configure

def CriarCaixaTexto(local, largura, altura, linha, coluna, texto='nada'):
    caixa = tk.CTkEntry(local, width=largura, height=altura)
    caixa.grid(row=linha, column=coluna)
    if texto !='nada':
        caixa.configure(placeholder_text=texto)
    return caixa


def CriarBotao(local, texto, comando, largura, altura, linha, coluna):
    btn = tk.CTkButton(local, text=texto, command=comando, width=largura, height=altura)
    btn.grid(row=linha, column=coluna)
    return btn


#check box
def CriarCheck(local, texto, linha, coluna):
    check = tk.CTkCheckBox(local, text=texto)
    check.grid(row=linha, column=coluna)
    return check


#switch
def CriarSwitch(local, texto, linha, coluna):
    swi = tk.CTkCheckBox(local, text=texto)
    swi.grid(row=linha, column=coluna)
    return swi


# Combo box
def CriarCombo(local, valores, largura, altura, linha, coluna):
    combo = tk.CTkComboBox(local, width=largura, height=altura, values=valores, state='readonly')
    combo.grid(row=linha, column=coluna)
    combo.set('Selecione')
    return combo

#progress bar
def CriarProgress(local, largura, altura, linha, coluna):
    progress = tk.CTkCheckBox(local, width=largura, height=altura)
    progress.grid(row=linha, column=coluna)
    return progress

#slider
def CriarSlider(local, largura, altura, linha, coluna):
    slider = tk.CTkSlider(local, width=largura, height=altura)
    slider.grid(row=linha, column=coluna)
    slider.get()
    return slider