'''
Criar um Menu com opções dentro de laço:
#click_vizinho()
#click_guilda()
#click_amigos()
todos 
sair
'''


opcao = 0
while opcao != 5:
    print('''
          [ 1 ] Clicar nos Vizinhos
          [ 2 ] Clicar na Guilda
          [ 3 ] Clicar nos Amigos
          [ 4 ] Todas as opções
          [ 5 ] Sair do programa
            ''')
    opcao = int(input('>>>>>>>>>> Qual é a sua opção?  '))
    if opcao == 1:
        print('opção 1')
        #click_vizinho()
    elif opcao == 2:
        print('opção 2')
        #click_guilda()
    elif opcao == 3:
        print('opção 3')
        #click_amigos()
    elif opcao == 4:
        print('opção 4 - Todos')
        #click_vizinho()
        #click_guilda()
        #click_amigos()
    elif opcao == 5:
        print('saindo....')
    else:
        print('Opção inválida. Tente novamente!')
        print('=-=' * 15)
print('Fim do programa!')

