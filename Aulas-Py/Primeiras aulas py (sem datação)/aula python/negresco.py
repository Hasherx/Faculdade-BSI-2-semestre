produto = "camiseta"
preço_produto = 29.99     
estoque = 50 
print ("produto: ", produto)
print ("preço, ", preço_produto)
print ("estoque: ", estoque)

def vendaproduto(quantidade):
    global estoque
    estoque = quantidade - 1
    print ("estoque: ",estoque)

vendaproduto (5)
vendaproduto (10)




def multiplicar(a, b):
    print("Multipicacao: ", a*b)

def divisao(a, b):
    print("Divisao: ", a/b)

multiplicar(40, 10)
divisao(5, 4)