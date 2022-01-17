""" função e retorno de valores """

def soma(n1, n2):
    num = n1 * n2
    return print(f"A multiplicação entre {n1} e {n2} é {num}")

    # return print('A multiplicação entre {} e {} é {}'.format(n1, n2, num))
    # return print('A soma vale:', num)
    

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

soma(n1, n2)


