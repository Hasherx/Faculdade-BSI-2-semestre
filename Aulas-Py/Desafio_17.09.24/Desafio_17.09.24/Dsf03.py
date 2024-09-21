num1 = int(input("Digite um numero : "))

divisores = []

for i in range(1, num1 + 1):
    if num1 % i == 0:
        divisores.append(i)

print(f"Os divisores de {num1} são: {divisores}")

if len(divisores) == 2: 
    print(f"{num1} é um número primo.")
    
num2 = int(input("Digite outro numero : "))

divisores_2 = []

for i in range(1, num2 + 1):
    if num2 % i == 0:
        divisores_2.append(i)
        print(f"Os divisores de {num2} são: {divisores_2}")