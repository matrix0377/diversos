# Cadastro de Trabalhador em Python
# Calcula em quantos anos o trabalhador se aposenta
# Levamos em consideração apenas 35 anos, independente do sexo, somente exercício
# cores: colorama {color['green']}

from datetime import datetime
import os
from colorama import Fore, init
init()

os.system('cls')

color = {
    'yellow': Fore.YELLOW,
    'blue': Fore.BLUE,
    'green': Fore.GREEN,
    'red': Fore.RED,
    'magenta': Fore.MAGENTA,
    'cian': Fore.CYAN,
    'reset': Fore.RESET}

dados = dict()
print(f'\n {color['magenta']}  === Cadastro de Trabalhador em Python  === {color['reset']} \n')
dados['nome'] = str(input(f'{color['green']} Nome: {color['reset']}'))
nasc = int(input(f'{color['green']} Ano de Nascimento: {color['reset']}'))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input(f'{color['red']} Carteira de Trabalho (0 não tem): {color['reset']}'))
if dados['ctps'] != 0:
    dados['contratação'] = int(input(f'{color['green']} Ano de Contratação: {color['reset']}'))
    dados['salário'] = float(input(f'{color['green']} Salário: R$ {color['reset']}'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'    - {color['green']} {k} {color['reset']} tem o valor: {color['blue']} {v} {color['reset']}')

print(f'\n                          {color['yellow']} Fim.... {color['reset']}\n')
