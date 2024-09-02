import json

def calcular_faturamento(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    faturamento = [d['valor'] for d in data['faturamento'] if d['valor'] > 0]
    
    if not faturamento:
        return "Não há dados de faturamento para calcular."
    
    menor_valor = min(faturamento)
    maior_valor = max(faturamento)
    media_mensal = sum(faturamento) / len(faturamento)
    
    dias_acima_da_media = sum(1 for valor in faturamento if valor > media_mensal)
    
    return {
        "menor_valor": menor_valor,
        "maior_valor": maior_valor,
        "dias_acima_da_media": dias_acima_da_media
    }

# Substitua 'faturamento.json' pelo caminho para o seu arquivo JSON
resultados = calcular_faturamento('faturamento.json')

print(f"Menor valor de faturamento: R${resultados['menor_valor']:.2f}")
print(f"Maior valor de faturamento: R${resultados['maior_valor']:.2f}")
print(f"Número de dias com faturamento acima da média: {resultados['dias_acima_da_media']}")
