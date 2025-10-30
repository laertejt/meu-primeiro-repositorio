lista = []
nome = "laerte"
idade = 46
email = "laerte@laerte.com"
lista = [nome, idade, email]
lista[-1]
# 1.Crie uma lista frutas contendo as seguintes frutas: "maçã", "banana", "laranja", "uva".
frutas = ["maçã", "banana", "laranja", "uva"]
# 2.Imprima o primeiro e o último elemento da lista.
frutas[0]
frutas[-1]
# 3.Adicione a fruta "manga" ao final da lista.
frutas.append("manga")
frutas = frutas + ["manga"]
# 4.Remova a fruta "banana" da lista.
frutas.remove("banana")
# 5.Substitua "laranja" por "abacaxi".
indice = frutas.index("laranja")
frutas[indice] = "abacaxi" 
# 6.Crie uma lista numeros contendo os números de 1 a 10.
numeros = list(range(1,11))
# 7.	Calcule e imprima a soma de todos os números da lista.
soma = sum(numeros)
print(soma)
# 8.	Encontre e imprima o maior e o menor número da lista.
max(numeros)
min(numeros)
# 9.Inverta a ordem dos elementos na lista e imprima a lista invertida.
list(reversed(numeros))
# 10.Crie uma lista cidades contendo as seguintes cidades: "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba".
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]
# 11.	Ordene a lista cidades em ordem alfabética.
sorted(cidades)
# 12.	Adicione a cidade "Porto Alegre" ao final da lista.
cidades.append("Porto Alegre")
# 13.	Encontre o índice da cidade "Curitiba" na lista.
cidades.index("Curitiba")
# 14.	Remova a cidade "Rio de Janeiro" da lista.
cidades.remove("Rio de Janeiro")



# 21.	Crie uma lista nomes contendo os nomes: "Ana", "Pedro", "Maria", "João".
nomes=["Ana", "Pedro", "Maria", "João"]
# 22.	Utilize um loop for para imprimir cada nome da lista.
for nome in nomes:
    print(nome)
# 23.	Crie uma nova lista nomes_maiusculos contendo os nomes da lista nomes em letras maiúsculas. Utilize um loop for para isso.
nomes_mausculos = []
for i in nomes:
    i = i.upper()
    nomes_mausculos.append(i)
    print(nome)


# Exercicio da Temperatura
lista_temperatura = [10,20,30,40,50,60,70]
for temp in lista_temperatura:
    if temp > 30:
        print("Dia quente")
    else:
        print("Dia Agradvel")

# 24.	Crie uma lista numeros contendo os números de 1 a 20. Utilize um loop for para imprimir apenas os números pares.
for i in range(0,21,2):
    print(i)

# 28.Crie uma lista notas contendo [5.5, 7.0, 8.3, 4.9, 6.2]. 
# Utilize um loop for para contar quantos alunos estão aprovados 
# (nota >= 7) e quantos estão reprovados (nota < 7).
notas = [5.5, 7.0, 8.3, 4.9, 6.2]
aprovados = 0
nao_aprovados = 0


# 31 Escreva um programa que 
# use um loop while para imprimir os números de 1 a 10.
numero = 1
while numero <= 10:
    print(numero)
    numero = numero + 1
# 32. Usando um loop while, 
# peça para o usuário digitar um número inteiro. 
# O programa deve parar quando o usuário digitar o número 0.
while True:
    numero = int(input("Digite um numero:"))
    print(numero)
    if numero==0:
        print("Numero 0 digitado.")
        break
# 33. Utilize um loop while 
# para calcular a soma dos números de 1 a 100.
numero = 1
soma = 0
while numero <= 100:
    soma = soma + numero
    numero += 1
    print(soma)
# 34. Peça para o usuário adivinhar um número secreto 
# (por exemplo, 7). 
# Use um loop while para continuar 
# pedindo até que ele acerte.
while True:
    numero = int(input("Digite um numero:"))
    print(numero)
    if numero==7:
        print("Numero Correto.")
        break
    else:
        print("Numero Errado")
# 35. Crie um loop while que imprima 
# todos os números pares de 2 até 20.
numero = 2
while numero <= 20:
    print(numero)
    numero = numero + 2
    

