def dividir(numerador, denominador):
    # Verifica se o denominador é zero para evitar erro de divisão por zero
    if denominador == 0:
        return "Erro: tem como denominador ser 0 n cara."
    else:
        return numerador / denominador

def multiplicar(a, b):
    return a * b

divid = dividir(10, 2) 
multi = multiplicar(10, 5) 

print("Resultado da divisão: ", divid)
print("Resultado da multiplicação: ", multi)