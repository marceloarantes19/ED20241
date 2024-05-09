from Elemento import Elemento
from No import No
from Lista import Lista
l = Lista()
for i in range(0, 10):
  e = Elemento(i)
  e.setNome(i)
  n = No(e)
  l.insereNoFim(n)
l.mostraLista()
print("Quantidade de Elementos na lista", l.getQuantidade())
