import pandas as pd
import random
file_path = 'C:\\Users\\21701079836\\Documents\\estruturada\\lista_alunos.xlsx'  # coloque o caminho do seu arquivo aqui
df = pd.read_excel(file_path)
coluna_nomes = df.columns[2]
alunos = df[coluna_nomes].dropna().tolist()
aluno_sorteado = random.choice(alunos)
print(f"Aluno sorteado: {aluno_sorteado}")
