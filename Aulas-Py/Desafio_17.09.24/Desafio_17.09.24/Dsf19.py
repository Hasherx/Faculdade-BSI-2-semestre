# Função que realiza a operação
def calculadora(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 == 0:
            return "Erro: Divisão por zero não é permitida."
        else:
            return num1 / num2
    else:
        return "Operação inválida. Escolha entre +, -, * ou /."

def executar_calculadora():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Escolha a operação (+, -, *, /): ")

        resultado = calculadora(num1, num2, operacao)
        print("Resultado:", resultado)
    
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite números válidos.")

executar_calculadora()
