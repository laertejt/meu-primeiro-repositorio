import streamlit as st
import pandas as pd

st.title("Meu primeiro Dashboard.")
st.text("meu nome é Laerte")
st.button("Aperte aqui")
st.slider("Idade", 0 ,100, 25)
df = pd.read_csv("imoveis_brasil.csv")
st.dataframe(df)

import matplotlib.pyplot as plt
import pandas as pd
file="empresas_desempenho.csv"
df=pd.read_csv(file)
# Grafico de Barras
df_grouped = df.groupby("Setor")["Receita"].sum().reset_index()
fig = plt.figure(figsize=(8,5))
plt.bar(df_grouped["Setor"], df_grouped["Receita"])
plt.title("Grafico de Barras Setor x Receita")
plt.xlabel("Setor")
plt.ylabel("Receita")

st.pyplot(fig)
