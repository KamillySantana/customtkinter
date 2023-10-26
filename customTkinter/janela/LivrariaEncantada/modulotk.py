import customtkinter as tk
from PIL import Image
from tkcalendar import *
primeiro = True

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
    Caixa = tk.CTkEntry(local, width=largura, height=altura)
    Caixa.grid(row=linha, column=coluna)
    if texto !=0:
        Caixa.configure(placeholder_text=texto)

    #Mascaras
    if modo == "Senha":
        Caixa.configure(show="*")
        def SenhaMostra():
            global primeiro
            if primeiro:
                imagem_pillow = Image.open("Imagens/eye.ico")
                imageTk = tk.CTkImage(imagem_pillow, size=[15, 15])
                MostraSenha.configure(image=imageTk)
                Caixa.configure(show="")
                primeiro = False
            else:
                imagem_pillow = Image.open("Imagens/eye2.ico")
                imageTk = tk.CTkImage(imagem_pillow, size=[15, 15])
                MostraSenha.configure(image=imageTk)
                Caixa.configure(show="*")
                primeiro = True
        MostraSenha = CriarBotao(Caixa, "", SenhaMostra, 0, 0, 10, 10, Imagem="Imagens/eye2.ico")
        MostraSenha.grid(sticky="e", padx=2)
        MostraSenha.configure(fg_color=Caixa.cget("fg_color"), hover_color=Caixa.cget("fg_color"), corner_radius=0)
    elif modo == "Hora":
        def format_hora(event=None):
            text = Caixa.get().replace(":", "")[:4]
            new_text = ""
            if event.keysym.lower() == "backspace": return
            for index in range(len(text)):
                if not text[index] in "0123456789": continue
                if index == 1:
                    new_text += text[index] + ":"
                else:
                    new_text += text[index]
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)

        Caixa.bind("<KeyRelease>", format_hora)
    elif modo == "Moeda":
        def format_moeda(event=None):
            text = Caixa.get().replace("R$", "")[:11]
            new_text = ""
            if event.keysym.lower() == "backspace": return
            for index in range(len(text)):
                if not text[index] in "0123456789": continue
                if index == 0:
                    new_text += "R$" + text[index]
                else:
                    new_text += text[index]
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)

        Caixa.bind("<KeyRelease>", format_moeda)
    elif modo == "CPF":
        def format_cpf(event=None):
            text = Caixa.get().replace(".", "").replace("-", "")[:11]
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
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)

        Caixa.bind("<KeyRelease>", format_cpf)
    elif modo == "CNPJ":
        def format_CNPJ(event=None):
            text = Caixa.get().replace(".", "").replace("/", "").replace("-", "")[:14]
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
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)

        Caixa.bind("<KeyRelease>", format_CNPJ)
    elif modo == "Telefone":
        def format_tel(event=None):
            text = Caixa.get().replace("(", "").replace(")", "").replace("-", "")[:11]
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
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)
        Caixa.bind("<KeyRelease>", format_tel)
    elif modo == "Data":
        def format_data(event=None):
            text = Caixa.get().replace("/", "")[:8]
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
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)
        Caixa.bind("<KeyRelease>", format_data)
    elif modo == "CEP":
        def format_cep(event=None):
            text = Caixa.get().replace("-", "")[:8]
            new_text = ""
            if event.keysym.lower() == "backspace":
                return
            for index in range(len(text)):
                if not text[index] in "0123456789":
                    continue
                if index == 5:
                    new_text += "-" + text[index]
                else:
                    new_text += text[index]
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)
        Caixa.bind("<KeyRelease>", format_cep)
    return Caixa

def CriarBotao(Local,Texto,Comando,Linha,Coluna,Largura,Altura,Cor=0,CorHover=0,Imagem="Nada"):
    if Imagem!="Nada":
        imagem_pillow = Image.open(Imagem)
        imageTk = tk.CTkImage(imagem_pillow, size=[15, 15])
        botao = tk.CTkButton(Local, text=Texto, command=Comando,
                             width=Largura, height=Altura, image=imageTk)
        botao.grid(row=Linha, column=Coluna)
    else:
        botao = tk.CTkButton(Local, text=Texto, command=Comando,
                             width=Largura, height=Altura)
        botao.grid(row=Linha, column=Coluna)
    if Cor != 0:
            botao.configure(fg_color=Cor)
    if CorHover != 0:
            botao.configure(hover_color=CorHover)

    return botao

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

#-------------------------------------

#Caixa de Texto (rolagem)
def CriarTextoRolagem(Local,Linha,Coluna,Texto,Largura=0,Altura=0):
    caixatxt= tk.CTkTextbox(Local,wrap="word")
    caixatxt.grid(row=Linha,column=Coluna,sticky="nsew")
    caixatxt.insert("0.0",Texto,)
    if Largura!=0:
        caixatxt.configure(width=Largura)
    if Altura!=0:
        caixatxt.configure(height=Altura)

    return caixatxt

def CriarData(Local,Linha,Coluna):
    pass

#Imagem PIL
def CriarImagem(Local,Caminho,Linha,Coluna,Altura,Largura):
    imagem_pillow = Image.open(Caminho)
    imageTk = tk.CTkImage(imagem_pillow,size=[Largura,Altura])
    imagem = tk.CTkLabel(Local, image=imageTk, text='')
    imagem.grid(row=Linha, column =Coluna)
    return imagem

def CriarFundo(Local,Largura,Altura,Caminho):
    imagem_pillow = Image.open(Caminho)
    imageTk = tk.CTkImage(imagem_pillow,size=[Largura,Altura])
    imagem = tk.CTkLabel(Local, image=imageTk, text= '')
    imagem.place(x=0,y=0)
    return imagem

def CriarFrame(Local,Linha,Coluna,Largura,Altura):
    frame = tk.CTkFrame(Local,width=Largura,height=Altura)
    frame.grid(row=Linha, column=Coluna)
    Tamanho = list(range(13))
    frame.grid_propagate(False)
    frame.grid_rowconfigure(Tamanho, weight=1)
    frame.grid_columnconfigure(Tamanho, weight=1)
    return frame

def CriarAbas(Local,Linha,Coluna,Largura,Altura,*Abas):
    aba = tk.CTkTabview(Local,width=Largura, height=Altura)
    for C in Abas:
        aba.add(C)
        Tamanho = list(range(13))
        aba.tab(C).grid_rowconfigure(Tamanho,weight=1)
        aba.tab(C).grid_columnconfigure(Tamanho, weight=1)
    aba.grid(row=Linha, column=Coluna)
    return aba



