# Função recursiva para calcular o fatorial
def fatorial(n):
    if n == 0 or n == 1:  
        return 1
    else:
        return n * fatorial(n - 1)  

def calcular_fatorial():
    try:
        numero = int(input("Digite um número inteiro não negativo: "))
        
        if numero < 0:
            print("Erro: Não existe fatorial para números negativos.")
        else:
            resultado = fatorial(numero)
            print(f"O fatorial de {numero} é {resultado}.")
    
    except ValueError:
        print("Erro: Por favor, insira um número inteiro válido.")

calcular_fatorial()
