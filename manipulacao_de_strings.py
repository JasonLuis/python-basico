# -*- coding: utf-8 -*-
"""Manipulação de variáveis e constantes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zHkg0u422FxA96zsOwEVcSf8X6GtEQ7G
# Manipulação de strings
"""


a = 'casaco'
print(a)

maiuscula = a.upper()
print(maiuscula)

minuscula = maiuscula.lower()
print(minuscula)

capital = a.capitalize()
print(capital)

metade_palavra = a[0:3]
print(metade_palavra)

ultimas_letras = a[3:]
print(ultimas_letras)

b = a.replace('aco', 'inha')
print(a)
print(b)

c = a.replace('o', 'a')
print(c)

print(c.find('b'))

e = ' casaco '
print(len(e))

f = e.strip()
print(f)
print(len(f))

n1 = 14
n2 = 16

print(f'Dividindo {n1} por {n2} o resultado é {n1/n2}')
