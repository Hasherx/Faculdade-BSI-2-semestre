valor_produto = float(input("Qual o valor do produto : R$"))

valor_desconto = valor_produto * (10/100)

valor_final = valor_produto - valor_desconto


print(f"O valor final do produto com 10% de desconto é: R$ {valor_final:.2f}")