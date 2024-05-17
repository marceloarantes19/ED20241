class Elemento:
    def __init__(self, chave = 0):
        self.__chave = chave
        self.__nome  = ""
    def getChave(self):
        return self.__chave
    def setChave(self, c):
        self.__chave = c 
    def getNome(self):
        return self.__nome 
    def setNome(self, n):
        self.__nome = n
    def getValores(self):
        return (self.__chave, self.__nome)
    def eIgual(self, e):
        return self.__chave == e.getChave()
    def eMaior(self, e):
        return self.__chave > e.getChave()
    def eMenor(self, e):
        return self.__chave < e.getChave()
    def eIgualValor(self, v):
        return self.__chave == v
    def eMaiorValor(self, v):
        return self.__chave > v
    def eMenorValor(self, v):
        return self.__chave < v
