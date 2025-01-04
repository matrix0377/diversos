# Curso em Vídeo - Gustavo Guanabara
# site: 


import os
from random import randint
from time import sleep
from colorama import init, Fore, Back, Style
init()

os.system('cls')
lista = list()
jogos = list()
print('-' * 42)
print(Fore.MAGENTA + '     JOGA NA MEGA SENA     ' + Fore.RESET)
print('-' * 42)
quant = int(input('quantos jogos você quer que eu sorteie? '))
print()
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print()
    print(Fore.CYAN + f'JOGO {i+1}: {l}' + Fore.RESET)
    sleep(1)

print()
print('-=' * 7, '< BOA SORTE! >', '-=' * 7)
print("\n")
    