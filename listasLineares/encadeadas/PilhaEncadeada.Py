from Lista import Lista
class PilhaEncadeada(Lista):
  def pilhaVazia(self):
    return self.listaVazia()
  def push(self, v):
    self.insereNoInicio(v)
  def pop(self):
    return self.retiraNoInicio()