import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def mostrar_mensagem():
    nome = entrada_nome.get()
    peso = entrada_peso.get()
    altura = entrada_altura.get()
    
    if nome == "" or peso == "" or altura == "":
        messagebox.showerror("Erro","É necessário que você digite todos os campos!")
        return  # Retorna se algum campo estiver vazio
        
    # Substitui vírgula por ponto para evitar erros de digitação
    peso = peso.replace(',', '.')
    altura = altura.replace(',', '.')
    
    try:
        peso = float(peso)
        altura = float(altura)
        
        # Validação adicional
        if peso <= 0 or altura <= 0:
            messagebox.showerror("Erro", "Peso e altura devem ser maiores que zero!")
            return
            
        imc = peso / (altura ** 2)
        
        # Calcula o peso ideal e diferenças uma única vez
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
        print(f"IMC calculado: {imc}")  # Para debug
        mostrar_grafico(imc)  # Passa o IMC calculado para o gráfico
        
    except ValueError:
        messagebox.showerror("Erro", "Digite valores válidos para peso e altura.\nExemplos:\nPeso: 70.5\nAltura: 1.75")

def mostrar_tabela_referencia():
    tabela = tk.Toplevel(janela)
    tabela.title("Tabela de Referência IMC")
    tabela.geometry("300x200")
    
    # Estilo para a tabela
    style = ttk.Style()
    style.configure("Cabecalho.TLabel", font=('Arial', 10, 'bold'))
    
    # Cabeçalho
    ttk.Label(tabela, text="Classificação", style="Cabecalho.TLabel").grid(row=0, column=0, padx=5, pady=5)
    ttk.Label(tabela, text="IMC", style="Cabecalho.TLabel").grid(row=0, column=1, padx=5, pady=5)
    
    # Dados da tabela
    referencias = [
        ("Abaixo do peso", "< 19"),
        ("Peso normal", "19 - 25"),
        ("Sobrepeso", "25 - 29"),
        ("Obesidade Grau 1", "29 - 34"),
        ("Obesidade Grau 2", "34 - 39"),
        ("Obesidade Grau 3", "> 39")
    ]
    
    for i, (categoria, faixa) in enumerate(referencias, 1):
        ttk.Label(tabela, text=categoria).grid(row=i, column=0, padx=5, pady=2)
        ttk.Label(tabela, text=faixa).grid(row=i, column=1, padx=5, pady=2)

def mostrar_grafico(imc):
    try:
        grafico = tk.Toplevel(janela)
        grafico.title("Gráfico de IMC")
        grafico.geometry("600x400")
        
        fig = Figure(figsize=(10, 6))
        ax = fig.add_subplot(111)
        
        # Definir as faixas de IMC com cores válidas
        faixas = [
            (0, 19, '#FF4444'),    # Vermelho claro
            (19, 25, '#44FF44'),   # Verde
            (25, 29, '#FFFF44'),   # Amarelo
            (29, 34, '#FFA500'),   # Laranja
            (34, 39, '#FF4444'),   # Vermelho claro
            (39, 45, '#CC0000')    # Vermelho escuro
        ]
        
        # Plotar as faixas coloridas
        for inicio, fim, cor in faixas:
            ax.axvspan(inicio, fim, alpha=0.3, color=cor)
        
        # Adicionar linha vertical para o IMC atual
        ax.axvline(x=imc, color='blue', linestyle='-', linewidth=2, label='Seu IMC')
        
        # Configurações do gráfico
        ax.set_xlim(15, 45)
        ax.set_ylim(0, 1)
        ax.set_title('Seu IMC em relação às faixas de referência')
        ax.set_xlabel('IMC')
        ax.get_yaxis().set_visible(False)
        
        # Adicionar legendas das faixas
        ax.text(17, 0.5, 'Abaixo\ndo peso', ha='center')
        ax.text(22, 0.5, 'Peso\nideal', ha='center')
        ax.text(27, 0.5, 'Sobrepeso', ha='center')
        ax.text(31.5, 0.5, 'Obesidade\nGrau 1', ha='center')
        ax.text(36.5, 0.5, 'Obesidade\nGrau 2', ha='center')
        ax.text(42, 0.5, 'Obesidade\nGrau 3', ha='center')
        
        canvas = FigureCanvasTkAgg(fig, master=grafico)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    except Exception as e:
        print(f"Erro ao criar gráfico: {e}")  # Para debug
        messagebox.showerror("Erro", "Erro ao gerar o gráfico")

def criar_menu():
    menu_bar = tk.Menu(janela)
    janela.config(menu=menu_bar)
    
    # Menu Arquivo
    arquivo_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Arquivo", menu=arquivo_menu)
    arquivo_menu.add_command(label="Limpar Campos", command=limpar_campos)
    arquivo_menu.add_separator()
    arquivo_menu.add_command(label="Sair", command=janela.quit)
    
    # Menu Visualizar
    visualizar_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Visualizar", menu=visualizar_menu)
    visualizar_menu.add_command(label="Tabela de Referência", command=mostrar_tabela_referencia)

def limpar_campos():
    entrada_nome.delete(0, tk.END)
    entrada_peso.delete(0, tk.END)
    entrada_altura.delete(0, tk.END)

def criar_tooltip(widget, texto):
    def mostrar_tooltip(event):
        tooltip = tk.Toplevel()
        tooltip.overrideredirect(True)
        tooltip.configure(bg='black')
        
        label = tk.Label(tooltip, text=texto, bg="black", fg="white", padx=5, pady=2)
        label.pack()
        
        x = widget.winfo_rootx() + widget.winfo_width() + 5
        y = widget.winfo_rooty()
        tooltip.geometry(f"+{x}+{y}")
        
        widget.tooltip = tooltip
        
    def esconder_tooltip(event):
        if hasattr(widget, 'tooltip'):
            widget.tooltip.destroy()
            
    widget.bind('<Enter>', mostrar_tooltip)
    widget.bind('<Leave>', esconder_tooltip)

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("400x300")

# Criar menu
criar_menu()

# Frame principal
frame_principal = ttk.Frame(janela, padding="10")
frame_principal.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Widgets
rotulo_nome = ttk.Label(frame_principal, text="Digite seu nome:")
rotulo_nome.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

entrada_nome = ttk.Entry(frame_principal)
entrada_nome.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

rotulo_peso = ttk.Label(frame_principal, text="Digite seu peso (kg):")
rotulo_peso.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

entrada_peso = ttk.Entry(frame_principal)
entrada_peso.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

rotulo_altura = ttk.Label(frame_principal, text="Digite sua altura (m):")
rotulo_altura.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

entrada_altura = ttk.Entry(frame_principal)
entrada_altura.grid(row=2, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

botao = ttk.Button(frame_principal, text="Calcular IMC", command=mostrar_mensagem)
botao.grid(row=3, column=0, columnspan=2, pady=20)

# Adicionar tooltips
criar_tooltip(entrada_nome, "Digite seu nome completo")
criar_tooltip(entrada_peso, "Digite seu peso em quilogramas (ex: 70.5)")
criar_tooltip(entrada_altura, "Digite sua altura em metros (ex: 1.75)")

# Configurar redimensionamento
janela.columnconfigure(0, weight=1)
janela.rowconfigure(0, weight=1)
frame_principal.columnconfigure(1, weight=1)

# Vincular tecla Enter
janela.bind('<Return>', lambda event: mostrar_mensagem())

janela.mainloop()