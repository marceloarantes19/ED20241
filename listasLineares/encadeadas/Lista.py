from Elemento import Elemento
from No import No
class Lista:
  def __init__(self):
    elemento = Elemento()
    no = No(elemento)
    self.__cabeca = no
  def getCabeca(self):
    return self.__cabeca
  def setCabeca(self, c):
    self.__cabeca = c
  # Método que verifica se a Lista está vazia
  def listaVazia(self):
    return self.getCabeca().getProximo() == None
  # Método para inserir dados no início da Lista
  def insereNoInicio(self, n): # n é um nó
    n.setProximo(self.getCabeca().getProximo())
    self.getCabeca().setProximo(n)
  # Método para retirar dados no início da Lista
  def retiraNoInicio(self):
    ret = None
    if not self.listaVazia():
      ret = self.getCabeca().getProximo()
      self.getCabeca().setProximo(ret.getProximo())
      ret.setProximo(None)
    return ret
  # Método para inserir dados no fim da Lista
  def insereNoFim(self, n):
    aux = self.getCabeca()
    while aux.getProximo() != None:
      aux = aux.getProximo()
    aux.setProximo(n)
  # Método para retirar dados no fim da Lista
  def retiraNoFim(self):
    atual = None
    if not self.listaVazia():
      aux = self.getCabeca()
      atual = self.getCabeca().getProximo()
      while atual.getProximo() != None:
        aux = atual
        atual = aux.getProximo()
      aux.setProximo(None)
    return atual
  # Método para inserir dados ordenados pela chave
  def insereOrdenadoChave(self, n):
    aux = self.getCabeca()
    atual = aux.getProximo()
    while atual != None and n.getElemento().getChave()>atual.getElemento().getChave():
      aux = atual
      atual = aux.getProximo()
    n.setProximo(atual)
    aux.setProximo(n)
  # Método para retirar dados a partir da chave
  def retiraNoChave(self, v):
    atual = None
    if not self.listaVazia():
      aux = self.getCabeca()
      atual = aux.getProximo()
      while atual != None and v!=atual.getElemento().getChave():
        aux = atual
        atual = aux.getProximo()
      if atual != None:
        aux.setProximo(atual.getProximo())
        atual.setProximo(None)
    return atual

  # Método INTERATIVO para mostrar os elementos da lista
  def mostraLista(self):
    aux = self.getCabeca().getProximo()
    while aux != None:
      print(aux.getElemento().getValores())
      aux = aux.getProximo()

# Correção dos Exercícos
# Exercício Nº 3
  def getQuantidade(self):
    ret = 0
    aux = self.getCabeca().getProximo()
    while aux != None:
      ret = ret + 1
      aux = aux.getProximo()
    return ret

  # Método RECUSIVO para mostrar os elementos da lista
  def mostraListaRec(self, n):
    if n != None:
      print(n.getElemento().getValores())
      self.mostraListaRec(n.getProximo())

  # Método RECUSIVO para mostrar os elementos da lista Invertido
  def mostraListaInv(self, n):
    if n != None:
      self.mostraListaInv(n.getProximo())
      print(n.getElemento().getValores())

  # Insere na Posicao
  def insereNaPosicao(self, n, pos):
    if pos > 0 and pos <= (self.getQuantidade() + 1):
      ind = 1
      ante  = self.getCabeca()
      atual = self.getCabeca().getProximo()
      while atual != None and ind < pos:
        ante  = atual
        atual = ante.getProximo()
        ind = ind + 1
      n.setProximo(atual)
      ante.setProximo(n)

  # Retira na Posicao
  def retiraNaPosicao(self, pos):
    ret = None
    if pos > 0 and pos <= self.getQuantidade():
      ind = 1
      ante  = self.getCabeca()
      atual = self.getCabeca().getProximo()
      while ind < pos:
        ante  = atual
        atual = ante.getProximo()
        ind = ind + 1
      ante.setProximo(atual.getProximo())
      atual.setProximo(None)
      ret = atual
    return ret

  # Limpando a Lista (Exercício 8)  
  def limpaLista(self, n):
    if n != None:
      self.limpaLista(n.getProximo())
      n.setProximo(None)


