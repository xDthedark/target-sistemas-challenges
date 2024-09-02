# soma_variavel.py
def soma_variavel(*args):
    return sum(args)

if __name__ == "__main__":
    import sys
    valores = map(float, sys.argv[1:])
    resultado = soma_variavel(*valores)
    print(f"A soma é: {resultado}")
