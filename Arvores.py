class Arvore:
    def __init__(self, dado):
        self.esq = None
        self.info = dado
        self.dir = None

    def imprimir_Pre_Esq(self):
        vista = self.info
        print(vista)

        if self.esq:
            self.esq.imprimir_Pre_Esq()

        if self.dir:
            self.dir.imprimir_Pre_Esq()
    
    def infixDir(self):
        if self.dir:
            self.dir.infixDir()

        print(self.info)
        if self.esq:
            self.esq.infixDir()
    def imprimir(self,lado,metodo):
        if lado == "esq" and metodo == "pre":
            self.imprimir_Pre_Esq()
        if lado == "dir" and metodo == "in":
            self.infixDir()
    def localizar (self,V):
        if V == self.info:
            return self
        if self.esq:
            aux = self.esq.localizar(V)
            if aux:
                return aux
        if self.dir:
            aux = self.dir.localizar(V)
            if aux:
                return None
                return aux

    def localiza_Pai(self, valor):
        if self != None:
            if self.esq and self.esq.info == valor:
                return self
            if self.dir and self.dir.info == valor:
                return self
            if self.esq:
                aux = self.esq.localiza_Pai(valor)
                if aux:
                    return aux
            if self.dir:
                aux = self.dir.localiza_Pai(valor)
                if aux:
                    return aux
                return None
                
    def inserir(self,P,F,lado):
        pai = self.localizar(P)
        if pai:
            if lado == "esq":
                if pai.esq == None:
                    pai.esq = Arvore(F)
            if lado == "dir":
                if pai.dir == None:
                    pai.dir = Arvore(F)

    def folha(self):
        return (self.dir == None and self.esq == None)

    def remover(self, valor):
        nodoPai = self.localizar(valor)
        if (nodoPai):
            if (nodoPai.esq and nodoPai.esq.info == valor and nodoPai.esq.folha()):
                nodoPai.esq = None
            if (nodoPai.dir and nodoPai.dir.info == valor and nodoPai.dir.folha()):
                nodoPai.dir = None


a = Arvore("A")
a.esq = Arvore("B")
a.dir = Arvore("C")
a.esq.esq = Arvore("D")
a.esq.esq.dir = Arvore("E")
a.esq.esq.esq = Arvore("F")
a.esq.dir = Arvore("G")

a.imprimir_Pre_Esq()

print("in fix\n")
a.infixDir()