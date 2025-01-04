from random import randint
from time import sleep
from operator import itemgetter
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

jogo = {'jogador1': randint(1, 6),
       'jogador2': randint(1, 6),
       'jogador3': randint(1, 6),
       'jogador4': randint(1, 6)}
       
ranking = list()
print(f"\n{color['green']}      Valores sorteados: {color['reset']}")

for k, v in jogo.items():
    print(f'    {k} tirou {v} no dado.')
    sleep(1)
    
print('\n')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 20)
print(f'\n {color['magenta']} == RANKING DOS JOGADORES == {color['reset']}')
for i, v in enumerate(ranking):
    print(f'{color['blue']}    {i+1}º lugar: {v[0]} com {v[1]}. {color['reset']}')
    sleep(1)
print('\n')
print(f'\n                   {color['yellow']} Fim.... {color['reset']}\n')

