"""
## Estrutura de repetição – for

"""

print(1)
print(2)
print(3)
print(4)
print(5)

for numero in range(1, 6):
  print(numero)

5 + 4 + 3 + 2 + 1

print("\n\n")
for numero in range(5, 0, -1):
  print(numero)

print("\n\n")
soma = 0
for numero in range(1, 6):
  soma = soma + numero
  #print(soma)

print(soma)

print("\n\n")
palavra = 'sorvete'
for letra in palavra:
  #print(letra)
  if letra == 'v':
    print('Achou a letra v')

print("\n\n")
for i in range(0,5):
  print(i)
  print('---')
  for j in range(0,3):
    print(j)
  print()


