from ArvoreBB import ArvoreBB
a = ArvoreBB()
x = int(input("Digite um valor para inserir na árvore (-1 para sair): "))
while x != -1:
  a.insereNoChave(x)
  a.preOrdem(a.getRaiz())
  x = int(input("Digite um valor para inserir na árvore (-1 para sair): "))
print("Teste de Entrada Finalizado")
