"""
# Exercício 1 

## Lista: Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os armazene dentro de uma lista. Após a leitura, crie outra estrutura de repetição para somar todos os valores digitados

"""
lista = []
for i in range(1,6):
  numero = int(input("Digite um numero: "))
  lista.append(numero)

total = 0
for i in lista:
  total += i

print("Total: ",total)
  

"""
# Exercício 2 

## Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos, fazendo a leitura dos valores por meio de uma estrutura de repetição. Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média

"""

aluno = {}

for item in range(1,4):
  nome = input("Digite o nome do aluno: ")
  nota = float(input("Digite a nota: "))
  aluno[nome] = nota

total = 0

for i in aluno.values():
    total += i

print("A media é: ",round((total/3),1))



"""
# Exercício 3 

## Matriz: Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz

"""
import numpy as np

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])

total = 0

for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
      total += matriz[i][j]

print("O resultado da soma da matriz é: ",total)