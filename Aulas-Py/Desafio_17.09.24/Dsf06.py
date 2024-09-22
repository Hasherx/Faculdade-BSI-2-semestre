# Crie um programa que peça ao usuário três números e imprima a média deles.	Verifique e informe se algum dos números fornecidos é maior que 100.

numero1 = float(input("Digite o primeiro número: "));
numero2 = float(input("Digite o segundo número: "));
numero3 = float(input("Digite o terceiro número: "));

media = (numero1 + numero2 + numero3) / 3;

print(f"A média dos três números é: {media}");

if numero1 > 100 :
    print("O primeiro numero e maior que 100");
    if numero2 > 100:
        print("O segundo numero e maior que 100");
        if numero3 > 100:
            print("O terceiro numero e maior que 100");
        else:
            print();
    else:
        print();
else:
    print("nenhum numero e maior que 100");

# Função para retornar os números pares
def filtrar_pares(lista):
    return [num for num in lista if num % 2 == 0]

