'''
1. Crie uma classe chamada aluno com os seguintes atributos:
– Nome
– Nota 1
– Nota 2
– Crie um construtor para a classe (__init__)
2. Crie as seguintes funções (métodos):
– Calcula média, retornando a média aritmética entre as notas
– Mostra dados, que somente imprime o valor de todos os atributos
– Resultado, que verifica se o aluno está aprovado ou reprovado (se a média for maior ou igual a 6.0, o aluno está aprovado)
3. Crie dois objetos (aluno1 e aluno2) e teste as funções
'''

class Aluno:
  def __init__(self, nome, nota1, nota2):
    self.nome = nome
    self.nota1 = nota1
    self.nota2 = nota2
  
  def mediaAritimetica(self):
    media = (self.nota1 + self.nota2)/2
    return media
  
  def resultado(self):
    print(f"Nome do Aluno: {self.nome}")
    print(f"Nota 1: {self.nota1}")
    print(f"Nota 2: {self.nota2}")
    print(f"Media: {self.mediaAritimetica()}")
    if(self.mediaAritimetica() >= 6):
      print("Status: Aprovado")
    else:
      print("Status: Reprovado")
    
  
a1 = Aluno('Jason', 10, 10)
a1.resultado()

a2 = Aluno('Vilsom', 5, 6)
a2.resultado()