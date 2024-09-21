def pali(texto):
    texto = txt.replace(" ","").lower()
    if texto == texto[::-1]:
        return f"{txt} é um palíndromo."
    else:
        return f"{txt} não é um palíndromo."
    
txt = input("Digite uma palavra: ")

print(pali(txt))