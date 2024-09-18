
def saudacao():
    return f"Seja bem vindo {nome}"

def contador():
    return len(nome)

nome = input("Qual é seu nome ?: ")  

print(saudacao()) 

print(f"Seu nome tem {contador()} letras.")
