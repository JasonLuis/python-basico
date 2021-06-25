## Manipulação de arquivos

with open('arquivos/frase1.txt','r') as tex: 
  for linha in tex:
    print(linha)

with open('arquivos/frase1.txt','r') as tex: 
  r = tex.readlines()
  print(r)

with open('arquivos/texto2.txt','w') as texto:
  texto.write('Programação is very god')

with open('arquivos/texto2.txt','r') as tex: 
  r = tex.readlines()
  print(r)

