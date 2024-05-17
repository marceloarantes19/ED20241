from Elemento import Elemento
from No import No
class ArvoreBB:
    def __init__(self):
        self.__raiz = None 
    def getRaiz(self):
        return self.__raiz 
    def setRaiz(self, n):
        self.__raiz = n 
    def arvoreVazia(self):
        return self.getRaiz() == None
    def criaNoChave(self, chave = 0):
        elemento = Elemento(chave)
        no = No(elemento)
        return no
    def criaNoElemento(self, elemento = None):
        no = No(elemento)
        return no
    def insereNoChave(self, chave):
        no = self.criaNoChave(chave)
        self.insere(no)
    def insereNoElemento(self, e):
        no = self.criaNoElemento(e)
        self.insere(no)
    def insere(self, no):
        if self.arvoreVazia():
            self.setRaiz(no)
        else:
            self.insereNo(None, self.getRaiz(), no)
    def insereNo(self, pai, atual, no):
        if atual == None:
            if no.eMenor(pai):
                pai.setFilhoAEsquerda(no)
            else:
                pai.setFilhoADireita(no)
        elif no.eMenor(atual):
            self.insereNo(atual, atual.getFilhoAEsquerda(), no)
        else:
            self.insereNo(atual, atual.getFilhoADireita(), no)
    def preOrdem(self, n):
        if n != None:
            print(n.getValores())
            self.preOrdem(n.getFilhoAEsquerda())
            self.preOrdem(n.getFilhoADireita())
    def emOrdem(self, n):
        if n != None:
            self.emOrdem(n.getFilhoAEsquerda())
            print(n.getValores())
            self.emOrdem(n.getFilhoADireita())
    def posOrdem(self, n):
        if n != None:
            self.posOrdem(n.getFilhoAEsquerda())
            self.posOrdem(n.getFilhoADireita())
            print(n.getValores())
    def remove(self, v):
        if self.arvoreVazia():
            return None 
        else:
            return self.removeElemento(None, self.getRaiz(), v)
    def removeElemento(self, pai, atual, v):
        if v < atual.getChave():
            return self.removeElemento(atual, atual.getFilhoAEsquerda(), v)
        elif v > atual.getChave():
            return self.removeElemento(atual, atual.getFilhoADireita(), v)
        elif v == atual.getChave(): # Faz a remoção
            ret = atual
            if atual.eFolha():
                if atual == self.getRaiz():
                    self.setRaiz(None)
                elif atual.eFilhoAEsquerda(pai):
                    pai.setFilhoAEsquerda(None)
                else:
                    pai.setFilhoADireita(None)
            elif atual.soTemFilhoAEsquerda():
                if atual == self.getRaiz():
                    self.setRaiz(atual.getFilhoAEsquerda())
                elif atual.eFilhoAEsquerda(pai):
                    pai.setFilhoAEsquerda(atual.getFilhoAEsquerda())
                else:
                    pai.setFilhoADireita(atual.getFilhoADireita())
            elif atual.soTemFilhoADireita():
                if atual == self.getRaiz():
                    self.setRaiz(atual.getFilhoADireita())
                elif atual.eFilhoADireita(pai):
                    pai.setFilhoADireita(atual.getFilhoADireita())
                else:
                    pai.setFilhoAEsquerda(atual.getFilhoADireita())
            else: # Tem dois filhos
                ret = self.maisADireita(atual, atual, atual.getFilhoAEsquerda())
            return ret
        else:
            return None
    def maisADireita(self, fixo, pai, atual):
        if atual.getFilhoADireita() != None:
            return self.maisADireita(fixo, atual, atual.getFilhoADireita())
        else:
            x = atual.getDados()
            atual.setDados(fixo.getDados())
            fixo.setDados(x)
            if fixo == pai:
                pai.setFilhoAEsquerda(atual.getFilhoAEsquerda())
            else:
                pai.setFilhoADireita(atual.getFilhoAEsquerda())
            atual.setFilhoAEsquerda(None)
            return atual
