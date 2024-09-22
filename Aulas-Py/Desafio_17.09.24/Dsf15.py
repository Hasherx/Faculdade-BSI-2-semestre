import random

numero_aleatorio = random.randint(1, 10)

palpite = int(input("Adivinhe o número que estou pensando entre 1 e 10: "))

if palpite == numero_aleatorio:
    print("Parabéns! Você acertou!")
elif palpite > numero_aleatorio:
    print(f"Errou! Seu palpite foi maior que o número. O número era {numero_aleatorio}.")
else:
    print(f"Errou! Seu palpite foi menor que o número. O número era {numero_aleatorio}.")
