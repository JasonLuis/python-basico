## Funções 

# * Trechos de programa que recebem um determinado nome e podem ser chamados várias vezes durante a execução
# * Pricipais vantagens: reutilização de código, modularidade e facilidade de manutenção do sistema


# Função sem parâmetro e sem retorno

def mensagem():
  print('apenas texto')

mensagem()


# Função com passagem de parâmetro

def mensagem(texto):
  print(texto)

mensagem('texto')

def soma(a,b):
  print(a + b)

soma(2,5)

# Função com passagem de parâmetro e retorno

def soma(a,b):
  return a + b

r = soma(5, 5)

print(r)

def calcula_energia_potencial_gravitacional(m, h, g = 10):
  '''
    imagine que aqui tem uma documentação desta função
  '''
  e = g * m *h
  return e

e = calcula_energia_potencial_gravitacional(30, 12)
print(e)

e = calcula_energia_potencial_gravitacional(30, 12,9.8)
print(e)
help(calcula_energia_potencial_gravitacional)