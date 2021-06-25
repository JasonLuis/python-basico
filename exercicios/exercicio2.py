"""
# Exercícios

## Leia a idade do usuário e classifique-o em:
– Criança – 0 a 12 anos
– Adolescente – 13 a 17 anos
– Adulto – acima de 18 anos
-Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida

"""

idade = int(input("Digite sua idade: "))

if idade <=12:
  print("Você é uma criança.")
elif idade <=17:
  print("Você é um adolescente.")
else:
  print("Você é um adulto.")



"""
## Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas M1, M2 e M3; passando por um cálculo da média aritmética. Após a média calculada, devemos anunciar se o aluno foi aprovado, reprovado ou pegou exame
– Se a média estiver entre 0.0 e 4.0, o aluno está reprovado
– Se a média estiver entre 4.1 e 6.0, o aluno pegou exame
– Se a média for maior do que 6.0, o aluno está aprovado
– Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0, está aprovado, senão; está reprovado
"""

m1 = float(input("Digite a nota 1 do aluno: "))
m2 = float(input("Digite a nota 2 do aluno: "))
m3 = float(input("Digite a nota 3 do aluno: "))

media = (m1+m2+m3) / 3

if media <= 4:
  print("aluno reprovado.")
elif media <= 6:
  print("aluno pegou exame.")
else:
  print("aluno aprovado.")

