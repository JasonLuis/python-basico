'''
1. Considerando o dicionário com o nome dos alunos e suas respectivas notas abaixo, crie uma estrutura de repetição para percorrer cada elemento do dicionário para gravar cada aluno em um novo arquivo de texto
– Cada aluno deve ocupar uma linha do novo arquivo de texto
– O formato deve ser: nome,nota (Pedro,8.0)
– Após a criação do arquivo de texto, faça a leitura do arquivo e mostre todos os alunos
'''

alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

with open('arquivos/exe8.txt','w') as arq:
  for nome, nota in alunos.items():
    r = arq.write(f"Nome: {nome} || Nota: {nota}\n")


with open('arquivos/exe8.txt','r') as text:
  for linha in text:
    print(linha)
  
    