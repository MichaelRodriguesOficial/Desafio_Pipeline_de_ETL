import datetime
import pandas as pd

# Entrada dos arquivos
entrada = pd.read_csv("Entrada de dados/Brasileirao.csv")

# Extração dos dados
times = entrada['TIME']
pontos = entrada['P']
porcentagem = entrada['%']

# Cria lista de IDs sequenciais
ids = list(range(1, len(times) + 1))

# Data da extração
data_atual = datetime.date.today()
data = data_atual.strftime("%d/%m/%Y")

# Criar um excel com as listas de dados
dados = pd.DataFrame({'ID': ids, 'Time': times, 'Pontos': pontos, "% de Título": porcentagem, 'Data de entrada': data})

# Salvar os dados em um arquivo XLSX
dados.to_excel('Dados transformados/Brasileirao.xlsx', index=False)
