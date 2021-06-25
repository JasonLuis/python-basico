#Módulos úteis

## Biblioteca Math
'''
https://docs.python.org/3/library/math.html
'''
import math

#raiz quadrado
raiz = math.sqrt(9)
print("raiz quadrada: ",raiz)

#seno
seno = math.sin(45)
print("seno: ",seno)

#coseno
coseno = math.cos(45)
print("coseno: ",coseno)

#logaritmo
logaritmo = math.log(1000, 10)
print("logaritmo: ",logaritmo)

#euler
euler = math.e
print("euler: ",euler)

#pi
pi = math.pi
print("PI: ",pi)


## Biblioteca datetime
'''
https://docs.python.org/3/library/datetime.html
'''

import datetime
#informa os recursos da biblioteca datetime
dir(datetime)

#hoje
hoje = datetime.date.today()
print("Data de Hoje: ", hoje)

#agora
agora = datetime.datetime.now()
print("Tempo atual: ",agora)

#recebndo valor como data
data = datetime.date(2020, 7, 10)
print("Formato de Data: ",data)

#pegamando os elementos
print("Dia: ", data.day)
print("Mês: ", data.month)
print("Ano: ", data.year)


#Recebendo um valor como horario
horario = datetime.datetime(2020, 7, 10, 7, 30, 0)
print("Formato em Horas: ",horario)

#pegamando os elementos
print("Horas: ",horario.hour)
print("Minutos: ",horario.minute)
print("Segundos: ",horario.second)