from PilhaEncadeada import PilhaEncadeada
from Elemento import Elemento
from No import No
p = PilhaEncadeada()
num = int(input('Digite um natural: '))
x = num
y = ''
while x > 0:
  e = Elemento(x % 2)
  n = No(e)
  p.push(n)
  x = x // 2
while not p.pilhaVazia():
  y = y + str(p.pop().getElemento().getChave())
print(num, ' = ', y)

