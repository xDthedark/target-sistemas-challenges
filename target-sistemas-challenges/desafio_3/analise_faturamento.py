# analise_faturamento.py
import json

def analisa_faturamento(dados):
    total = sum(dados)
    media = total / len(dados)
    acima_media = len([x for x in dados if x > media])
    return total, media, acima_media

if __name__ == "__main__":
    with open('faturamento.json', 'r') as f:
        faturamento = json.load(f)
    
    total, media, acima_media = analisa_faturamento(faturamento)
    print(f"Total: {total}")
    print(f"Média: {media}")
    print(f"Meses acima da média: {acima_media}")
