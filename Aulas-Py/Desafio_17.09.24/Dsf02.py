num = int(input("Digite um numero  :"))

if num % 2 == 0:
    print(f"O numero {num} é par.")
    if num % 4 == 0:
        print(f"O numero {num} é par e múltiplo de 4.")   
else:
    print(f"O numero {num} é impar.")


    
num1 = int(input("Digite um numero :"))
num2 = int(input("Digite um numero :"))

divn1n2 = num1 / num2

if num1 / 2 >= 0:
    print(f"O resultado da divisão é :{divn1n2}")
else:  
    print("A sua divisão dara um numero quebrado")