import json
import csv
from processamento_dados import Dados


# CAMINHOS...
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'


dados_empresaA = Dados(path_json, 'json')
print(dados_empresaA.qtd_linhas)
print(dados_empresaA.nome_colunas)


dados_empresaB = Dados(path_csv, 'csv')
print(dados_empresaB.qtd_linhas)
print(dados_empresaB.nome_colunas)


dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(dados_fusao)
print(dados_fusao.qtd_linhas)
print(dados_fusao.nome_colunas)


#LOAD
path_dados_combinados = 'data_processed/dados_combinados_scritpCOMP.csv'
dados_fusao.salvar_dados(path_dados_combinados)
print(path_dados_combinados)