import pandas as pd
file = "estoqueacv_1.xlsx"
df=pd.read_excel(file, sheet_name="Consulta")
df.isna().sum()
df[df["Cliente/Fornecedor"].isna()]

