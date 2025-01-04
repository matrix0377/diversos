# Curso em Vídeo - Gustavo Guanabara 03/01/2025
# Exercício Python #094 - Unindo Dicionário e listas

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

galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f' {color['magenta']}{p["nome"]} {color['reset']}', end='')
print()
print('D) Lista das mulheres que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('     ', end='')
        for k, v in p.items():
            print(f' {color['green']} {k} {color['reset']} = {v}; ', end='')
        print('\n')
print('<< ENCERRADO >>')

