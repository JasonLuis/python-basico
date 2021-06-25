"""
# Exercícios

## Ler 5 notas e informar a média

"""
nota = 0
for index in range(1,6):
  nota += float(input(f"Digite a nota {index} do aluno: "))

print("A media é: ",(nota/5))

"""
## Imprimir a tabuada do número 3 (3 x 1 = 1 – 3 x 10 = 30)
"""
print()
index = 0
while index <= 10:
  print(f"3 x {index} = ",(3 * index))
  index += 1



