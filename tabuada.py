# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

import os

def tabuada():
    num =int(input('Digite um número para ver a sua tabuada: '))
    os.system('cls')
    print('='*30)
    print('=====   Tabuada do {}    ====== '.format(num))
    print('='*30)
    print('\n')
    print('{} x {:2} = {}'.format(num, 1, num*1))
    print('{} x {:2} = {}'.format(num, 2, num*2))
    print('{} x {:2} = {}'.format(num, 3, num*3))
    print('{} x {:2} = {}'.format(num, 4, num*4))
    print('{} x {:2} = {}'.format(num, 5, num*5))
    print('{} x {:2} = {}'.format(num, 6, num*6))
    print('{} x {:2} = {}'.format(num, 7, num*7))
    print('{} x {:2} = {}'.format(num, 8, num*8))
    print('{} x {:2} = {}'.format(num, 9, num*9))
    print('{} x {:2} = {}'.format(num, 10, num*10))
    print()
    print('Fim ....')
    print()

opcao = 0
while opcao != 2:
    print()
    print('''
          [ 1 ] Calcular tabuada
          [ 2 ] Sair do programa
            ''')
    opcao = int(input('>>>>>>>>>> Qual é a sua opção?  '))
    if opcao == 1:
        print('opção 1')
        tabuada()
    
    elif opcao == 2:
        print('saindo....')
        break
    else:
        print('Opção inválida. Tente novamente!')
        print('=-=' * 15)
print('Fim do programa!')






