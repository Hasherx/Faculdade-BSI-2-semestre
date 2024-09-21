def CelFah(celsius):
    return (celsius * 9/5) + 32

def FahCel(fahrenheit):
    return (fahrenheit - 32) * 5/9

def menu():
    print("Escolha qual voce deseja:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    escolha = input("Digite o número da sua escolha (1 ou 2): ")
    return escolha

opcao = menu()

if opcao == "1":
    valorcel = float(input("Digite a temperatura em Celsius: "))
    valorF = CelFah(valorcel)
    print(f"{valorcel}°C é igual a {valorF}°F.")
elif opcao == "2":
    valorF = float(input("Digite a temperatura em Fahrenheit: "))
    valorcel = FahCel(valorF)
    print(f"{valorF}°F é igual a {valorcel}°C.")
else:
    print("Opção inválida. Por favor, digite 1 ou 2.")
