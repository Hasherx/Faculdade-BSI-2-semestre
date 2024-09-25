# Q1
x = 10

print(x)

# Q2

def função():
    x = 20
    print(x)
# Def para definir função...

# Q3
print("Olá, mundo!")

# Q4
list=["garapa","seila","exemplo"]
list.append("elemento")

print(list)


# Q5
y = 10/2
print(y)

# Q6
a = 5
b = 10
print(a + b)

# Q7
list.pop()
print(list)

# Q8
# e int.

# Q9
x2 = 25

# Q11
u = 10
u -= 7
print(u)

# Q12
rs = 10**2
print(rs)

# Q13
xis = 20//3
print(xis)

# Q14
u+=5
print(u)

# Q15
num = int(input("Digite um numero  :"))
if num % 2 == 0:
    print(f"O numero {num} é par.")
else:
    print(f"O numero {num} é impar.")

# Q16
def verifica_par(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
print(verifica_par(int(input("Digite um numero para ver se ele e par : "))))

# Q17
def maior_numero(n1,n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return "Números iguais"
print(maior_numero(input("Digite o primeiro numero: "), input("Digite o segundo numero: ")))

# Q18
def verifica_positivo_negativo(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Zero"
print(verifica_positivo_negativo(int(input("Verificador de numero positivo\nDigite um numero: "))))

# Q19
def e_maior_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"
print(e_maior_idade(int(input("Verificador de maioridade\nDigite sua idade: "))))

# Q20
def nota_final(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
print(nota_final(float(input("Verificador de nota final\nDigite a sua média: "))))

# Q21
def calcula_imposto(salario: float, dependentes: int):
    if salario < 2000.00:
        imposto = 0.00
    elif 2000.00 <= salario <= 4000.00:
        imposto = (salario - 2000.00) * 0.15
    elif 4000.00 < salario:
        imposto = (salario - 4000.00) * 0.25 + (4000.00 - 2000.00) * 0.15
    reducao = dependentes * 200.00
    imposto -= reducao
    
    if imposto<0:
        return 0.0
    return f"R${imposto} e o valor que deve ser pago"
print("Calculadora de impostos!")
salario = float(input("Digite o salário: "))
dependentes = int(input("Digite o número de dependentes: "))
print(calcula_imposto(salario, dependentes))

# Q22
def classificar_triangulo(lado1,lado2,lado3):
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        if lado1 == lado2 == lado3:
            return "Equilátero"
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "Isósceles"
        else:
            return "Escaleno"
    else:
        return "Não é possível formar um triângulo com os lados fornecidos."
lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))
print(classificar_triangulo(lado1, lado2, lado3))