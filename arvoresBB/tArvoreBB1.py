from ArvoreBB import ArvoreBB
a = ArvoreBB()
x = int(input("Digite um valor para inserir na árvore (-1 para sair): "))
while x != -1:
  a.insereNoChave(x)
  a.emOrdem(a.getRaiz())
  x = int(input("Digite um valor para inserir na árvore (-1 para sair): "))
print("Teste de Entrada Finalizado")
x = int(input("Digite um valor para retirar da árvore (-1 para sair): "))
while x != -1:
  n = a.remove(x)
  if n != None:
    print("Dados do nó removido:", n.getValores())
  else:
    print("Valor não encontrado na árvore!")
  print("Árvore atual: ")
  a.emOrdem(a.getRaiz())
  x = int(input("Digite um valor para retirar da árvore (-1 para sair): "))

print("Fim do Teste!")