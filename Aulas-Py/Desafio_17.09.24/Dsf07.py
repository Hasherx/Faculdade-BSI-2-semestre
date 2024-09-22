# Crie uma função que receba uma lista de números e retorne apenas os números pares.	Implemente uma função adicional que retorne a soma dos números pares da lista.

def soma_pares(lista):
    pares = filtrar_pares(lista)
    return sum(pares)

def receber_numeros():
    entrada = input("Insira os números separados por espaço: ")
    lista_numeros = list(map(int, entrada.split()))
    return lista_numeros


numeros = receber_numeros()


numeros_pares = filtrar_pares(numeros)
print(f"Números pares: {numeros_pares}")


soma_dos_pares = soma_pares(numeros)
print(f"Soma dos números pares: {soma_dos_pares}")
