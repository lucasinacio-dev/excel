# Autor: Lucas Inácio
# Projeto: Análise de Dados de Excel

# Import do pandas
import pandas as pd

# Ler a planilha do Excel
planilha = pd.read_excel('ocupacao.xlsx')

# Agrupar os registros por nome
resultado = planilha.groupby(["Registro", "Nome"])["Horas"].sum()

# Loop para exibir os resultados
for (registro, nome), horas in resultado.items():
    print(f"Registro: {registro}, Nome: {nome}, Total de Horas: {horas}")