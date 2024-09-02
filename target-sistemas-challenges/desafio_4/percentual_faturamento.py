# Dados de faturamento por estado
faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

def calcular_percentuais(faturamento_por_estado):
    faturamento_total = sum(faturamento_por_estado.values())
    percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_por_estado.items()}
    return percentuais

def encontrar_maior_menor_estado(faturamento_por_estado):
    estado_maior_faturamento = max(faturamento_por_estado, key=faturamento_por_estado.get)
    estado_menor_faturamento = min(faturamento_por_estado, key=faturamento_por_estado.get)
    return estado_maior_faturamento, estado_menor_faturamento

percentuais = calcular_percentuais(faturamento_por_estado)
estado_maior_faturamento, estado_menor_faturamento = encontrar_maior_menor_estado(faturamento_por_estado)

print("Percentual de faturamento por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

print(f"\nEstado com o maior faturamento: {estado_maior_faturamento} - R${faturamento_por_estado[estado_maior_faturamento]:,.2f}")
print(f"Estado com o menor faturamento: {estado_menor_faturamento} - R${faturamento_por_estado[estado_menor_faturamento]:,.2f}")
