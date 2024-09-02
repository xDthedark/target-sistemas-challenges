from typing import Union

def inverter_string(s: str) -> str:
    """
    Inverte os caracteres de uma string fornecida.

    Args:
        s (str): A string a ser invertida.

    Returns:
        str: A string invertida.
    """
    # Cria uma lista vazia para armazenar os caracteres invertidos
    invertida = []

    # Itera sobre a string original do final para o início
    for i in range(len(s) - 1, -1, -1):
        invertida.append(s[i])

    # Converte a lista de volta para uma string e retorna
    return ''.join(invertida)

def obter_string_entrada() -> str:
    """
    Obtém uma string do usuário ou usa uma string definida no código.

    Returns:
        str: A string fornecida pelo usuário ou a string definida no código.
    """
    escolha = input("Digite '1' para inserir uma string ou '2' para usar uma string pré-definida: ")
    
    if escolha == '1':
        return input("Digite uma string para inverter: ")
    elif escolha == '2':
        return "exemplo"  # Alterar para a string desejada
    else:
        raise ValueError("Escolha inválida. Digite '1' ou '2'.")

def main():
    try:
        entrada = obter_string_entrada()
        resultado = inverter_string(entrada)
        print(f"String invertida: {resultado}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
