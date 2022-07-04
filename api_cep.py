''' Requests officially supports Python 2.7 & 3.6'''

import requests
import os

os.system('cls')


def pegar_cotacoes():
 
    busca_cep = 31160550
    requisicao = requests.get('https://correios.contrateumdev.com.br/api/busca_cep')

    requisicao_dic = requisicao.json()
    print(requisicao_dic)
    
    # bairro = requisicao_dic['USDBRL']['bid']
    # cep = requisicao_dic['EURBRL']['bid']
    # cidade = requisicao_dic['BTCBRL']['bid']
    # complemento = []
    # logradouro = []
    # uf = []

    # texto = f'''
    # Bairro: {bairro}
    # CEP:  {cep}
    # Cidade: {cidade}
    # Complemento: {complemento}
    # Logradouro: {logradouro}
    # uf: {uf}
    # '''

    print(texto, '\n')


pegar_cotacoes()
