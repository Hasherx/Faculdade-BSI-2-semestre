# Manipulando Listas em Python

# 1. 
numeros = list(range(1, 11))
print("1. Lista de números:", numeros)

# 2. 
frutas = ["maçã", "banana", "laranja", "uva", "morango"]
print("\n2. Acessando frutas:")
print("Primeira fruta:", frutas[0])
print("Última fruta:", frutas[-1])

# 3. 
animais = []
animais.extend(["gato", "cachorro", "pássaro"])
animais.remove("gato")
print("\n3. Lista de animais atualizada:", animais)

# 4. 
numeros = [2, 4, 6, 8, 10]
soma = sum(numeros)
print("\n4. Soma dos números:", soma)

# 5. 
idades = [34, 12, 23, 56, 18, 45]
idades.sort()
print("\n5. Idades ordenadas:", idades)

# 6. 
cidades = ["Brasília", "Rio de Janeiro", "São Paulo", "Salvador", "Fortaleza"]
cidade_usuario = input("\n6. Digite o nome de uma cidade: ")
if cidade_usuario in cidades:
    print(f"A cidade {cidade_usuario} foi encontrada na lista.")
else:
    print(f"A cidade {cidade_usuario} não foi encontrada na lista.")

# 7. 
cores = ["azul", "vermelho", "verde", "amarelo"]
cores_invertidas = cores.copy()
cores_invertidas.reverse()
print("\n7. Lista original:", cores)
print("Lista invertida:", cores_invertidas)

# 8. 
nomes = ["Ana", "Pedro", "Ana", "João", "Pedro", "Maria"]
nomes_sem_duplicatas = list(dict.fromkeys(nomes))
print("\n8. Lista sem duplicatas:", nomes_sem_duplicatas)

# 9. 
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
valor_central = matriz[1][1]
print("\n9. Valor central da matriz:", valor_central)

# 10. 
palavras = ["sol", "lua", "estrela", "sol", "lua", "sol"]
contagem_sol = palavras.count("sol")
print("\n10. Ocorrências da palavra 'sol':", contagem_sol)
