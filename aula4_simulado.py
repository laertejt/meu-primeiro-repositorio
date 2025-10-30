# Simulado – Programação Estruturada
# (0,1 ponto) 1 - Crie uma lista com os preços de cinco produtos de supermercado. 
# Calcule a soma total dos preços e exiba o valor da compra.
compra = [5, 5 ,4, 8, 10]
sum(compra)
# (0,1 ponto) 2 - Dado o dicionário:
# estoque = {"notebook": 5, "mouse": 12, "teclado": 8}
# Adicione um novo item chamado "monitor" com quantidade 3. Em seguida, exiba o dicionário atualizado.
estoque = {"notebook": 5, "mouse": 12, "teclado": 8}
estoque.update({"monitor": 3})
print(estoque)
# outra forma
estoque["monitor"]=3
# (0,2 ponto) 3 - Peça para o usuário digitar a nota final de um aluno de Administração e use if/elif/else para classificar:
# - "Aprovado" se a nota for maior ou igual a 7.
# - "Recuperação" se a nota for entre 5 e 6.9.
# - "Reprovado" se a nota for menor que 5.
nota_final = float(input("Digite a nota final:"))
if nota_final >= 7:
    print("Aprovado")
elif nota_final >= 5 and nota_final <= 6.9:
    print("Recuperacao")
else:
    print("Reprovado")
# (0,3 ponto) 4 - Considere a lista:
# cidades = ["São Paulo", "Nova York", "Rio de Janeiro", "Chicago", "Brasília", "Los Angeles"]
# Use um for loop para percorrer a lista e exiba quantas cidades são do Brasil.
cidades = ["São Paulo", "Nova York", "Rio de Janeiro", "Chicago", "Brasília", "Los Angeles"]
cidades_brasil = ["São Paulo",  "Rio de Janeiro", "Brasília"]
contador = 0
for cidade in cidades:
    if cidade in cidades_brasil:
        contador += 1
print(contador)
# 
cidade_br = []
for cidade in cidades:
    if cidade == "São Paulo" or cidade == "Rio de Janeiro" or cidade == "Brasília":
        cidade_br.append(cidade)
print(len(cidade_br))
# (0,3 ponto) 5 - Uma empresa de consultoria financeira fez uma pesquisa de satisfação com clientes em três regiões do Brasil. Os dados estão em um dicionário de listas:
# avaliacoes = {
#   "Norte": [7, 8, 6, 5, 9],
#   "Sul": [8, 9, 7, 10, 6],
#   "Sudeste": [9, 8, 9, 10, 9]
# }
# Calcule e mostre a média de satisfação de cada região usando o for loop no dicionário.
avaliacoes = {
  "Norte": [7, 8, 6, 5, 9],
  "Sul": [8, 9, 7, 10, 6],
  "Sudeste": [9, 8, 9, 10, 9]
}
for key, value in avaliacoes.items():
    media = sum(value) / len(value)
    print(media)
