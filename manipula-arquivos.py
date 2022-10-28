# Listar arquivos
import os 
import shutil

os.system('cls')

cores = {'limpa':'\033[m',
          'azul':'\033[34m',
          'amarelo':'\033[33m',
          'vermelho':'\033[31m',
          'verde':'\033[32m',
          'roxo':'\033[35m',
          'cian':'\033[36m',
          'cinza':'\033[37m',
          'pretoeamarelo':'\033[7;33m'}

# lista diretório
print(" ")
arquivos = os.listdir()
print(f"{cores['vermelho']} ======================= List do Diretório =========================== {cores['limpa']}")
print("\n")
print(arquivos)

# caminho da pasta
caminho = os.getcwd()
print(" ")
print(f"\n --->>>> {cores['amarelo']} caminho:{cores['limpa']} {cores['cian']} {caminho} {cores['limpa']}")
print(" ")

# Renomear
# os.rename('Vendas - 1.xlsx', 'Vendas 1.xlsx')

# Mover
# os.rename('Vendas - 1.xlsx', 'Vendas\Vendas - 1.xlsx')

# Copiar arquivos
# import shutil
# shutil.copy2()

print(f"\n {cores['vermelho']} ================= Lista arquivos do Diretório em colunas =================== {cores['limpa']}")

lista_arquivos = os.listdir()
for arquivo in lista_arquivos:
    print(arquivo)

# Organizar os arquivos em suas devidas pastas
# lista_arquivos = os.listdir()
# for arquivo in lista_arquivos:
#     if 'xlsx' in arquivo:
#         if "Compras" in arquivo:
#             # jogar para a pasta de compras
#             os.rename(arquivo, f'Compras\{arquivo}')
              # ou se quiser pode usar a sintaxe com '//'
              # os.rename(arquivo, f'Compras//{arquivo}')
#         elif "Vendas" in arquivo:
#             # jogar para a pasta de vendas
#             os.rename(arquivo, f'Vendas\{arquivo}')



