# Questão 1
numero = int(input("Digite um número inteiro: "))
if numero > 0:
    if numero % 2 == 0:
        print(f"O número {numero} é positivo e par.")
    else:
        print(f"O número {numero} é positivo e ímpar.")
elif numero < 0:
    print(f"O número {numero} é negativo.")
else:
    print("O número é zero.")

# Questão 2
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
if num1 > num2 and num1 > num3:
    print(f"O maior número é {num1}.")
elif num2 > num1 and num2 > num3:
    print(f"O maior número é {num2}.")
else:
    print(f"O maior número é {num3}.")

# Questão 3
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
if media < 60:
    print("O aluno foi reprovado.")
elif media > 70:
    print("O aluno foi aprovado com distinção.")
else:
    print("O aluno foi aprovado.")

# Questão 4
idade = int(input("Digite a idade da pessoa: "))
if idade < 12:
    print("A pessoa é uma criança.")
elif 12 <= idade <= 17:
    print("A pessoa é um adolescente.")
elif 18 <= idade <= 64:
    print("A pessoa é um adulto.")
else:
    print("A pessoa é um idoso.")

# Questão 5
numero = int(input("Digite um número: "))
if numero % 2 == 0 and numero % 3 == 0:
    print("O número é divisível por 2 e 3.")
elif numero % 2 == 0:
    print("O número é divisível por 2.")
elif numero % 3 == 0:
    print("O número é divisível por 3.")
else:
    print("O número não é divisível por 2 ou 3.")

# Questão 6
lista_original = [1, 2, 3, 4, 5]
lista_clonada = list(lista_original)
lista_clonada[0] = 10
print("Lista original:", lista_original)
print("Lista clonada:", lista_clonada)

# Questão 7
nomes = []
for i in range(5):
    nomes.append(input(f"Digite o {i+1}º nome: "))
nomes_clone = nomes[:]
print("Lista original de nomes:", nomes)
print("Lista clonada de nomes:", nomes_clone)

# Questão 8
import copy
numeros = [10, 20, 30, 40]
numeros_clone = copy.copy(numeros)
numeros_clone[-1] = 99
print("Lista original de números:", numeros)
print("Lista clonada de números:", numeros_clone)

# Questão 9
lista1 = [1, 2, 3]
lista2 = lista1
lista2[0] = 10
print("Lista 1:", lista1)

lista3 = [1, 2, 3]
lista4 = copy.copy(lista3)
lista4[0] = 10
print("Lista 3:", lista3)

lista5 = [1, 2, 3]
lista6 = lista5[:]
lista6[0] = 10
print("Lista 5:", lista5)

# Questão 10
itens = ["maçã", "banana", "laranja"]
itens_clone = copy.deepcopy(itens)
itens_clone[1] = "manga"
print("Lista original de itens:", itens)
print("Lista clonada de itens:", itens_clone)
