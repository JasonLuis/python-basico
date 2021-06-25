"""
##Coleções

#Dicionários

"""
coleta = {
  'Aedes aegypt': 32,
  'Aedes albopictus': 22,
  'Anopheles darlingi': 14
  }
print(coleta['Aedes aegypt'])

coleta['Rhodnius montenegrensis'] = 11
print(coleta)

del(coleta)['Aedes albopictus']
print(coleta)

#retorna os items do dicionario
print(coleta.items())

#retorna as chaves
print(coleta.keys())

#retorna os valores
print(coleta.values())

coleta2 = {'Anopheles gambiae': 13,'Anopheles deaneorum': 14}
print(coleta2)

coleta.update(coleta2)
print(coleta)

print(coleta.items())

for especie, num_especimes in coleta.items():
  print(f'Espécie: {especie}, número de espécimes coletados: {num_especimes}')


"""
##Conjuntos(set)

"""

biomoleculas = ('proteína','ácidos nucleicos','carboidrato', 'lipídeo',
                'ácidos nucleicos','carboidrato','carboidrato','carboidrato')

print(biomoleculas)

print(set(biomoleculas))

c1 = {1,2,3,4,5}
c2 = {3,4,5,6,7}
#so retornarão os numeros que se encontram nos conjuntos em c1 e tambem em c2
c3 = c1.intersection(c2)

print(c3)

#so retornarão os numeros que tem no conjunto c1, mas não no c2 e tem no c2, mas não se encontram em c1
c3 = c1.difference(c2)

print(c3)