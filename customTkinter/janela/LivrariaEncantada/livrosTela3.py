class livros:
    def __init__(self,nome,autor,qnt,preco):
        self.nome = nome
        self.autor = autor
        self.qnt = qnt
        self.preco = preco

listaLivros = []

def adicionarLivros(nome,autor,qnt,preco):
    obj = livros(nome,autor,qnt,preco)
    listaLivros.append(obj)

def pesquisar(nome):
    if not listaLivros:
        return 'vazio'
    else:
        for l in listaLivros:
            if l.nome == nome:
                indice = listaLivros.index(l)
                return indice
            else:
                return 'erro'