import tkinter as tk
from tkinter import messagebox

def mostrar_mensagem():
    nome = entrada_nome.get()
    peso = entrada_peso.get()
    altura = entrada_altura.get()
    
    if nome == "" or peso == "" or altura == "":
        messagebox.showerror("Erro","E necessario que voce digite todos os campos!")
    else:
        try:
            peso = float(peso)
            altura = float(altura)
            imc = peso / (altura ** 2)
            
            if imc < 19:
                mensagem = f"Olá, {nome}! Seu IMC é {imc:.2f}, você está abaixo do peso ideal."
            elif 19 <= imc <= 25:
                mensagem = f"Olá, {nome}! Seu IMC é {imc:.2f}, você está no peso ideal."
            elif 25 <= imc <= 29:
                mensagem = f"Olá, {nome}! Seu IMC é {imc:.2f}, você está com sobrepeso."
            elif 29 <= imc <= 34:
                mensagem = f"Olá, {nome}! Seu IMC é {imc:.2f}, você está com obesidade grau 1."
            elif 34 <= imc <= 39:
                mensagem = f"Olá, {nome}! Seu IMC é {imc:.2f}, você está com obesidade grau 2."
            else:
                mensagem = f"Olá, {nome}! Seu IMC é {imc:.2f}, você está com obesidade grau 3."
                
            messagebox.showinfo("IMC", mensagem)
        except ValueError:
            messagebox.showerror("Erro","Digite valores válidos para peso e altura.")

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


janela.mainloop()
