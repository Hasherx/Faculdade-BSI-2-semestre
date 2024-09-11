texto=input("Escreva uma palavra:  ")
def contador():
    
    qntcaracteres = len(texto)
    return f"a quantidade de caracteres contida no texto é : " +  str(qntcaracteres)
    
print("o seguinte texto:", texto , "possui" ,contador())