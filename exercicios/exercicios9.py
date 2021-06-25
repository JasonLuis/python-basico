'''
Crie expressões regulares para extrair as seguintes informações do texto abaixo (use a função findall):
– Números
– CEPs
– URLs
'''
texto = "Minha casa fica na rua Carneiro, 78. O CEP é 88388-000 e 11111-111 meu site é https://www.iaexpert.academy http://iaexpert.com.br"

import re 

numeros = re.findall('\d', texto)
print(numeros)

cep = re.findall('\d{5}-\d{3}', texto)
print(cep)

urls = re.findall('https?://[A-Za-z0-9./]+', texto)
print(urls)