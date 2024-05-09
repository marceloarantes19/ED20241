from Lista import Lista
class FilaEncadeada(Lista):
  def FilaVazia(self):
    return self.listaVazia()
  def enQueue(self, v):
    self.insereNoFim(v)
  def deQueue(self):
    return self.retiraNoInicio()