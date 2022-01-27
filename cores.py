nome = ' Augusto '
cores = {'limpa':'\033[m',
          'azul':'\033[34m',
          'amarelo':'\033[33m',
          'vermelho':'\033[31m',
          'verde':'\033[32m',
          'roxo':'\033[35m',
          'cian':'\033[36m',
          'cinza':'\033[37m',
          'pretoeamarelo':'\033[7;33m'}


# print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoeamarelo'], nome, cores['limpa']))
print('-=' * 30)
print()
print(f"    Olá! Muito prazer em te conhecer, {cores['pretoeamarelo']}{nome}{cores['limpa']}!!!")
print()
print('-=' * 30)
