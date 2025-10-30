import matplotlib.pyplot as plt
import pandas as pd
file="empresas_desempenho.csv"
df=pd.read_csv(file)
df.head()
# Grafico de Linha
filtro = df["Setor"]=="Comércio"
df_com = df.loc[filtro]
plt.figure(figsize=(8, 5))

# Ajustando o estilo da linha com cor extravagante e marcador
plt.plot(df_com["Ano"], df_com["Receita"], color='blue', linewidth=3, marker='o', markerfacecolor='yellow', markersize=8)
# Títulos e labels com cores vibrantes
plt.title("Gráfico de Linha Receita x Ano", fontsize=16, color='black', fontweight='bold')
plt.xlabel("Ano", fontsize=14, color='lime')
plt.ylabel("Receita", fontsize=14, color='lime')
# Alterar o fundo do gráfico e das áreas de texto
plt.gca().tick_params(axis='both', which='major', labelsize=12, colors='white')  # Ticks com texto branco
# Adicionar grid no fundo
plt.grid(True, linestyle='--', color='gray', alpha=0.3)
# Mostrar o gráfico
plt.show()
# Grafico de Barras
df_grouped = df.groupby("Setor")["Receita"].sum().reset_index()
plt.figure(figsize=(8,5))
plt.bar(df_grouped["Setor"], df_grouped["Receita"])
plt.title("Grafico de Barras Setor x Receita")
plt.xlabel("Setor")
plt.ylabel("Receita")
plt.show()
# Grafico de Pizza
df_part = df.groupby("Setor")["ParticipacaoMercado"].mean().reset_index()
plt.figure(figsize=(8,5))
plt.pie(df_part["ParticipacaoMercado"], autopct="%1.2f%%")
plt.title("Grafico de Pizza de Participacao do Mercado")
plt.show()
