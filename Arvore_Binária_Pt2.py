class Nodo:
    def __init__(self, chave, info, esq = None, dir = None):
        self.info = info
        self.chave = esq
        self.esq = esq
        self.dir = dir

    def insere(self, chave, valor):
        if chave > self.chave:
            if self.dir is None:
                self.dir = Nodo(chave, valor)
            else:
                self.dir.insere(chave, valor)
        elif chave < self.chave:
            if self.esq is None:
                self.esq = Nodo(chave, valor)
            else:
                self.esq.insere(chave, valor)
        else: 
            return None

arv = Nodo(30, "raiz")
arv.insere(26, "A")
arv.insere(32, "B")
arv.insere(48, "C")