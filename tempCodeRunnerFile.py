'''
Serve para calcular tempo de execução de um programa
'''

import datetime
import time
# insira o tempo logo abaixo dos imports
tempo_inicial = datetime.datetime.now().time().strftime('%H:%M:%S')

print('.....' * 15)
print('---------->>>> tempo para esse teste de 5 segundos')
time.sleep(5) # tempo para esse teste de 5 segundos

tempo_final = datetime.datetime.now().time().strftime('%H:%M:%S')
tempo_total=(datetime.datetime.strptime(tempo_final,'%H:%M:%S') - datetime.datetime.strptime(tempo_inicial,'%H:%M:%S'))

# print com os tempos
print('.....' * 15)
print('                HH : MM : SS')
print(' ')
print('Tempo inicial: ', tempo_inicial)
print('Tempo final  : ', tempo_final)
print('Tempo TOTAL  :  ', tempo_total)

