def estoq_inicial():
    #Varialvel do produto
    product_name = "Camiseta"

    #variavel de preço
    product_value = 29.99

    #variavel da quantidade de estoque
    quant_stoq = 50

    #uma interface que informe o preço em r e quantidade em estoque
    print("Produto:", product_name)
    print("Preço: R$",product_value)
    print("Quantidade em estoque:", quant_stoq)

def venda_produto(quant_stoq,quantidadevendida):
    quant_stoq = quant_stoq - quantidadevendida
    print("quantidade em estoque:", quant_stoq)

venda_produto(50, 3)
venda_produto(47, 5)
venda_produto(42,2)

def cadastro():
    nome = input("Coloque seu nome")
    sobrenome = input("Coloque seu sobrenome")
    idade = print("coloque sua iadade")
    print("Nome :",nome)
    print("Idade :",idade)
    print("Sobrenome :", sobrenome)

cadastro("joão",23,"rodrigues")