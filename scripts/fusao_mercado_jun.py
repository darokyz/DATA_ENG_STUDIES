import json
import csv
from processamento_dados import Dados


# PS PRA MIM MESMO PRESTA ATENÇAO NA INDENTAÇAOOOO INFERNOOO
# def leitura_json(path_json):
#     dados_jason = []
#     with open(path_json, 'r') as file:
#         dados_jason = json.load(file)
#     return dados_jason
    

# def leitura_csv(path_csv):
# #transformando a lista de listas em uma lista de dicionario DictReader != reader
#     dados_csv = []
#     with open(path_csv,'r') as file:
#         spamreader = csv.DictReader(file, delimiter=",")
#         for linha in spamreader:
#             dados_csv.append(linha)
#     return dados_csv


# def leitura_dados(path, tipo_arquivo):
    
#     dados = []
#     if tipo_arquivo == 'csv':
#        dados = leitura_csv(path)

#     elif tipo_arquivo == 'json':
#         dados = leitura_json(path)
#     return dados


# def get_columns(dados):
#     return list(dados[-1].keys())


# def rename_columns(dados, key_mapping):
    
#     new_dados_csv = []
    
#     for old_dict in dados:
#         dict_temp = {}
#         for old_key, value in old_dict.items():
#             dict_temp[key_mapping[old_key]] = value
#         new_dados_csv.append(dict_temp)
#     return new_dados_csv


# def size_data(dados):
#     return len(dados)


# def join(dadosA, dadosB):

#     combined_list = []

#     combined_list.extend(dadosA)
#     combined_list.extend(dadosB)
#     return combined_list


# def transformar_dados_tabela(dados, nomes_colunas):
    
#     dados_combinados_tabela = [nomes_colunas]
#     for row in dados:
#         linha = []
#         for coluna in nomes_colunas:
#             linha.append(row.get(coluna, 'Indisponivel'))
#         dados_combinados_tabela.append(linha)
#     return dados_combinados_tabela


# def salvar_csv(dados, path):

#     with open(path, 'w') as file:
#         writer = csv.writer(file)
#         writer.writerows(dados)


# INICIANDO A LEITURA DOS DADOS...
# dados_json = leitura_dados(path_json, 'json')
# nomes_colunas_json = get_columns(dados_json)
# tamanho_json = size_data(dados_json)

# print(f"nome colunas json: {nomes_colunas_json}")
# print(f"Tamanho json: {tamanho_json}")

# dados_csv = leitura_dados(path_csv,'csv')
# nomes_colunas_csv = get_columns(dados_csv)
# tamanho_csv = size_data(dados_csv)

# print(f"nome colunas csv: {nomes_colunas_csv}")
# print(f"Tamanho csv: {tamanho_csv}")


# # NEXT KKK BORA DE TRANSFORMAÇAO DE DADOS -- -- -- -- -- 
# # VARIAVEL PARA SUBSTITUIR OS NOMES DA COLUNA DO CSV PELOS MESMOS DO JSON
# key_mapping = {'Nome do Item':'Nome do Produto',
#             'Classificação do Produto':'Categoria do Produto',
#             'Valor em Reais (R$)': 'Preço do Produto (R$)',
#             'Quantidade em Estoque': 'Quantidade em Estoque',
#             'Nome da Loja':'Filial',
#             'Data da Venda': 'Data da Venda'
#             }


# # ULTILIZANDO AS FUNÇOES PARA FAZER A TROCA DO NOME DAS COLUNAS DO CSV PARA OS MSM DO JSON 
# dados_csv = rename_columns(dados_csv, key_mapping)
# new_names_columns_CSV = get_columns(dados_csv)
# print(new_names_columns_CSV)


# #  FUSAO
# dados_da_fusao = join(dados_json, dados_csv)
# nome_colunas_fusao = get_columns(dados_da_fusao)
# tamanho_fusao = size_data(dados_da_fusao)
# print(nome_colunas_fusao)
# print(tamanho_fusao)

# #  SALVANDO OS DADOS

# dados_fusao_tabela = transformar_dados_tabela(dados_da_fusao, nome_colunas_fusao)
# path_dados_combinados = 'data_processed/dados_combinados_scritpCOMP.csv'

# salvar_csv(dados_fusao_tabela, path_dados_combinados)
# print(path_dados_combinados)
