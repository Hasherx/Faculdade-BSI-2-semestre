
nome = input("Digite seu nome : ")
idade = int(input("Digite sua idade : "))

#100 - idade = x (x = valor que falta ate 100)
idade_ate_100 = 100 - idade

txtate100 = f"{nome} o tempo que falta para você atingir 100 anos é : {idade_ate_100} anos"

print(txtate100)

randomnum = int(input("Insira um numero aleatorio : "))

# Loop para repetir o numero enserido em idade_ate_100 quantas vezes for colocado em randomnum
for i in range(randomnum):
    print(f"{txtate100}\n")