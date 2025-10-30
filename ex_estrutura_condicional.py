
# 1. Par ou Ímpar
# Leia um número inteiro e informe se ele é par ou ímpar.
num1 = 10
if num1 % 2 == 0:
    print("O numero é par")
else:
    print("O numero é impar")

# 2. Aprovado ou Reprovado
# Leia a nota final de um aluno e diga se ele está:
# - Aprovado, se a nota for maior ou igual a 7.
# - Reprovado, se a nota for menor que 7.
ap1 = float(input("DIGITE a nota da ap1"))
ap2 = float(input("DIGITE a nota da ap2"))
ac = float(input("DIGITE a nota da ac"))
media = 0.4 * ap1 + 0.4 * ap2 + 0.2 * ac
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
# 3. Cálculo de Desconto
# Leia o valor de uma compra.
# - Se o valor for maior que 100, aplicar 10% de desconto.
# - Caso contrário, não aplicar desconto.
# - Mostrar o valor final.
valor = float(input("Digite o valor da sua compra"))
if valor > 100:
    desconto = valor * 0.1
    preco_final = valor - desconto
    print(f"Compra totalizando:{preco_final} \n e desconto: {desconto}")
else:
    preco_final = valor
    print(f"Valor Final:{preco_final}")

# 4. Conversão de Temperatura
# Leia a temperatura em Celsius e converta para Fahrenheit usando a fórmula: F = (C x 9/5) + 32.
celsius = float(input("Digite a temperatura:"))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperatura em Celsius {fahrenheit}")

# 5. Maior Número (Dois Valores)
# Leia dois números inteiros e informe:
# - Qual deles é o maior.
# - Ou se são iguais.
n1 = int(input("digite o n1:"))
n2 = int(input("digite o n2:"))
if n1 > n2:
    print("Primeiro é maior")
elif n2 > n1:
    print("Segundo é maior")
elif n1 == n2:
    print("Os dois sao iguais")
# 6. Maior Número (Três Valores)
# Escreva um programa que leia três números inteiros e determine qual deles é o maior.
# Entrada: Três números inteiros.
# Saída: O maior número.
# Exemplo:
# Entrada: 7, 2, 9
# Saída: 9
n1 = int(input("digite o n1:"))
n2 = int(input("digite o n2:"))
n3 = int(input("digite o n3:"))
if n1 > n2 and n1 > n3:
    print(f"Print {n1}")
elif n2 > n1 and n2 > n3:
    print(f"Print {n2}")
elif n3 > n1 and n3 > n2:
    print(f"Print {n3}")
else:
    print("Todas sao iguais")
# maior = n1
# if maior < n2:
#     maior = n2
# if maior < n3:
#     maior = n3
# print(f"Numero maior é o {maior}")

# 7. Calculadora Simples
# Crie uma calculadora simples que permita ao usuário realizar operações básicas: soma (+), subtração (-), multiplicação (*) e divisão (/).
# Entrada: Dois números e a operação desejada.
# Saída: O resultado da operação.
# Exemplo:
# Entrada: 8, 4, "/"
# Saída: 2
n1 = float(input("digite o n1:"))
n2 = float(input("digite o n2:"))
operacao = input("Digite a operacao:")
if operacao=="+":
    resultado=n1+n2
elif operacao=="-":
    resultado=n1-n2
elif operacao=="*":
    resultado=n1*n2
elif operacao=="/":
    if n2!=0:
        resultado=n1/n2
    else:
        print("divisao por zero")
print(f"Resultado é {resultado}")

# 8. Contagem de Números
# Leia uma sequência de números inteiros e conte quantos são positivos, negativos e zeros.
# Entrada: Lista de números inteiros (o usuário decide quantos números serão inseridos).
# Saída: Quantidade de números positivos, negativos e zeros.
# Exemplo:
# Entrada: [3, -1, 0, 7, -5]
# Saída: 2 positivos, 2 negativos, 1 zero
lista = [3, -1, 0, 7, -5]
numero_positivo = 0
numero_negativo = 0
for n in lista:
    if n > 0:
        numero_positivo = numero_positivo + 1
        print("numero positivo")
    elif n < 0:
        numero_negativo = numero_negativo + 1
        print("numero negativo")
    else:
        print("Numero é zero")
print(f"Numero Positivo: {numero_positivo}")
print(f"Numero Negativo: {numero_negativo}")
# 9. Ano Bissexto
# Leia um número inteiro representando um ano e verifique se ele é bissexto ou não.
# Entrada: Um ano (número inteiro).
# Saída: "Bissexto" ou "Não é bissexto".
# Exemplo:
# Entrada: 2024
# Saída: Bissexto
ano = 100
if ano % 4 == 0:
    print("Ano Bissexto")
else:
    print("Ano NAO Bissexto")
# 10. Intervalo de Idade
# Leia a idade de uma pessoa e informe se ela está na faixa etária permitida (18 a 65 anos).
# - Se a idade estiver entre 18 e 65 (inclusive), mostrar: "Dentro da faixa permitida".
# - Caso contrário, mostrar: "Fora da faixa permitida".
# (Use >= e <= com and).
idade = 17
if idade >= 18 and idade <= 65:
    print("Dentro da faixa permitida")
else:
    print("Fora da faixa permitida")
# 11. Acesso ao Sistema
# Leia o usuário e a senha digitados.
# - Se usuário == "admin" e senha == "1234", mostrar: "Acesso permitido".
# - Caso contrário, mostrar: "Acesso negado".
# (Use == e and).
user = input("Digite o usuario:")
password = input("Digite a senha:")
if user=="eduardo" and password=="1234":
    print("acesso permitido")
else:
    print("acesso negado")
# 12. Voto Obrigatório
# Leia a idade de uma pessoa.
# - Se a idade for menor que 16, mostrar "Não vota".
# - Se a idade for entre 18 e 70, mostrar "Voto obrigatório".
# - Caso contrário, mostrar "Voto facultativo".
# (Use combinações com and e or).
idade = int(input("Digite a idade:"))
if idade <= 16:
    print("Nao vota")
elif idade >= 18 and idade <= 70:
    print("voto obrigatorio")
else:
    print("voto optativo")
# 13. Número Fora de Intervalo
# Leia um número inteiro e verifique:
# - Se o número não está no intervalo de 10 a 50, mostrar "Fora do intervalo".
# - Caso contrário, mostrar "Dentro do intervalo".
# (Use not com >= e <=).
numero = int(input("Digite seu numero:"))
if numero >= 10 and numero <= 50:
    print("dentro do intervalor")
else:
    print("fora do intervalo")
# 14. Aluno Aprovado com Recuperação
# Leia a média final de um aluno.
# - Se a média for >= 7, mostrar "Aprovado".
# - Se a média for >= 5 e < 7, mostrar "Recuperação".
# - Caso contrário, mostrar "Reprovado".
# (Use and, >=, <).
media_final = float(input("Digite a sua media:"))
if media_final >= 7:
    print("Aprovado")
elif media_final >= 5 and media_final < 7:    
    print("Recuperacao")
else:
    print("Reprovado")


# 29.Crie uma lista palavras com ["arara", "banana", "radar", "python"].
# Utilize um loop for para identificar e imprimir quais palavras são 
# palíndromos (iguais quando lidas de trás para frente).
lista_palavras = ["arara", "banana", "radar", "python"]
for palavra in lista_palavras:
    if palavra == palavra[::-1]:
        print(palavra) 





