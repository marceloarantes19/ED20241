from Elemento import Elemento
class No:
    def __init__(self, e = None):
        self.__dados  = e
        self.__filhoE = None
        self.__filhoD = None
    def getDados(self):
        return self.__dados 
    def setDados(self, d):
        self.__dados = d
    def getFilhoAEsquerda(self):
        return self.__filhoE
    def setFilhoAEsquerda(self, n):
        self.__filhoE = n 
    def getFilhoADireita(self):
        return self.__filhoD
    def setFilhoADireita(self, n):
        self.__filhoD = n 
    def eFolha(self):
        return self.__filhoE == None and self.__filhoD == None
    def eFilhoAEsquerda(self, pai):
        return self == pai.getFilhoAEsquerda()
    def eFilhoADireita(self, pai):
        return self == pai.getFilhoADireita()
    def temDoisFilhos(self):
        return self.__filhoE != None and self.__filhoD != None 
    def soTemFilhoAEsquerda(self):
        return self.__filhoE != None and self.__filhoD == None
    def soTemFilhoADireita(self):
        return self.__filhoE == None and self.__filhoD != None
    def eIgual(self, no):
        return self.getDados().eIgual(no.getDados())
    def eMenor(self, no):
        return self.getDados().eMenor(no.getDados())
    def eMaior(self, no):
        return self.getDados().eMaior(no.getDados())
    def getChave(self):
        return self.getDados().getChave()
    def getValores(self):
        return self.getDados().getValores()