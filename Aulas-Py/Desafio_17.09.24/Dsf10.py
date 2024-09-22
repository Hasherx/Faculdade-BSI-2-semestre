# Crie um programa que peça o valor de um produto e aplique um desconto de 10%. Exiba o valor final com desconto.	Peça ao usuário o percentual de desconto e aplique-o dinamicamente.

def aplicar_desconto():
    try:
        valor_produto = float(input("Digite o valor do produto: R$ "))
        percentual_desconto = float(input("Digite o percentual de desconto (ex: 10 para 10%): "))

        desconto = (percentual_desconto / 100) * valor_produto
        valor_final = valor_produto - desconto

        print(f"\nO valor original do produto é: R$ {valor_produto:.2f}")
        print(f"O desconto aplicado foi de: R$ {desconto:.2f} ({percentual_desconto}%)")
        print(f"O valor final com desconto é: R$ {valor_final:.2f}")

    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

aplicar_desconto()