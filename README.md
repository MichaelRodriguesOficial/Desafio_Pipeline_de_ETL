## Desafio de Extração e Transformação de Dados


Neste projeto, você irá criar um script Python para extrair dados de uma planilha CSV, realizar transformações nesses dados e, em seguida, criar uma nova planilha em formato XLSX com os dados transformados. 

Foi adicionado um ID sequencial e a data de importação a nessa nova planilha. 

Abaixo, você encontrará um guia de como usar o código e informações adicionais relevantes.

#### Passos para Execução

Siga os passos abaixo para executar o código e realizar a extração e transformação de dados:

1 - Pré-requisitos: Certifique-se de ter Python instalado em seu sistema. Você também precisa ter as bibliotecas pandas e datetime instaladas. Você pode instalá-las usando o pip:


```bash
  pip install pandas
```


2 - Estrutura do Diretório: Certifique-se de que sua estrutura de diretório seja semelhante à seguinte:

```bash
projeto/
├── Entrada de dados/
│   └── Brasileirao.csv
├── Dados transformados/
│   └── Brasileirao.xlsx
├── seu_script.py
└── README.md
```
- Coloque sua planilha de entrada Brasileirao.csv na pasta Entrada de dados.

- O arquivo de saída, Brasileirao.xlsx, será gerado na pasta Dados transformados.


3 - Execute o Script: Execute o script Python seu_script.py que contém o código que você forneceu. Certifique-se de que ele está no mesmo diretório que os arquivos de entrada e saída.

```bash
python seu_script.py

```

4 - Resultados: Após a execução bem-sucedida, você encontrará um novo arquivo Brasileirao.xlsx na pasta Dados transformados com os dados extraídos, o ID sequencial e a data de importação.

### Estrutura do Código
Aqui está uma visão geral da estrutura do código:

```bash
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

# Criar um Excel com as listas de dados
dados = pd.DataFrame({'ID': ids, 'Time': times, 'Pontos': pontos, "% de Título": porcentagem, 'Data de entrada': data})

# Salvar os dados em um arquivo XLSX
dados.to_excel('Dados transformados/Brasileirao.xlsx', index=False)
```

### Conclusão

Este script permite que você automatize o processo de extração, transformação e exportação de dados de uma planilha CSV para uma planilha XLSX, tornando-o útil para tarefas de análise de dados e relatórios.

