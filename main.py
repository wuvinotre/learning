import os
import requests
import filter_urls
import pandas as pd
import matplotlib.pyplot as plt

link = os.environ['LIVEID_IMAGES']
request = requests.get(link)

data_json = request.json()

dataFiltered = filter_urls.filter_urls_csv(data_json)
dataFilteredSuccess = filter_urls.filter_urls_csv_success(data_json)
for url in dataFilteredSuccess[-10:]:
    df = pd.read_csv(url)
    line_25 = df.iloc[23]
    media_lines = df.mean(axis=0)
    plt.figure(figsize=(10, 6))
    plt.plot(line_25, label='Linha 25')
    plt.plot(media_lines, label='Média')
    plt.xlabel('Índice da Linha')
    plt.ylabel('Valor')
    plt.title('Gráfico da Linha 25 e Média de Todas as Linhas')
    plt.legend()
    plt.grid(axis='y')
    # plt.show()


# show all
plt.show()
