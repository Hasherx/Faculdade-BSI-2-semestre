from datetime import datetime

def verificar_data(data_str):
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
        return data
    except ValueError:
        return None

def calcular_dias_passados(data):
    hoje = datetime.now()
    diferenca = hoje - data
    return diferenca.days

data_mostrada = input("Digite uma data no formato DD/MM/AAAA: ")

data = verificar_data(data_mostrada)

if data:
    dias_passados = calcular_dias_passados(data)
    print(f"Desde {data_mostrada}, se passaram {dias_passados} dias.")
else:
    print("Data inválida. Por favor, tente novamente no formato DD/MM/AAAA.")
