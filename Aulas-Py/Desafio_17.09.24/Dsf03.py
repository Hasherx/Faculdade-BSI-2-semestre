num1 = int(input("Digite um numero : "))

divisores = []

for i in range(1, num1 + 1):
    if num1 % i == 0:
        divisores.append(i)

print(f"Os divisores de {num1} são: {divisores}")

if len(divisores) == 2: 
    print(f"{num1} é um número primo.")
