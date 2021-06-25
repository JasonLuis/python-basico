'''

# 1. Crie uma lista vazia e faça a leitura de dois valores do tipo float,
colocando cada um dos valores nas primeiras posições da lista
(o valor1 ficará na posição 0 da lista e o valor2 ficará na posição 1 da lista).
Faça a divisão dos dois valores e trate as seguintes exceções:

# 2. Mostre uma mensagem personalizada na ocorrência de cada um desses erros

'''

lista = []

while True:
  try:
    lista.append(float(input('Digite um número: ')))
    lista.append(float(input('Digite outro número: ')))
    resultado = lista[0] / lista[1]
  except ValueError:
    print('Valor inválido')
  except ZeroDivisionError:
    print('Divisão invalida')
  except IndexError:
    print('Posição inexistente')
  except KeyboardInterrupt:
    print('Usuário interrompeu a execução')
    break
  else:
    print(f'Resultado da divisão: {resultado}')
    break