# Exercício 1: Criando um Dicionário
# Crie um dicionário chamado 'aluno' com as seguintes chaves:
# - 'nome': contendo um nome fictício,
# - 'idade': contendo a idade do aluno,
# - 'curso': contendo o curso que ele está matriculado.
# Após criar o dicionário, exiba seus valores no seguinte formato:
# Nome: <nome>
# Idade: <idade>
# Curso: <curso>
aluno = {
    "Nome": "Laerte",
    "Idade": 46,
    "Curso": "Economia",
}
print(aluno["Nome"])
print(aluno["Idade"])
print(aluno["Curso"])
# Exercício 2: Manipulação de Dicionário
# Dado o dicionário abaixo:
# produto = {
#     "nome": "Teclado Mecânico",
#     "preco": 350.00,
#     "estoque": 10
# }
# 1. Adicione uma nova chave chamada 'marca' com um valor de sua escolha.
# 2. Atualize o preço do produto para R$ 320,00.
# 3. Reduza o estoque em 2 unidades.
# 4. Remova a chave 'marca' do dicionário.
# 5. Exiba o dicionário atualizado.
produto = {
    "nome": "Teclado Mecânico",
    "preco": 350.00,
    "estoque": 10
}
produto["marca"] = "Toshiba"
produto["preco"] = 320.00
produto["estoque"] = produto["estoque"] - 2
produto.pop("marca")


# Exercício 3: Iterando sobre um Dicionário
# Dado o dicionário:
# notas = {
#     "Alice": 8.5,
#     "Bruno": 7.0,
#     "Carla": 9.2,
#     "Daniel": 6.8
# }
# 1. Itere sobre o dicionário e exiba os nomes dos alunos e suas respectivas notas.
notas = {
    "Alice": 8.5,
    "Bruno": 7.0,
    "Carla": 9.2,
    "Daniel": 6.8
}
# For loop
for key, value in notas.items():
    print(f"O aluno é {key} e a nota é {value}")
#
notas.keys()
notas.values()
# 2. Calcule a média das notas e exiba o resultado.
media = (notas["Alice"] + notas["Bruno"] + 
         notas["Carla"] + notas["Daniel"]) / 4
# Jeito Campeao
media = sum(notas.values()) / len(notas)
print(media)
# Exercício 4: Soma de Valores
# Dado um dicionário com valores numéricos, percorra o dicionário e some todos os valores.
# Exemplo:
# numeros = {"a": 10, "b": 20, "c": 30}
# Saída esperada: 60
numeros = {"a": 10, "b": 20, "c": 30}
soma = sum(numeros.values())
print(soma)
# Exercicio 5 
lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
frequencia = {}
for item in lista:
    if item in frequencia:
        frequencia[item] += 1
    else:
        frequencia[item] = 1
print(frequencia)

# Exercício 6: Filtrando Dicionário
# Dado um dicionário contendo produtos e seus preços, filtre os produtos que custam mais de R$ 50,00.
# Exemplo:
# produtos = {"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000}
# Saída esperada: {"mochila": 80, "notebook": 3000}
produtos = {"caneta": 10, 
            "mochila": 80, 
            "caderno": 45, 
            "notebook": 3000
            }
# Looser
for produto, preco in produtos.items():
    if preco >= 50:
        print(produto, "=" , preco)
# Campeao
filtro = {}
for produto, preco in produtos.items():
    if preco >= 50:
        filtro[produto] = preco
print(filtro)

# Exercício 7: Tradutor Simples
# Crie um dicionário chamado 'tradutor' que contém algumas palavras em inglês como chaves e suas traduções para português como valores.
# Peça ao usuário para digitar uma palavra em inglês e exiba sua tradução, caso exista no dicionário.
# Se a palavra não estiver cadastrada, exiba "Palavra não encontrada".

tradutor = {
    "door": "porta",
    "cat": "gato",
    "drink": "bebida"
}
palavra = input("Digite a palavra em inglês:")
if palavra in tradutor:
    print(f"Traducao: {tradutor[palavra]}")
else:
    print("Palavra nao encontrada")

# Exercício 8: Lista de Compras
# Crie um dicionário onde as chaves são nomes 
# de produtos e os valores são quantidades.
# Permita ao usuário adicionar produtos, atualizar 
# quantidades e remover itens.
# No final, exiba a lista completa de compras.
estoque = {}
remover = input("Remover item")
produto = input("Digite o produto")
quantidade = int(input("Digite a quantidade"))
if remover == "nao":
    if produto in estoque:
        estoque[produto] = estoque[produto] + quantidade
    else: 
        estoque[produto] = quantidade
    print(estoque)
else:
    estoque.pop(produto)
    print(estoque)

# turma = {
#     "Ana": {"idade": 17, "notas": [8, 9, 7]},
#     "Pedro": {"idade": 18, "notas": [6, 7, 8]},
#     "Mariana": {"idade": 17, "notas": [9, 10, 8]}
# }
turma = {
    "Ana": {"idade": 17, "notas": [8, 9, 7]},
    "Pedro": {"idade": 18, "notas": [6, 7, 8]},
    "Mariana": {"idade": 17, "notas": [9, 10, 8]}
}
# 1. Adicione um novo aluno ao dicionário.
turma["Laerte"] = {"idade": 46, "notas": [9, 10, 8]}
# 2. Calcule a média de notas de cada aluno e exiba no formato:
#    Ana: Média 8.0
#    Pedro: Média 7.0
#    Mariana: Média 9.0
for key, value in turma.items():
    media = sum(value["notas"]) / len(value["notas"])
    print(key, media)
# 3. Encontre o aluno com a maior média e exiba o nome dele.
maior_media = 0
aluno_maior_media = ""
for key, value in turma.items():
    if media > maior_media:
        maior_media = media
        aluno_maior_media = key
        print(aluno_maior_media, maior_media)


# Exercício 10: Cadastro de Funcionários
# Crie um programa que permita cadastrar funcionários em uma empresa.
# O programa deve permitir adicionar funcionários com os seguintes dados:
# - Nome
# - Cargo
# - Salário
# Os funcionários devem ser armazenados em um dicionário onde a chave é o nome e o valor é outro dicionário com os dados do funcionário.
# O programa deve permitir consultar funcionários pelo nome e exibir suas informações.
funcionarios = {}
nome=input("Nome do funcionário >>> ")
carg=input("Cargo do funcionário >>>> ")
sala=input("Salário >>> ")
funcionarios[nome] = {"Cargo":carg,"Salário":sala}
pesquisa= input("pesquise o funcionário >>> ")
if pesquisa in funcionarios:
    print(funcionarios[pesquisa])
else:
    print("funcionário não encontrado")