import tkinter as tk
from tkinter import messagebox

def mostrar_mensagem():
    nome = entrada_nome.get()
    peso = entrada_peso.get()
    altura = entrada_altura.get()
    
    if nome == "" or peso == "" or altura == "":
        messagebox.showerror("Erro","É necessário que você digite todos os campos!")
    else:
        try:
            peso = float(peso)
            altura = float(altura)
            imc = peso / (altura ** 2)
            
            
            peso_ideal_min = 19 * (altura ** 2)
            peso_ideal_max = 25 * (altura ** 2)
            diferenca_min = peso_ideal_min - peso  
            diferenca_max = peso - peso_ideal_max  
            
            if imc < 19:
                mensagem = f"Olá, {nome}! Seu IMC é {imc:.2f}, você está abaixo do peso ideal.\n"
                mensagem += f"Você precisa ganhar {abs(diferenca_min):.2f} kg para atingir o peso mínimo ideal."
            elif 19 <= imc <= 25:
                mensagem = f"Olá, {nome}! Seu IMC é {imc:.2f}, você está no peso ideal.\n"
                mensagem += f"Seu peso está ótimo! Mantenha-se entre {peso_ideal_min:.2f}kg e {peso_ideal_max:.2f}kg"
            elif 25 < imc <= 29:
                mensagem = f"Olá, {nome}! Seu IMC é {imc:.2f}, você está com sobrepeso.\n"
                mensagem += f"Você precisa perder {diferenca_max:.2f} kg para atingir o peso máximo ideal."
            elif 29 < imc <= 34:
                mensagem = f"Olá, {nome}! Seu IMC é {imc:.2f}, você está com obesidade grau 1.\n"
                mensagem += f"Você precisa perder {diferenca_max:.2f} kg para atingir o peso máximo ideal."
            elif 34 < imc <= 39:
                mensagem = f"Olá, {nome}! Seu IMC é {imc:.2f}, você está com obesidade grau 2.\n"
                mensagem += f"Você precisa perder {diferenca_max:.2f} kg para atingir o peso máximo ideal."
            else:
                mensagem = f"Olá, {nome}! Seu IMC é {imc:.2f}, você está com obesidade grau 3.\n"
                mensagem += f"Você precisa perder {diferenca_max:.2f} kg para atingir o peso máximo ideal."
                
            messagebox.showinfo("IMC", mensagem)
        except ValueError:
            messagebox.showerror("Erro","Digite valores válidos para peso e altura.")

def pressionar_enter(event):
    mostrar_mensagem()

janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("300x300")

rotulo_nome = tk.Label(janela, text="Digite seu nome:")
rotulo_nome.pack(padx=10, pady=10)

entrada_nome = tk.Entry(janela)
entrada_nome.pack(padx=10, pady=10)

rotulo_peso = tk.Label(janela, text="Digite seu peso (kg):")
rotulo_peso.pack(padx=10, pady=10)

entrada_peso = tk.Entry(janela)
entrada_peso.pack(padx=10, pady=10)

rotulo_altura = tk.Label(janela, text="Digite sua altura (m):")
rotulo_altura.pack(padx=10, pady=10)

entrada_altura = tk.Entry(janela)
entrada_altura.pack(padx=10, pady=10)

botao = tk.Button(janela, text="Calcular IMC", command=mostrar_mensagem) 
botao.pack(padx=10, pady=10) 


janela.bind('<Return>', pressionar_enter)  


janela.mainloop()