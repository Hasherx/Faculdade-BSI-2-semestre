def maior_numero(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

maior = maior_numero(numero1, numero2)
print(f"O maior número entre {numero1} e {numero2} é: {maior}")
