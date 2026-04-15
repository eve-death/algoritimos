from Livro import Livro

class Pilha:


    def __init__(self):
        self.topo = None

    def add(self, valor):
        if self.topo is not None:
            livro.prox = self.topo
        self.topo = livro
        self.imprimir()

    def remnover(self):
        if self.topo is not None:
            self.topo = self.topo.prox
        self.imprimir()
    
    def imprimir(self):
        print("-------------------")
        if self.topo is None:
            print("nPilha Vazia")
        else:
            print("\n")