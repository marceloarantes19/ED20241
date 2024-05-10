from Elemento import Elemento
from No import No
from Lista import Lista
from PilhaEncadeada import PilhaEncadeada
l = Lista()
p = PilhaEncadeada()
for i in range(0, 5):
  e = Elemento(i)
  e.setNome(i)
  n = No(e)
  l.insereNoFim(n)

# Testa o Exercício 3
print("Quantidade de Elementos na lista", l.getQuantidade())

# Testa o Exercício 4
print("\nExercício 4")
l.mostraListaRec(l.getCabeca().getProximo())

# Testa o Exercício 5
print("\nExercício 5 - Invertido")
l.mostraListaInv(l.getCabeca().getProximo())

# Testa o Exercício 8
print("\nExercício 8")
l.limpaLista(l.getCabeca())
print(l.listaVazia())

# Testa o Exercício 6
i = int(input("Digite a chave (-1 para sair): "))
while i != -1:
  nome = input("Digite um nome: ")
  e = Elemento(i)
  e.setNome(nome)
  n = No(e)
  pos = int(input("Digite a posição de inserção: "))
  l.insereNaPosicao(n, pos)
  print("\nMostrando a lista após a entrada de:", i)
  l.mostraLista()
  i = int(input("Digite a chave (-1 para sair): "))

# Testa numero 7  
pos = int(input("Digite a posição de Retirada (-1 para sair): "))
while pos != -1:
  n = l.retiraNaPosicao(pos)
  if n != None:
    print("Retirado: ", n.getElemento().getValores())
  else:
    print("Nenhum elemento retirado!")
  pos = int(input("Digite a posição de Retirada (-1 para sair): "))
  

