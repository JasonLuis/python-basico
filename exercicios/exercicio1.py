"""
## Exercícios

#Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição, subtração, multiplicação e divisão

"""

a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))

print(f'A adição de de {a} + {b} é {a+b}')
print(f'A subtração de de {a} - {b} é {a-b}')
print(f'A multiplicação de de {a} * {b} é {a*b}')
print(f'A divisão de de {a} / {b} é {a/b}')

"""
##Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem
"""

print("\n\nCalculo de litro de combustivel gasto em uma viagem, utilizando um automóvel que consome 12KM por litro \n\n")


TEMPO = float(input("Digite o tempo gasto na viagem em horas: "))
VELOCIDADE = float(input("Digite a velocidade utilizada durante o percurso em KM:  "))

DISTANCIA = TEMPO * VELOCIDADE
LITROS_USADOS = DISTANCIA / 12
print("A quantidade de litros gasta é: ",round(LITROS_USADOS,1))


