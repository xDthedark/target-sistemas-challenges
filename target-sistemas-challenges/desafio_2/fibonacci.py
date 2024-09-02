# fibonacci

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

if __name__ == "__main__":
    try:
        numero = int(input("Digite um número: "))
        fibonacci(numero)
    except ValueError:
        print("Por favor, forneça um número inteiro válido.")
