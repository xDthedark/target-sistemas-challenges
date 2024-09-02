def obter_dados_faturamento():
    # Dicionário para armazenar o faturamento por estado
    faturamento_por_estado = {}
    
    while True:
        # Solicita ao usuário o nome do estado
        estado = input("Digite o nome do estado (ou 'fim' para terminar): ")
        
        # Sai do loop se o usuário digitar 'fim'
        if estado.lower() == 'fim':
            break
        
        try:
            # Solicita o valor de faturamento para o estado
            valor = float(input(f"Digite o valor de faturamento para {estado}: R$"))
            # Adiciona o valor ao dicionário
            faturamento_por_estado[estado] = valor
        except ValueError:
            # Mensagem de erro se o valor inserido não for um número
            print("Valor inválido. Por favor, insira um número válido.")
    
    return faturamento_por_estado

def calcular_percentuais(faturamento_por_estado):
    # Calcula o faturamento total
    faturamento_total = sum(faturamento_por_estado.values())
    
    # Calcula o percentual de faturamento para cada estado
    percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_por_estado.items()}
    
    return percentuais

def encontrar_maior_menor_estado(faturamento_por_estado):
    # Encontra o estado com o maior faturamento
    estado_maior_faturamento = max(faturamento_por_estado, key=faturamento_por_estado.get)
    
    # Encontra o estado com o menor faturamento
    estado_menor_faturamento = min(faturamento_por_estado, key=faturamento_por_estado.get)
    
    return estado_maior_faturamento, estado_menor_faturamento

# Obtém os dados de faturamento do usuário
faturamento_por_estado = obter_dados_faturamento()

# Calcula os percentuais de faturamento
percentuais = calcular_percentuais(faturamento_por_estado)

# Encontra os estados com maior e menor faturamento
estado_maior_faturamento, estado_menor_faturamento = encontrar_maior_menor_estado(faturamento_por_estado)

# Exibe os resultados
print("\nPercentual de faturamento por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

print(f"\nEstado com o maior faturamento: {estado_maior_faturamento} - R${faturamento_por_estado[estado_maior_faturamento]:,.2f}")
print(f"Estado com o menor faturamento: {estado_menor_faturamento} - R${faturamento_por_estado[estado_menor_faturamento]:,.2f}")
