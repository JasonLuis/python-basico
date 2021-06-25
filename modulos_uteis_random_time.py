## Biblioteca random
'''
https://docs.python.org/3/library/random.html
'''

import random

#imprimir um numero randomico
randomico = random.random()
print(randomico)

#imprimir um numero randomico de 1 a 10
numero = random.randint(1,10)
print(numero)


#imprimir um numero randomico de 0 a 10 multiplos de 3
numero = random.randrange(0,10,3)
print(numero)

#escolher um elemento aleatorio de uma lista com random

x = ['K', 'd', 13, '34-j', 'x']
valor = random.choice(x)
print("Valor pego da lista: ",valor)

## Biblioteca time
'''
https://docs.python.org/3/library/time.html
'''

import time as tm

# retorna o tempo atual em segundos
atual = tm.time()
print("Tempo atual em segundos: ", atual)

#informando o tempo que um codigo levou para executar
antes = tm.time()
lista = []
for i in range(0,10000):
  lista.append(i)
depois = tm.time()
intervalo = depois - antes
print(f'Tempo: {intervalo} segundos')

#criando um pequeno loading com time
print('Finalizando...')
tm.sleep(2)
print('...')
tm.sleep(2)
print('Até a próxima')