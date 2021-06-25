"""
##Coleções

#Tuplas

"""

tupla = ('Homo sapiens', 'Canis familiaris', 'Felis catus')

print(tupla)
print(tupla[0])

print(tupla.index('Canis familiariss'))

for elemento in tupla:
  print(elemento)


"""
#Lista
"""

l1 = ['Homo sapiens', 'Canis familiaris', 'Felis catus']
l2 = ['Xenopus laevis', 'Ailuropoda melanoleuca']
l3 = l1 + l2
print(l3)

print(l2)

l2_2 = l2 * 2

print(l2_2)

print(l1[0]) 
print(l1[0:2]) 
 
#insere um novo elemnto na lista
l1.append('Gorila gorila')
print(l1)

#remover um elemento da lista
l1.remove('Felis catus')
print(l1)

#apagar uma lista inteira
del(l1)

for item in l2_2:
  print(item)


