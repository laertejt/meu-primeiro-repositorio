# 1 - Crie variáveis que representem:
# sua idade
idade = 46
# sua altura
altura = 1.73
# seu nome
nome = 'laerte'
# se você é estudante
eh_estudante = False
# para ver o tipo da variavel
type(eh_estudante)

# 2 - O usuário digita a sua idade.
# -   Converta essa entrada para número inteiro.
# -   Some +5 anos e mostre o resultado.
idade = input("Digite a sua idade:")
idade = int(idade) + 5
print(idade)

# 3.  Soma de Números Inteiros:
# Leia dois números inteiros e exiba a soma deles. 
# Entrada: Dois números inteiros. 
# Saída: A soma dos dois números. 
# Exemplo: Entrada: 3, 5 Saída: 8
num1 = input("Digite o primeiro numero:")
num2 = input("Digite o segundo numero:")
num1 = int(num1)
num2 = int(num2)
soma = num1 + num2
print(f"A Soma é igual a: {soma}")

# 4.  Média de Três Números Inteiros Enunciado:
# Escreva um programa que leia três números inteiros e determine a média deles. 
# Entrada: Três números inteiros.
# Saída: Média dos três números. 
# Exemplo: 
# Entrada: 5, 1, 12 
# Saída: 6
n1=int(input("Digite o primeiro numero:"))
n2=int(input("Digite o segundo numero:"))
n3=int(input("Digite o terceiro numero:"))
media = (n1+n2+n3)/3
print(f"A Media é igual a: {media}")

# 5.  Média Ponderada (Padrão Ibmec):
# Escreva um programa que receba as 3 notas das avaliações dos alunos e determine a média final através da ponderação padrão do Ibmec. 
# Entrada: Três números (notas). 
# Saída: Nota Final. 
# Exemplo: 
# Entrada: 5, 6.5, 10 
# Saída: 6
ap1=float(input("Digite o primeiro numero:"))
ap2=float(input("Digite o segundo numero:"))
ac=float(input("Digite o terceiro numero:"))
media = 0.4 * ap1 + 0.4 * ap2 + 0.2 * ac
print(media) 

# 6.  Manipulação de Strings:
# Peça o nome completo do usuário.
# -   Mostre o nome em letras maiúsculas.
# -   Mostre apenas o primeiro nome.
# -   Mostre a quantidade de letras do nome (sem contar os espaços).
nome = input("Digite o nome completo:")
nome.upper()
nome.split()
len(nome)