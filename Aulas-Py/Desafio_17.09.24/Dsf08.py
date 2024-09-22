# Peça ao usuário uma frase e conte quantas palavras existem na frase.	Implemente uma função que também conte quantas palavras têm mais de 5 letras.

def contar_palavras_e_maiores(frase):

    separacao = frase.split()
    total_palavras = len(separacao)
    palavras_maiores_5 = sum(1 for palavra in separacao if len(palavra) > 5)
    return total_palavras, palavras_maiores_5

frase = input("Coloque sua frase aqui: ")
total, maiores_5 = contar_palavras_e_maiores(frase)

print(f"Essa é a quantidade total de palavras: {total}")
print(f"Essa é a quantidade de palavras com mais de 5 letras: {maiores_5}")