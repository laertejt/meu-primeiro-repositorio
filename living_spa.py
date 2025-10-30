import pandas as pd
file = "Dados de pagamentos living spa.xlsx"
df=pd.read_excel(file, sheet_name=None)
nomes_das_abas = list(df.keys())
len(nomes_das_abas)
index0 = nomes_das_abas.index("JANEIRO 2023")
index1 = nomes_das_abas.index("DEZEMBRO 2023")
nomes_das_abas = nomes_das_abas[index0:index1+1]
df_final=pd.DataFrame()
for aba in nomes_das_abas:
    df_temp = pd.read_excel(file, sheet_name=aba)
    df_final = pd.concat([df_final, df_temp], axis=0)
    print(aba)


