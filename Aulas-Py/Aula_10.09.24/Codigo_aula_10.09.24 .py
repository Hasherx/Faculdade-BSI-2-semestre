# Função ela guarda parâmetros (atributos) e realiza ações (métodos), entregando um resultado.
# Função para calcular o preç do cachorro-quente.
## Parâmetro = qnt de cachorros-quentes comidos.
## Parâmetro = custo de um cachorro-quente.
## Método = calcular o valor da conta.
## Retorno = Valor da conta.

import math 

def conta_hot_dog(qnt_hotdog, price):
    valor_conta = qnt_hotdog * price 
    return valor_conta
print("O valor da conta é: ")
print (conta_hot_dog(4, 2.50))

# Função para calcular o preço do hot-dog.

# Situação 2 com a adição de mais um parametro

def conta_hot_dog2(qnt_hotdog, price):
    valor_conta = (qnt_hotdog * price) * 1.05
    return valor_conta
print("O valor da conta com imposto é: ")
print (conta_hot_dog2(4, 2.50))

# Eu tenho uma conta e quero ua função chama saque(). O cliente informa o valor e o saque é debitado da conta. A conta de ter um saldo inicial fornecido como parâmetro.
def saque(saldo_total,vlr_saque):
    Saldo_final =  vlr_saque - saldo_total
    return Saldo_final

print(saque(int(input("Qual valo deseja sacar? ")), 2000))

# Crie e uma função que calcule a área de um retangulo.
def area_retangulo(base, altura):
    area_retangulo = base * altura
    return f"A área do retângulo de base: {base}m e a altura: {altura} é de: {area_retangulo}m2."

print(area_retangulo(20, 15))

# crie uma função que calcule a área de um círculo. Considere pi = 3,14. A = pi*r**2

def Area_circulo(r):
    Area_circulo = math.pi * r**2
    return f"A área do círculo de raio: {r}m é de: {Area_circulo}m²."
print(Area_circulo(5))

# Criar uma função que gerencia a fila de um banco e chama os seus clientes em ordem

def fila_banco(fila_clientes):
    while fila_clientes:
        proximo_atendido = fila_clientes[0]
        fila_clientes.remove(proximo_atendido)
        print(f"O próximo cliente é : {proximo_atendido}")
        print(f"Restam na fila : {fila_clientes}")

fila_banco(["joão","maria", "carlos", "josé", "katarina", "bobs"])

# Crie uma função chamada soma() que receba dois números como parâmetros e retorne a soma deles.
## Dica: inpu() entrega valores do tipo string. Converta int() -> int("string")
def soma(a,b):
    return a + b 

print(soma(int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: "))))

# Crie uma função chamada par_ou_impar() que receba um número como parâmetro e retorne se ele é "Par" ou "Impar"

def par_ou_impar():
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        return "Par"
    else:
        return "Impar"

print(par_ou_impar())

# Crie uma função para saber se o numero e divisivel por 3

def numero_divisivel_por_3(num):
    if num % 3 == 0:
        return f"O seu numero  {num} é divisivel por 3"

    else:
        return f"O numero {num} não é divisivel por 3"

print(numero_divisivel_por_3(int(input("Digite um número: "))))