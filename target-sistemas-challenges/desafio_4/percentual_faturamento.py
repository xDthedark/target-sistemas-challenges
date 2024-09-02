# percentual_faturamento.py
import json

def percentual_faturamento(dados):
    total = sum(dados)
    percentuais = [(x / total) * 100 for x in dados]
    return percentuais

if __name__ == "__main__":
    with open('faturamento.json', 'r') as f:
        faturamento = json.load(f)
    
    percentuais = percentual_faturamento(faturamento)
    print("Percentuais de faturamento:")
    for percentual in percentuais:
        print(f"{percentual:.2f}%")
