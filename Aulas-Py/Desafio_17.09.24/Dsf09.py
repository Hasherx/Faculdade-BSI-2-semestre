# Escreva um programa que peça a idade de várias pessoas até que um valor negativo seja inserido. Após isso, exiba a média das idades.	Informe também qual foi a maior idade fornecida.


# Inicializa as variáveis
idades = []
maior_idade = 0

while True:
    idade = int(input("Digite a idade (insira um valor negativo para parar): "))
    
    # Verifica se o valor é negativo
    if idade < 0:
        break
    
    idades.append(idade)
    
    if idade > maior_idade:
        maior_idade = idade

if idades:
    media_idades = sum(idades) / len(idades)
    print(f"\nA média das idades fornecidas é: {media_idades:.2f}")
    print(f"A maior idade fornecida foi: {maior_idade}")
else:
    print("\nNenhuma idade foi fornecida.")