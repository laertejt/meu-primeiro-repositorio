import pandas as pd
# file = "cadastro_alunos.xlsx"
file = "imoveis_brasil.csv"
df = pd.read_csv(file)
# 1.	Mostrar as 5 primeiras e as 5 ultimas linhas do DataFrame. Use também df.sample(5) e verifique qual o resultado.
df.head(5)
df.tail(5)
df.sample(5)
# 2.	Exibir o número de linhas e colunas com shape.
df.shape
# 3.	Listar os nomes das colunas.
df.columns
# 4.	Mostrar os tipos de dados de cada coluna.
df.dtypes
# 5.	Usar describe() para ver estatísticas das colunas numéricas.
df.describe()
# 6.	Usar info() para ver informações gerais.
df.info()
# 7.	Verifique quais os tipos de imóveis que temos na amostra.
df["Tipo_Imovel"].unique()
# 8.	Filtrar imóveis com valor acima de R$ 1.000.000,00.
filtro = df["Valor_Imovel"]>1000000
df.loc[filtro]
# 9.	Selecionar as colunas cidade, bairro, e valor em um novo DataFrame chamado df2
coluna = [ 'Cidade', 'Bairro',  'Valor_Imovel']
df[coluna]
# 10.	Filtrar os imóveis da cidade de Curitiba e gravar em um novo df_curitiba
filtro = df["Cidade"]=="Curitiba"
df.loc[filtro]
# 11.	Verificar valores nulos em cada coluna com isnull().sum().
df.isnull().sum()
# 12.	Ordenar os 10 imóveis mais caros (coluna valor decrescente).
df.sort_values("Valor_Imovel", ascending=False)
# 13.	Qual é o valor médio (média) dos imóveis no dataset?
df["Valor_Imovel"].mean()
# 14.	Qual é o valor mediano (mediana)?
df["Valor_Imovel"].median()
# 15.	Qual é o desvio padrão do valor dos imóveis?
df["Valor_Imovel"].std()
# 16.	Mostre o valor mínimo e o valor máximo de área construída (ou variável similar).
df["Area_m2"].min()
df["Area_m2"].max()
# 17.	Quantos imóveis estão abaixo do valor médio e quantos estão acima?
media = df["Valor_Imovel"].mean()
filtro = df["Valor_Imovel"]>media
df.loc[filtro]
# 18.	Adicionar uma nova coluna chamada valor_m2 que divide o valor pela area.
valor = df["Valor_Imovel"]
area = df["Area_m2"]
df["valor_m2"] = valor / area
# 19.	Inserir uma linha fictícia no final do DataFrame, 
# com um imóvel da cidade "Teste", valor 999999 e área 100.
dic = {"Cidade": "Teste", "Valor_Imove":999, "Area_m2":100}
df.loc[len(df)] = dic
# 20.	Verificar valores nulos novamente.
df.isnull().sum()
# 21.	Remover todos os imóveis com valor Numero_Quartos=5
filtro = df["Numero_Quartos"]!=5
df = df.loc[filtro]
# 22.	Excluir a coluna ID_Imovel
df.drop(columns=["ID_Imovel"])
# 23.	Remover os imóveis da cidade "Teste".
filtro = df["Cidade"]!="Teste"
df = df.loc[filtro]
# 24.	Agrupar por cidade e calcular média de valor dos imóveis.

