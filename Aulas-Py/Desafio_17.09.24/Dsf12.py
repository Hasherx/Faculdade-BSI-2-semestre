entrada = input("Digite uma lista de números separados por vírgula: ")

numeros = [int(num) for num in entrada.split(",")]

numeros_ordenados = sorted(numeros)

numeros_repetidos = set([num for num in numeros if numeros.count(num) > 1])

print(f"Números em ordem crescente: {numeros_ordenados}")

if numeros_repetidos:
    print(f"Há números repetidos: {numeros_repetidos}")
else:
    print("Não há números repetidos.")
