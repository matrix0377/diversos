''' 
Como pegar minhas variáveis de Ambiente
'''

import os

cor = {'limpa': '\033[m',
       'azul': '\033[34m',
       'amarelo': '\033[33m',
       'verde': '\033[32m',
       'lilas': '\033[35m',
       'branco': '\033[37m',
       'vermelho': '\033[31m',
       'cian': '\033[36m'
       }

os.system('cls')

# print(os.environ)
for k, v  in enumerate(os.environ.items()):
    print(f" {k} : -->>>> {v}")


print('\n------------------------------------------------\n')
print(os.environ["COMPUTERNAME"])
print(os.environ["PROCESSOR_ARCHITECTURE"])
print('\n------------------------------------------------\n')
