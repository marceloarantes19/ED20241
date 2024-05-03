from Elemento import Elemento
from No import No
from Lista import Lista
l = Lista()
i = int(input("Digite a chave (-1 para finalizar a entrada): "))
while i != -1:
  nome = input("Digite um nome: ")
  e = Elemento(i)
  e.setNome(nome)
  n = No(e)
  l.insereOrdenadoChave(n)
  print("\nMostrando a lista após a entrada de:", i)
  l.mostraLista()
  i = int(input("Digite a chave (-1 para finalizar a entrada): "))
i = int(input("Digite a chave de saída (-1 para finalizar a saída): "))
while not l.listaVazia() and i != -1:
  x = l.retiraNoChave(i)
  if x != None:
    print(x.getElemento().getValores())
  else:
    print("Chave", i, "não encontrada na lista.")
  print("Lista após operação")
  l.mostraLista()
  i = int(input("Digite a chave de saída (-1 para finalizar a saída): "))
